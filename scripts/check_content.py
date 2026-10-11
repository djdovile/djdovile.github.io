#!/usr/bin/env python3
"""Pre-push consistency check for the dj_hugo site. Reads content, changes nothing.

    python scripts/check_content.py            front matter and content rules (fast)
    python scripts/check_content.py --build    also build into a temp folder and check the output
    pnpm run check / pnpm run check:build      same, via package.json

Exit code 1 if any ERROR is found; WARN lines are advice only.
Needs PyYAML (pip install pyyaml). The --build part needs hugo on PATH.
"""
import datetime
import glob
import html.parser
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
from collections import defaultdict

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is missing: pip install pyyaml")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")

PROJECT_STATUS = {"Vykdomas", "Įgyvendintas"}
COURSE_STATUS = {"Dėstomas", "Dėstytas"}
PUB_TYPES = {"article-journal", "chapter", "book", "edited-book", "review", "report"}
FORBIDDEN_KEYS = {"permalink", "tech_stack"}

findings = []  # (level, path, message)


def rel(p):
    return os.path.relpath(p, ROOT).replace("\\", "/")


def add(level, path, msg):
    findings.append((level, rel(path) if os.path.isabs(path) else path, msg))


def load(path):
    """Return front matter dict, or None (and report) if unreadable."""
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        add("ERROR", path, "no YAML front matter (file must start with ---)")
        return None
    try:
        fm = yaml.safe_load(text.split("---", 2)[1]) or {}
    except yaml.YAMLError as e:
        add("ERROR", path, f"front matter is not valid YAML: {str(e).splitlines()[0]}")
        return None
    if not isinstance(fm, dict):
        add("ERROR", path, "front matter is not a key: value block")
        return None
    return fm


def blank(v):
    return v is None or (isinstance(v, str) and not v.strip()) or v == []


def as_datetime(v):
    if isinstance(v, datetime.datetime):
        return v if v.tzinfo else v.replace(tzinfo=datetime.timezone.utc)
    if isinstance(v, datetime.date):
        return datetime.datetime(v.year, v.month, v.day, tzinfo=datetime.timezone.utc)
    if isinstance(v, str):
        try:
            d = datetime.datetime.fromisoformat(v.strip())
            return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)
        except ValueError:
            return None
    return None


def require(path, fm, keys):
    for k in keys:
        if blank(fm.get(k)):
            add("ERROR", path, f"missing or empty `{k}`")


def check_dates(path, fm, keys=("date", "publishDate")):
    now = datetime.datetime.now(datetime.timezone.utc)
    for k in keys:
        if k in fm and not blank(fm[k]):
            d = as_datetime(fm[k])
            if d is None:
                add("ERROR", path, f"`{k}` is not a valid date: {fm[k]!r}")
            elif d > now and not fm.get("draft"):
                add("ERROR", path, f"`{k}` is in the future ({fm[k]}); Hugo will silently not publish this page")


def bundles(section):
    return sorted(glob.glob(os.path.join(CONTENT, section, "*", "index.md")))


# ---------------------------------------------------------------- per type


def check_project(path, fm):
    require(path, fm, ["title", "summary", "date", "tags", "status"])
    check_dates(path, fm)
    status = fm.get("status")
    tags = fm.get("tags") or []
    if status not in PROJECT_STATUS:
        add("ERROR", path, f"`status` is {status!r}, expected one of {sorted(PROJECT_STATUS)}")
    topic = [t for t in tags if t not in ("projektas", "vykdomi", "igyvendinti")]
    if not topic:
        add("WARN", path, "no topic tags")
    if fm.get("reading_time") is not False:
        add("WARN", path, "`reading_time: false` not set")
    if fm.get("profile") is not False:
        add("WARN", path, "`profile: false` not set")


def check_course(path, fm):
    require(path, fm, ["title", "summary", "date", "tags", "status"])
    check_dates(path, fm)
    tags = fm.get("tags") or []
    status = fm.get("status")
    if status not in COURSE_STATUS:
        add("ERROR", path, f"`status` is {status!r}, expected one of {sorted(COURSE_STATUS)} (exact case)")
    if fm.get("reading_time") is not False:
        add("WARN", path, "`reading_time: false` not set")
    if fm.get("profile") is not False:
        add("WARN", path, "`profile: false` not set")


def check_post(path, fm):
    require(path, fm, ["title", "date"])
    check_dates(path, fm)
    if not isinstance(fm.get("draft"), bool):
        add("ERROR", path, "`draft` must be true or false")
    elif fm["draft"]:
        add("WARN", path, "draft: true (will not be published)")
    if blank(fm.get("tags")):
        add("WARN", path, "no tags")
    authors = fm.get("authors") or []
    if not authors:
        add("WARN", path, "no `authors` (use `me`)")
    if "admin" in authors:
        add("WARN", path, "author is `admin`; use `me` or leave empty")
    if "lastmod" in fm and fm["lastmod"] is not None and as_datetime(fm["lastmod"]) is None:
        add("ERROR", path, f"`lastmod` is not a valid date: {fm['lastmod']!r}")


