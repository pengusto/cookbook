#!/usr/bin/env python3
"""Build and check the skill package and its project-path static site."""
import argparse
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "will-they-sue-me"
DIST = ROOT / "dist"


def skill_files():
    return [ROOT / "SKILL.md", ROOT / "LICENSE", *sorted((ROOT / "agents").rglob("*.yaml")), *sorted((ROOT / "references").rglob("*.md"))]


def write_copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def build():
    # These three directories are disposable outputs owned by this build only.
    for name in ("site", "skill", "preview"):
        target = DIST / name
        if target.exists():
            shutil.rmtree(target)
    site = DIST / "site"
    shutil.copytree(ROOT / "site", site)
    for source in skill_files():
        write_copy(source, DIST / "skill" / source.relative_to(ROOT))
        write_copy(source, site / "docs" / source.relative_to(ROOT))
    for source in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
        target = site / "docs" / source.relative_to(ROOT)
        write_copy(source, target)
        text = target.read_text()
        text = re.sub(r"\((?:\.\./)*\.github/workflows/check\.yml\)", "(https://github.com/pengusto/will-they-sue-me/actions/workflows/check.yml)", text)
        target.write_text(text)
    archive = site / "downloads" / f"{NAME}.zip"
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
        for source in skill_files():
            entry = zipfile.ZipInfo(f"{NAME}/{source.relative_to(ROOT).as_posix()}", date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            package.writestr(entry, source.read_bytes())
    (site / "downloads" / "SHA256SUMS").write_text(f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}\n")
    (site / ".nojekyll").touch()
    shutil.copytree(site, DIST / "preview" / NAME)
    return archive


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        for name in ("href", "src"):
            if name in attrs:
                self.links.append(attrs[name])


def check_links(base, source_only=False):
    for source in sorted(base.rglob("*")):
        if source.suffix not in (".html", ".md"):
            continue
        if source_only and (source.suffix != ".md" or source.relative_to(base).parts[0] in ("dist", "site", ".git", ".scratch")):
            continue
        text = source.read_text()
        links = Document(text).links if source.suffix == ".html" else re.findall(r"\]\(([^\s)]+)\)", text)
        for link in links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            assert not parts.path.startswith("/"), f"Root-relative link breaks project path: {source}: {link}"
            target = (source.parent / unquote(parts.path)).resolve() if parts.path else source.resolve()
            assert target.is_relative_to(base.resolve()), f"Link leaves artifact: {source}: {link}"
            if target.is_dir():
                target /= "index.html"
            assert target.is_file(), f"Broken link: {source}: {link}"
            if parts.fragment and target.suffix == ".html":
                assert unquote(parts.fragment) in Document(target.read_text()).ids, f"Missing anchor: {source}: {link}"


def check():
    text = (ROOT / "SKILL.md").read_text()
    front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    assert front, "Missing skill frontmatter"
    fields = dict(line.split(": ", 1) for line in front[1].splitlines())
    assert fields.get("name") == NAME and fields.get("description"), "Invalid skill metadata"
    assert "$" + NAME in (ROOT / "agents/openai.yaml").read_text(), "Prompt does not invoke skill"
    check_links(ROOT, source_only=True)
    archive = build()
    with zipfile.ZipFile(archive) as package:
        expected = {f"{NAME}/{p.relative_to(ROOT).as_posix()}": p.read_bytes() for p in skill_files()}
        assert set(package.namelist()) == set(expected), "Unexpected package content"
        assert package.testzip() is None, "Archive integrity failed"
        for name, data in expected.items():
            assert package.read(name) == data, f"Package drift: {name}"
    check_links(DIST / "site")
    for source in (DIST / "site").rglob("*"):
        if source.is_file():
            assert source.read_bytes() == (DIST / "preview" / NAME / source.relative_to(DIST / "site")).read_bytes(), "Preview drift"
    first_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
    assert hashlib.sha256(build().read_bytes()).hexdigest() == first_hash, "Package is not reproducible"
    print(f"PASS: metadata, source/artifact links, package contents/integrity, project-path preview, reproducible ZIP ({first_hash[:12]})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "check"))
    args = parser.parse_args()
    if args.command == "check":
        check()
    else:
        print(f"Built {build().relative_to(ROOT)} and dist/preview/{NAME}/")
