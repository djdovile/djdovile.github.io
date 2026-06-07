#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path
from datetime import datetime

# Publication type mapping
TYPE_MAP = {
    '2': 'article-journal',
    '5': 'book',
    '6': 'chapter'
}

# Keywords for auto-tagging
TAG_KEYWORDS = {
    'russia': ['russia', 'russian', 'soviet', 'ussr'],
    'geopolitics': ['geopolitical', 'geopolitics', 'foreign policy', 'international relations', 'security'],
    'baltic': ['baltic', 'lithuania', 'latvia', 'estonia', 'baltic states'],
    'energy': ['energy', 'oil', 'gas', 'fossil'],
    'eu': ['european union', 'eu ', 'europe'],
    'democracy': ['democracy', 'democratic', 'governance'],
    'conflict': ['conflict', 'war', 'ukraine', 'nato'],
    'identity': ['identity', 'nation', 'nationalism', 'sovereignty'],
    'security': ['security', 'defense', 'military'],
}

def extract_summary(abstract):
    """Extract first sentence from abstract as summary."""
    if not abstract or not abstract.strip():
        return "Publication summary."
    
    # Split on periods, question marks, or exclamation marks
    sentences = re.split(r'(?<=[.!?])\s+', abstract.strip())
    summary = sentences[0] if sentences else "Publication summary."
    
    # Truncate if too long
    if len(summary) > 100:
        summary = summary[:97] + "..."
    
    return summary

def get_tags(title, abstract):
    """Generate up to 3 tags based on title and abstract."""
    text = f"{title} {abstract}".lower()
    found_tags = []
    
    for tag, keywords in TAG_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                if tag not in found_tags:
                    found_tags.append(tag)
                break
        if len(found_tags) >= 3:
            break
    
    if not found_tags:
        found_tags = ['Academic', 'Research']
    
    return found_tags[:3]

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    # Look for the first --- and find the next ---
    if not content.startswith('---'):
        return {}, content
    
    # Find the second --- separator
    first_sep = content.find('---')
    second_sep = content.find('---', first_sep + 3)
    
    if second_sep == -1:
        return {}, content
    
    yaml_content = content[first_sep + 3:second_sep].strip()
    body = content[second_sep + 3:].strip()
    
    try:
        frontmatter = yaml.safe_load(yaml_content)
        return frontmatter, body
    except:
        return {}, content

def build_new_frontmatter(old_fm, body):
    """Build new frontmatter from old one."""
    # Map publication type
    pub_type = old_fm.get('publication_types', ['2'])
    if isinstance(pub_type, list):
        pub_type = pub_type[0] if pub_type else '2'
    pub_type = str(pub_type).strip("'\"")
    new_pub_type = TYPE_MAP.get(pub_type, 'article-journal')
    
    # Get authors and replace admin with me
    authors = old_fm.get('authors', ['admin'])
    if not isinstance(authors, list):
        authors = [authors]
    authors = [('me' if auth == 'admin' else auth) for auth in authors]
    
    # Extract abstract
    abstract = old_fm.get('abstract', '')
    if isinstance(abstract, str):
        abstract = abstract.strip()
    else:
        abstract = ''
    
    # Extract/generate summary
    summary = extract_summary(abstract)
    
    # Auto-generate tags
    title = old_fm.get('title', '')
    tags = get_tags(title, abstract)
    
    # Extract DOI
    doi = old_fm.get('doI') or old_fm.get('doi') or old_fm.get('DOI') or ''
    if doi:
        # Clean up DOI format
        doi = str(doi).strip()
    
    # Build new frontmatter
    new_fm = {
        'title': title,
        'authors': authors,
        'author_notes': [''],
        'date': old_fm.get('date', datetime.now().isoformat() + 'Z'),
        'publishDate': old_fm.get('publishDate', datetime.now().isoformat() + 'Z'),
        'publication_types': [new_pub_type],
        'publication': old_fm.get('publication', ''),
        'publication_short': '',
        'abstract': abstract,
        'summary': summary,
        'tags': tags,
        'featured': False,
        'hugoblox': {
            'ids': {
                'arxiv': ''
            }
        },
        'links': [
            {'type': 'pdf', 'url': ''},
            {'type': 'code', 'url': ''},
            {'type': 'dataset', 'url': ''},
            {'type': 'poster', 'url': ''},
            {'type': 'project', 'url': ''},
            {'type': 'slides', 'url': ''},
            {'type': 'source', 'url': ''},
            {'type': 'video', 'url': ''},
        ],
        'image': {
            'caption': 'Image credit: [**Unsplash**](https://unsplash.com)',
            'focal_point': '',
            'preview_only': False
        },
        'projects': [],
        'slides': '',
        'draft': False
    }
    
    # Add DOI if present
    if doi:
        new_fm['doI'] = doi
    
    return new_fm



