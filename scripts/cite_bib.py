#!/usr/bin/env python3
"""Create and check cite.bib files for the publications in the dj_hugo site.

    python scripts/cite_bib.py                preview: which publications have no cite.bib, and what would be written
    python scripts/cite_bib.py --write        create the missing cite.bib files (never overwrites an existing one)
    python scripts/cite_bib.py --check        check existing cite.bib files against each publication's front matter
    python scripts/cite_bib.py --write --force   also replace existing files (only with a path filter, see below)
    pnpm run cite / cite:write / cite:check   same, via package.json

Any extra words are path filters: `--check jakniunaite2015` only looks at folders whose name contains that text.

The front matter is the source. A generated file is a draft: it cannot know details the front matter
does not hold (editors of a chapter are taken from the formatted citation in the page body when it
says "edited by ..."; otherwise the script says so). Read each new file once before you rely on it.
Reports only on --check: exit code 1 if an ERROR is found. Needs PyYAML.
"""
import glob
import os
import re
import sys
import unicodedata

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is missing: pip install pyyaml")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
TREES = [("lt", "publikacijos"), ("en", "publications")]

# publication_types value -> BibTeX entry type
BIB_TYPE = {
    "article-journal": "article",
    "review": "article",
    "report": "techreport",
    "book": "book",
    "edited-book": "book",
    "chapter": "incollection",
}
REQUIRED = {
    "article": ["title", "year", "journal"],
    "book": ["title", "year", "publisher"],
    "incollection": ["title", "year", "booktitle", "publisher"],
    "techreport": ["title", "year"],
}
STOP = {"the", "a", "an", "of", "on", "in", "and", "for", "to", "kaip", "ir", "apie", "is", "i"}
PARTICLES = {"van", "von", "de", "der", "den", "di", "da", "del", "la", "le", "du", "ter", "ten"}


# ---------- helpers ----------