def check_publication(path, fm, slugs, check_projects=True):
    require(path, fm, ["title", "authors", "date", "publication_types", "publication", "tags"])
    check_dates(path, fm)
    types = fm.get("publication_types") or []
    if not isinstance(types, list) or len(types) != 1 or types[0] not in PUB_TYPES:
        add("ERROR", path, f"`publication_types` is {types!r}, expected exactly one of {sorted(PUB_TYPES)}")
    if "me" not in (fm.get("authors") or []):
        add("WARN", path, "`me` is not among the authors")
    pub = fm.get("publication")
    if isinstance(pub, dict) and blank(pub.get("name")) and not blank(pub.get("short_name")):
        add("WARN", path, "`publication.name` empty")
    ids = (fm.get("hugoblox") or {}).get("ids") or {}
    if isinstance(ids.get("doi"), list):
        add("ERROR", path, "`hugoblox.ids.doi` is a list; it must be one string (a list prints [brackets] in the link)")
    doi = ids.get("doi")
    if isinstance(doi, str) and re.match(r"https?://", doi):
        add("WARN", path, "DOI should be the bare identifier (10.xxxx/...), not a full URL")
    for pr in fm.get("projects") or []:
        if pr is None:
            add("ERROR", path, "`projects:` contains an empty entry (null)")
        elif check_projects and pr not in slugs:
            add("ERROR", path, f"`projects:` refers to {pr!r}, which is not a project folder in content/lt/projektai")
    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        add("ERROR", path, "`tags` must be a list")


# ---------------------------------------------------------------- cross-file


def check_all_pages():
    """Rules that apply to every page: forbidden keys, `#` tags, stray YAML keys."""
    for path in glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True):
        fm = load(path)
        if fm is None:
            continue
        for k in FORBIDDEN_KEYS & set(fm):
            add("ERROR", path, f"forbidden front matter `{k}` (retired; see CLAUDE.md)")
        tags = fm.get("tags")
        if isinstance(tags, list):
            for t in tags:
                if not isinstance(t, str) or not t.strip():
                    add("ERROR", path, f"bad tag {t!r}")
                elif t.startswith("#") or t != t.strip():
                    add("ERROR", path, f"tag {t!r} has a leading # or stray space")
        elif tags is not None:
            add("ERROR", path, "`tags` must be a list")


def check_tag_variants(all_fm):
    """Same tag written in several cases/spellings across the site (e.g. Rusija / rusija)."""
    seen = defaultdict(lambda: defaultdict(list))
    for path, fm in all_fm:
        for t in fm.get("tags") or []:
            if isinstance(t, str):
                seen[t.strip().lower()][t].append(path)
    for key, variants in seen.items():
        if len(variants) > 1:
            parts = ", ".join(f"{v!r} ×{len(p)}" for v, p in variants.items())
            add("WARN", "(tags)", f"tag written several ways: {parts}")


def check_mirror():
    lt = {os.path.basename(os.path.dirname(p)) for p in bundles("lt/publikacijos")}
    en = {os.path.basename(os.path.dirname(p)) for p in bundles("en/publications")}
    for s in sorted(lt - en):
        add("ERROR", f"content/lt/publikacijos/{s}", "no English twin in content/en/publications")
    for s in sorted(en - lt):
        add("ERROR", f"content/en/publications/{s}", "no Lithuanian twin in content/lt/publikacijos")
    for s in sorted(lt & en):
        a = load(os.path.join(CONTENT, "lt/publikacijos", s, "index.md"))
        b = load(os.path.join(CONTENT, "en/publications", s, "index.md"))
        if not a or not b:
            continue
        for k in ("publication_types", "date"):
            if str(a.get(k)) != str(b.get(k)):
                add("ERROR", f"content/lt/publikacijos/{s}", f"`{k}` differs between LT ({a.get(k)!r}) and EN ({b.get(k)!r})")
        for lang, fm in (("LT", a), ("EN", b)):
            if fm.get("draft") is True:
                add("WARN", f"content/lt/publikacijos/{s}", f"{lang} version is a draft awaiting review")
        da = ((a.get("hugoblox") or {}).get("ids") or {}).get("doi")
        db = ((b.get("hugoblox") or {}).get("ids") or {}).get("doi")
        if da != db:
            add("ERROR", f"content/lt/publikacijos/{s}", f"DOI differs between LT ({da!r}) and EN ({db!r})")


