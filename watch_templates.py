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
            desc = markdowner.convert(markdown_content)
            projects.append(
                {
                    "title": markdowner.Meta["title"][0],
                    "description": desc,
                    "link": markdowner.Meta["link"][0],
                    "logo": markdowner.Meta.get("logo", [None])[0],
                    "screenshot": markdowner.Meta.get("screenshot", [None])[0],
                }
            )
    projects.sort(key=lambda p: p["title"])
    return {"projects": projects}


site = Site.make_site(
    searchpath="src",
    outpath="dist",
    contexts=[
        (r"posts/.*\.md", post_md_context),
        ("posts/index.html", post_index_context),
        ("projects/index.html", project_index_context),
    ],
    rules=[
        (r"posts/.*\.md", post_render_md),
    ],
)

if __name__ == "__main__":
    site.render(use_reloader="--watch" in sys.argv)
