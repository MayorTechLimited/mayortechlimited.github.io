import os
import sys
from pathlib import Path

import markdown
from staticjinja import Site

markdowner = markdown.Markdown(output_format="html5", extensions=["smarty", "meta"])


def post_get_created(template):
    created = template.name.replace("posts/", "").split("-", 3)
    return "-".join(created[:3])


def post_index_context(template):
    posts = []
    dir = site.searchpath / Path("posts")
    for f in dir.iterdir():
        if f.suffix == ".md" and not f.stem.startswith("_"):
            name = f.stem
            with f.open("r") as fd:
                for line in fd.readlines():
                    if line.startswith("# "):
                        name = line.replace("# ", "")
                        break
            posts.append({"stem": f.stem, "name": name, "created": post_get_created(f)})
    posts.sort(key=lambda p: p["stem"], reverse=True)
    return {"posts": posts}


def post_md_context(template):
    markdown_content = Path(template.filename).read_text()
    return {
        "content": markdowner.convert(markdown_content),
        "created": post_get_created(template),
        "description": "\n".join(markdowner.Meta["description"]),
    }


def post_render_md(site, template, **kwargs):
    out = Path(site.outpath) / "posts" / Path(template.name).stem / "index.html"
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("_post.html").stream(**kwargs).dump(str(out), encoding="utf-8")


def project_index_context(template):
    projects = []
    dir = site.searchpath / Path("projects")
    for f in dir.iterdir():
        if f.suffix == ".md" and not f.stem.startswith("_"):
            markdown_content = f.read_text()
            markdowner.convert(markdown_content)
            meta = markdowner.Meta
            projects.append(
                {
                    "stem": f.stem,
                    "title": meta["title"][0],
                    "description": "\n".join(meta["description"]),
                    "link": meta["link"][0] if meta.get("link") else None,
                    "logo": meta.get("logo", [None])[0],
                    "screenshot": meta.get("screenshot", [None])[0],
                }
            )
    projects.sort(key=lambda p: p["title"].lower())
    return {"projects": projects}


def project_render_md(site, template, **kwargs):
    out = Path(site.outpath) / "projects" / Path(template.name).stem / "index.html"
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("projects/_project.html").stream(**kwargs).dump(
        str(out), encoding="utf-8"
    )


def project_md_context(template):
    markdown_content = Path(template.filename).read_text()
    desc = markdowner.convert(markdown_content)
    meta = markdowner.Meta
    return {
        "title": meta["title"][0],
        "description": desc,
        "link": meta["link"][0] if meta.get("link") else None,
        "logo": meta.get("logo", [None])[0],
        "screenshot": meta.get("screenshot", [None])[0],
    }


def work_index_context(template):
    work = []
    dir = site.searchpath / Path("work")
    for f in dir.iterdir():
        if f.suffix == ".md" and not f.stem.startswith("_"):
            markdown_content = f.read_text()
            markdowner.convert(markdown_content)
            meta = markdowner.Meta
            work.append(
                {
                    "stem": f.stem,
                    "title": meta["title"][0],
                    "description": "\n".join(meta["description"]),
                    "link": meta["link"][0] if meta.get("link") else None,
                    "logo": meta.get("logo", [None])[0],
                    "screenshot": meta.get("screenshot", [None])[0],
                }
            )
    work.sort(key=lambda p: p["title"].lower())
    return {"work": work}


def work_render_md(site, template, **kwargs):
    out = Path(site.outpath) / "work" / Path(template.name).stem / "index.html"
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("work/_work.html").stream(**kwargs).dump(
        str(out), encoding="utf-8"
    )


def work_md_context(template):
    markdown_content = Path(template.filename).read_text()
    desc = markdowner.convert(markdown_content)
    meta = markdowner.Meta
    return {
        "title": meta["title"][0],
        "description": desc,
        "link": meta["link"][0] if meta.get("link") else None,
        "logo": meta.get("logo", [None])[0],
        "screenshot": meta.get("screenshot", [None])[0],
    }


site = Site.make_site(
    searchpath="src",
    outpath="dist",
    contexts=[
        (r"posts/.*\.md", post_md_context),
        (r"projects/.*\.md", project_md_context),
        (r"work/.*\.md", work_md_context),
        ("posts/index.html", post_index_context),
        ("projects/index.html", project_index_context),
        ("work/index.html", work_index_context),
    ],
    rules=[
        (r"posts/.*\.md", post_render_md),
        (r"projects/.*\.md", project_render_md),
        (r"work/.*\.md", work_render_md),
    ],
)

if __name__ == "__main__":
    site.render(use_reloader="--watch" in sys.argv)