def check_front_matter():
    project_slugs = {os.path.basename(os.path.dirname(p)) for p in bundles("lt/projektai")}
    all_fm = []
    for section, fn in (("lt/projektai", check_project), ("lt/destymas", check_course), ("lt/blogas", check_post)):
        for path in bundles(section):
            fm = load(path)
            if fm is not None:
                fn(path, fm)
                all_fm.append((path, fm))
    for section in ("lt/publikacijos", "en/publications"):
        for path in bundles(section):
            fm = load(path)
            if fm is not None:
                # EN has no project pages yet, so `projects:` is only resolved for LT
                check_publication(path, fm, project_slugs, check_projects=section.startswith("lt/"))
                all_fm.append((path, fm))
    check_all_pages()
    check_tag_variants(all_fm)
    check_mirror()


# ---------------------------------------------------------------- build output


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.hrefs.append(a["href"])


def check_build():
    if not shutil.which("hugo"):
        add("ERROR", "(build)", "hugo not found on PATH; cannot run --build checks")
        return
    out = tempfile.mkdtemp(prefix="dj_hugo_check_")
    print(f"building into {out} ...", flush=True)
    r = subprocess.run(["hugo", "--minify", "-d", out], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        add("ERROR", "(build)", "hugo build failed: " + (r.stderr or r.stdout).strip().splitlines()[-1])
        return
    for line in (r.stdout + r.stderr).splitlines():
        if line.startswith("WARN"):
            add("WARN", "(build)", line[:200])
    base = urllib.parse.urlparse(open(os.path.join(ROOT, "config/_default/hugo.yaml"), encoding="utf-8").read().split("baseURL:")[1].split()[0].strip("'\""))
    base_path = base.path.rstrip("/")
    broken = defaultdict(set)
    google, doi_brackets = set(), set()
    for dirpath, _, files in os.walk(out):
        for f in files:
            full = os.path.join(dirpath, f)
            page = "/" + os.path.relpath(full, out).replace("\\", "/")
            if f.endswith((".html", ".css", ".xml")):
                text = open(full, encoding="utf-8", errors="replace").read()
                if re.search(r"fonts\.(googleapis|gstatic)\.com", text):
                    google.add(page)
            if not f.endswith(".html"):
                continue
            p = Links()
            p.feed(open(full, encoding="utf-8", errors="replace").read())
            for h in p.hrefs:
                if re.search(r"doi\.org/(\[|%5B)", h):
                    doi_brackets.add(page)
                u = urllib.parse.urlparse(h)
                if u.scheme or h.startswith(("//", "#", "mailto:", "tel:", "javascript:")) or not (u.path):
                    continue
                path = urllib.parse.unquote(u.path)
                if path.startswith("/"):
                    if base_path and path.startswith(base_path + "/"):
                        path = path[len(base_path):]
                    target = os.path.join(out, path.lstrip("/"))
                else:
                    target = os.path.normpath(os.path.join(dirpath, path))
                ok = os.path.isfile(target) or os.path.isfile(os.path.join(target, "index.html"))
                if not ok:
                    broken[h].add(page)
    for pg in sorted(google):
        add("ERROR", pg, "built page loads from Google Fonts (fonts must be self-hosted)")
    for pg in sorted(doi_brackets):
        add("ERROR", pg, "DOI link contains [brackets]")
    for h, pages in sorted(broken.items()):
        first = sorted(pages)[0]
        more = f" (+{len(pages) - 1} more pages)" if len(pages) > 1 else ""
        add("ERROR", first, f"broken internal link {h}{more}")
    shutil.rmtree(out, ignore_errors=True)


# ---------------------------------------------------------------- main


def main():
    check_front_matter()
    if "--build" in sys.argv:
        check_build()
    errors = [f for f in findings if f[0] == "ERROR"]
    warns = [f for f in findings if f[0] == "WARN"]
    by_path = defaultdict(list)
    for lvl, path, msg in errors:
        by_path[path].append(msg)
    for path in sorted(by_path):
        print(path)
        for msg in sorted(by_path[path]):
            print(f"  ERROR {msg}")
    if warns:
        print("\nWarnings (advice only):")
        grouped = defaultdict(list)
        for lvl, path, msg in warns:
            grouped[msg].append(path)
        for msg, paths in sorted(grouped.items(), key=lambda kv: -len(kv[1])):
            names = ", ".join(sorted(os.path.basename(os.path.dirname(p)) if p.endswith("index.md") else p for p in paths))
            print(f"  WARN  {msg} [{len(paths)}]" + (f": {names}" if len(paths) <= 6 else ""))
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s)")
    if not findings:
        print("all checks passed")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