def update_publication(pub_path):
    """Update a single publication file."""
    index_file = pub_path / 'index.md'
    
    if not index_file.exists():
        return False, "index.md not found"
    
    try:
        # Read content
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse frontmatter and body
        old_fm, body = parse_frontmatter(content)
        
        if not old_fm:
            return False, "Could not parse frontmatter"
        
        # Build new frontmatter
        new_fm = build_new_frontmatter(old_fm, body)
        
        # Create new content with manual YAML formatting
        yaml_lines = []
        yaml_lines.append(f"title: {yaml.safe_dump(new_fm['title'], default_flow_style=False).strip()}")
        yaml_lines.append(f"authors:\n" + "\n".join([f"  - {auth}" for auth in new_fm['authors']]))
        yaml_lines.append(f"author_notes:\n  - \"\"")
        yaml_lines.append(f"date: {new_fm['date']}")
        yaml_lines.append(f"publishDate: {new_fm['publishDate']}")
        yaml_lines.append(f"publication_types: {yaml.safe_dump(new_fm['publication_types'], default_flow_style=True).strip()}")
        yaml_lines.append(f"publication: {yaml.safe_dump(new_fm['publication'], default_flow_style=False).strip()}")
        yaml_lines.append(f"publication_short: \"\"")
        
        abstract_str = new_fm['abstract'].replace('\n', '\n  ') if new_fm['abstract'] else ''
        if abstract_str:
            yaml_lines.append(f"abstract: |\n  {abstract_str}")
        else:
            yaml_lines.append("abstract: \"\"")
        
        yaml_lines.append(f"summary: {yaml.safe_dump(new_fm['summary'], default_flow_style=False).strip()}")
        yaml_lines.append(f"tags:\n" + "\n".join([f"  - {tag}" for tag in new_fm['tags']]))
        yaml_lines.append(f"featured: false")
        
        if 'doI' in new_fm and new_fm['doI']:
            yaml_lines.append(f"doI: {yaml.safe_dump(new_fm['doI'], default_flow_style=False).strip()}")
        
        yaml_lines.append("hugoblox:")
        yaml_lines.append("  ids:")
        yaml_lines.append("    arxiv: \"\"")
        yaml_lines.append("links:")
        for link in new_fm['links']:
            yaml_lines.append(f"  - type: {link['type']}")
            yaml_lines.append(f"    url: \"\"")
        yaml_lines.append("image:")
        yaml_lines.append("  caption: 'Image credit: [**Unsplash**](https://unsplash.com)'")
        yaml_lines.append("  focal_point: \"\"")
        yaml_lines.append("  preview_only: false")
        yaml_lines.append("projects: []")
        yaml_lines.append("slides: \"\"")
        yaml_lines.append("draft: false")
        
        yaml_content = "\n".join(yaml_lines)
        
        # Preserve body (citation text or abstract)
        if body.strip():
            new_content = f"---\n{yaml_content}---\n\n{body}\n"
        else:
            new_content = f"---\n{yaml_content}---\n\n"
        
        # Write back
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"Updated: {new_fm['title'][:50]}"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to update all publications."""
    pub_base = Path('content/publications')
    
    if not pub_base.exists():
        print(f"Error: {pub_base} not found")
        return
    
    # Get all publication directories (exclude example-publication)
    pub_dirs = sorted([
        d for d in pub_base.iterdir() 
        if d.is_dir() and d.name != 'example-publication'
    ])
    
    print(f"Found {len(pub_dirs)} publications to update\n")
    print("=" * 80)
    
    success_count = 0
    error_count = 0
    errors = []
    
    for i, pub_dir in enumerate(pub_dirs, 1):
        success, message = update_publication(pub_dir)
        status = "OK" if success else "FAIL"
        print(f"{i:2d}. {status} {pub_dir.name}")
        print(f"    {message}")
        
        if success:
            success_count += 1
        else:
            error_count += 1
            errors.append((pub_dir.name, message))
    
    print("=" * 80)
    print(f"\nResults: {success_count} successful, {error_count} failed")
    
    if errors:
        print("\nErrors:")
        for pub_name, error in errors:
            print(f"  - {pub_name}: {error}")

if __name__ == '__main__':
    main()