def ascii_fold(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()


def norm(s):
    return re.sub(r"[^a-z0-9]", "", ascii_fold(s).lower())


def load_fm(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        return None, ""
    try:
        _, fm, body = text.split("---", 2)
        return yaml.safe_load(fm) or {}, body
    except (ValueError, yaml.YAMLError):
        return None, ""


def my_name():
    """'Jakniūnaitė, Dovilė' from data/authors/me.yaml."""
    try:
        d = yaml.safe_load(open(os.path.join(ROOT, "data", "authors", "me.yaml"), encoding="utf-8"))
        full = d["name"]["display"]
    except Exception:
        full = "Dovilė Jakniūnaitė"
    return to_bib_name(full)


def to_bib_name(full):
    """'Terry D. Clark' -> 'Clark, Terry D.'; keeps 'van der X' particles with the surname."""
    full = " ".join(str(full).split())
    if "," in full:
        return full
    parts = full.split(" ")
    if len(parts) == 1:
        return full
    i = len(parts) - 1
    while i > 1 and parts[i - 1].lower() in PARTICLES:
        i -= 1
    return f"{' '.join(parts[i:])}, {' '.join(parts[:i])}"


def surname(bib_name):
    return norm(bib_name.split(",")[0])


def split_people(s):
    return [p.strip() for p in re.split(r"\s+and\s+", s) if p.strip()]


def esc(v):
    """Escape characters BibTeX treats specially. Unicode letters stay as they are."""
    v = str(v)
    v = re.sub(r"(?<!\\)([&%$#_])", r"\\\1", v)
    return v


def pages(v):
    v = str(v or "").strip()
    return re.sub(r"\s*[-–—]+\s*", "--", v) if v else ""


def make_key(authors, year, title):
    first = surname(authors[0]) if authors else "anon"
    words = [w for w in re.findall(r"[^\W_]+", ascii_fold(title)) if w.lower() not in STOP][:3]
    return f"{first}{year}{''.join(w.capitalize() for w in words)}"


def editors_from_body(body):
    """Editors named in the formatted citation under the front matter ('edited by A, B, and C, 93-138')."""
    m = re.search(r"(?:edited by|sud\.|red\.)\s+(.+?)(?:,\s*\d|\.\s|\.$|$)", body.strip().splitlines()[0] if body.strip() else "")
    if not m:
        m = re.search(r"(?:edited by|sud\.|red\.)\s+(.+?)(?:,\s*\d|\.\s|\.$|$)", body)
    if not m:
        return []
    names = re.split(r",\s*(?:and\s+)?|\s+and\s+|\s+ir\s+", m.group(1))
    return [to_bib_name(n) for n in names if n.strip()]


def front_authors(fm, me):
    out = []
    for a in fm.get("authors") or []:
        out.append(me if str(a) in ("me", "admin") else to_bib_name(a))
    return out


# ---------- generate ----------

def build_entry(path):
    """Return (bib_text, notes) for one publication folder, from its index.md."""
    fm, body = load_fm(path)
    notes = []
    if fm is None:
        return None, ["index.md has no readable front matter"]
    types = fm.get("publication_types") or []
    ptype = str(types[0]) if types else ""
    if ptype not in BIB_TYPE:
        return None, [f"unknown publication_types {types!r}"]
    btype = BIB_TYPE[ptype]
    pub = fm.get("publication") or {}
    me = my_name()
    people = front_authors(fm, me)
    title = str(fm.get("title") or "").strip()
    year = str(fm.get("date") or "")[:4]
    f = {}
    if ptype == "edited-book":
        f["editor"] = " and ".join(people)
    else:
        f["author"] = " and ".join(people)
    f["title"] = title
    f["year"] = year
    name = str(pub.get("name") or "").strip()
    publisher = str(pub.get("publisher") or "").strip()
    if btype == "article":
        f["journal"] = name
        if pub.get("volume"):
            f["volume"] = str(pub["volume"])
        if pub.get("issue"):
            f["number"] = str(pub["issue"])
        if publisher:
            f["publisher"] = publisher
    elif btype == "book":
        f["publisher"] = publisher or name
    elif btype == "incollection":
        f["booktitle"] = name
        f["publisher"] = publisher
        eds = editors_from_body(body)
        if eds:
            f["editor"] = " and ".join(eds)
        else:
            notes.append("chapter: editors not found in the page body, add `editor` by hand")
    if pub.get("pages"):
        f["pages"] = pages(pub["pages"])
    ids = ((fm.get("hugoblox") or {}).get("ids")) or {}
    if ids.get("doi"):
        f["doi"] = str(ids["doi"]).strip()
    if ids.get("isbn"):
        f["isbn"] = str(ids["isbn"]).strip()
    if re.search(r"[ąčęėįšųūžĄČĘĖĮŠŲŪŽ]", title):
        f["langid"] = "lithuanian"
    for k in REQUIRED[btype]:
        if not f.get(k):
            notes.append(f"`{k}` is empty in the front matter, so the entry has no `{k}`")
    f = {k: v for k, v in f.items() if v}
    if ptype == "edited-book" and not f.get("editor"):
        notes.append("edited-book has no authors to use as editors")
    key = make_key(people, year, title)
    lines = [f"@{btype}{{{key},"]
    for k in sorted(f):
        lines.append(f" {k} = {{{esc(f[k]) if k not in ('doi',) else f[k]}}},")
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}")
    return "\n".join(lines) + "\n", notes


# ---------- parse and check ----------

def parse_bib(text):
    """Return (entries, problems). entries: list of (type, key, {field: value})."""
    entries, problems = [], []
    pos = 0
    pat = re.compile(r"@(\w+)\s*\{\s*([^,\s]*)\s*,")
    while True:
        m = pat.search(text, pos)
        if not m:
            break
        depth, i = 1, m.end()
        while i < len(text) and depth:
            c = text[i]
            if c == "\\":
                i += 2
                continue
            depth += (c == "{") - (c == "}")
            i += 1
        if depth:
            problems.append(f"entry {m.group(2)!r}: braces are not balanced")
            break
        entries.append((m.group(1).lower(), m.group(2), parse_fields(text[m.end():i - 1])))
        pos = i
    if not entries and not problems:
        problems.append("no BibTeX entry found")
    return entries, problems


def parse_fields(body):
    fields = {}
    for m in re.finditer(r"(\w+)\s*=\s*", body):
        i = m.end()
        if i >= len(body):
            continue
        if body[i] == "{":
            depth, j = 1, i + 1
            while j < len(body) and depth:
                c = body[j]
                if c == "\\":
                    j += 2
                    continue
                depth += (c == "{") - (c == "}")
                j += 1
            val = body[i + 1:j - 1]
        elif body[i] == '"':
            j = body.find('"', i + 1)
            val = body[i + 1:j]
        else:
            j = re.compile(r"[,\s}]").search(body, i)
            val = body[i:j.start() if j else len(body)]
        fields.setdefault(m.group(1).lower(), re.sub(r"\s+", " ", val).strip())
    return fields


def odd_chars(s):
    bad = set()
    for ch in s:
        if ch.isalpha() and ord(ch) > 0x17F and not (0x0400 <= ord(ch) <= 0x04FF):
            bad.add(ch)
        if ch in "\ufffd":
            bad.add(ch)
    return sorted(bad)


def check_one(folder, findings, keys_seen):
    path = os.path.join(folder, "cite.bib")
    name = os.path.relpath(path, ROOT).replace("\\", "/")
    text = open(path, encoding="utf-8", errors="replace").read()

    def add(level, msg):
        findings.append((level, name, msg))

    entries, problems = parse_bib(text)
    for p in problems:
        add("ERROR", p)
    if not entries:
        return
    if len(entries) > 1:
        add("WARN", f"{len(entries)} entries in one file; the site's Cite link expects one")
    btype, key, f = entries[0]
    tree = os.path.relpath(folder, CONTENT).split(os.sep)[0]
    if (tree, key) in keys_seen and keys_seen[(tree, key)] != folder:
        add("ERROR", f"citation key {key!r} is also used in {os.path.basename(keys_seen[(tree, key)])}")
    keys_seen[(tree, key)] = folder

    if "\ufffd" in text or re.search(r"Ã.|Â.|â€", text):
        add("ERROR", "text contains broken characters (mojibake) from a wrong encoding")
    for k, v in f.items():
        if re.search(r"\\[.'`^\"~=][a-zA-Z]?|``|''", v):
            add("WARN", f"`{k}` has LaTeX accent or quote escapes ({v[:50]!r}...), probably a bad export")
        bad = odd_chars(v)
        if bad:
            add("WARN", f"`{k}` has unusual letters {''.join(bad)} (possible damaged text)")

    for k in REQUIRED.get(btype, ["title", "year"]):
        if not f.get(k):
            add("ERROR" if k in ("title", "year") else "WARN", f"@{btype} lacks `{k}`")
    if not (f.get("author") or f.get("editor")):
        add("ERROR", "neither `author` nor `editor`")
    if "pages" in f and not re.fullmatch(r"[\w.]+(--[\w.]+)?", f["pages"].replace(" ", "")):
        add("WARN", f"pages {f['pages']!r}: use `from--to` (two hyphens)")
    if "pages" in f and re.search(r"(?<!-)[-–—](?!-)", f["pages"]):
        add("WARN", f"pages {f['pages']!r}: a range needs `--`")

    # compare with the publication's front matter
    index = os.path.join(folder, "index.md")
    fm, body = load_fm(index) if os.path.exists(index) else (None, "")
    if fm is None:
        add("WARN", "no readable index.md to compare with")
        return
    ptype = str((fm.get("publication_types") or [""])[0])
    if ptype in BIB_TYPE and BIB_TYPE[ptype] != btype:
        add("WARN", f"publication_types is {ptype!r}, which should be @{BIB_TYPE[ptype]}, file has @{btype}")
    if ptype == "edited-book" and not f.get("editor"):
        add("ERROR", "edited-book must list its people as `editor`, not `author`")
    year = str(fm.get("date") or "")[:4]
    if f.get("year") and year and f["year"] != year:
        add("WARN", f"year {f['year']} differs from front matter date {year}")
    if f.get("title") and norm(f["title"]) != norm(str(fm.get("title") or "")):
        add("WARN", f"title differs from front matter: {f['title'][:60]!r} vs {str(fm.get('title'))[:60]!r}")
    doi = str((((fm.get("hugoblox") or {}).get("ids")) or {}).get("doi") or "").strip()
    bdoi = re.sub(r"^https?://(dx\.)?doi\.org/", "", f.get("doi", ""))
    if doi and bdoi and doi.lower() != bdoi.lower():
        add("WARN", f"DOI differs: file {bdoi} vs front matter {doi}")
    if doi and not bdoi:
        add("WARN", "front matter has a DOI but the file has none")
    people = f.get("editor") if ptype == "edited-book" else f.get("author")
    if people is not None:
        want = [surname(p) for p in front_authors(fm, my_name())]
        have = [surname(to_bib_name(p)) for p in split_people(people)]
        if want and have and sorted(want) != sorted(have):
            add("WARN", f"people differ from front matter authors: file {have} vs front matter {want}")
    pub = fm.get("publication") or {}
    if f.get("pages") and pub.get("pages") and pages(pub["pages"]) != f["pages"]:
        add("WARN", f"pages {f['pages']} differ from front matter {pages(pub['pages'])}")


def check_twins(findings):
    lt = {os.path.basename(os.path.dirname(p)): p for p in glob.glob(os.path.join(CONTENT, "lt", "publikacijos", "*", "cite.bib"))}
    en = {os.path.basename(os.path.dirname(p)): p for p in glob.glob(os.path.join(CONTENT, "en", "publications", "*", "cite.bib"))}
    for name in sorted(set(lt) & set(en)):
        a = open(lt[name], encoding="utf-8", errors="replace").read().strip()
        b = open(en[name], encoding="utf-8", errors="replace").read().strip()
        if a != b:
            findings.append(("WARN", f"content/lt|en/.../{name}/cite.bib", "LT and EN cite.bib differ"))


# ---------- main ----------

def folders(filters):
    out = []
    for lang, sub in TREES:
        for d in sorted(glob.glob(os.path.join(CONTENT, lang, sub, "*"))):
            if os.path.isfile(os.path.join(d, "index.md")) and (not filters or any(f in os.path.basename(d) for f in filters)):
                out.append(d)
    return out


def main():
    args = sys.argv[1:]
    write, check, force = "--write" in args, "--check" in args, "--force" in args
    filters = [a for a in args if not a.startswith("--")]
    if force and not filters:
        sys.exit("--force replaces existing files; name the folder(s) too, e.g. --write --force jakniunaite2015")
    dirs = folders(filters)

    if check:
        findings, keys_seen = [], {}
        have = [d for d in dirs if os.path.exists(os.path.join(d, "cite.bib"))]
        for d in have:
            check_one(d, findings, keys_seen)
        if not filters:
            check_twins(findings)
        missing = [d for d in dirs if d not in have]
        errs = [x for x in findings if x[0] == "ERROR"]
        warns = [x for x in findings if x[0] == "WARN"]
        for title, items in (("Errors", errs), ("Warnings", warns)):
            if items:
                print(f"{title}:")
                last = None
                for _, p, m in sorted(items, key=lambda x: (x[1], x[2])):
                    if p != last:
                        print(p)
                        last = p
                    print(f"  {'ERROR' if title == 'Errors' else 'WARN '} {m}")
                print()
        if missing:
            print(f"{len(missing)} publication(s) have no cite.bib (run without --check to preview, --write to create):")
            for d in missing:
                print("  " + os.path.relpath(d, CONTENT).replace("\\", "/"))
        print(f"\nChecked {len(have)} cite.bib file(s): {len(errs)} error(s), {len(warns)} warning(s).")
        sys.exit(1 if errs else 0)

    made = 0
    for d in dirs:
        target = os.path.join(d, "cite.bib")
        exists = os.path.exists(target)
        if exists and not force:
            continue
        text, notes = build_entry(os.path.join(d, "index.md"))
        rel = os.path.relpath(target, CONTENT).replace("\\", "/")
        if text is None:
            print(f"SKIP  {rel}: {'; '.join(notes)}")
            continue
        print(f"{'WRITE' if write else 'WOULD WRITE'}  {rel}")
        for n in notes:
            print(f"      note: {n}")
        if write:
            with open(target, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            made += 1
        else:
            print("      " + text.replace("\n", "\n      ").rstrip())
    if not write:
        print("\nPreview only. Run with --write to create these files.")
    else:
        print(f"\nCreated {made} file(s). Read each one once, then run with --check.")


if __name__ == "__main__":
    main()
