import shutil
import os
import sys
from pathlib import Path

import markdown

from staticjinja import Site

markdowner = markdown.Markdown(output_format="html5", extensions=["smarty", "meta"])


def get_created(template):
    created = template.name.replace("posts/", "").split("-", 3)
    return "-".join(created[:3])


def post_index_context(template):
    posts = []
    dir = site.searchpath / Path("posts")
    for f in dir.iterdir():
        if f.suffix == ".md":
            name = f.stem
            with f.open("r") as fd:
                for line in fd.readlines():
                    if line.startswith("# "):
                        name = line.replace("# ", "")
                        break
            posts.append({"stem": f.stem, "name": name, "created": get_created(f)})
    posts.sort(key=lambda p: p["stem"], reverse=True)
    return {"posts": posts}


def md_context(template):
    markdown_content = Path(template.filename).read_text()
    return {
        "content": markdowner.convert(markdown_content),
        "created": get_created(template),
        "description": "\n".join(markdowner.Meta["description"]),
    }


def render_md(site, template, **kwargs):
    out = Path(site.outpath) / "posts" / Path(template.name).stem / "index.html"
    os.makedirs(out.parent, exist_ok=True)
    site.get_template("_post.html").stream(**kwargs).dump(str(out), encoding="utf-8")


def copy_static():
    src = Path(".") / "static"
    src.mkdir(exist_ok=True, parents=True)
    dest = Path(".") / "dist"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


site = Site.make_site(
    searchpath="src",
    outpath="dist",
    contexts=[
        (r".*\.md", md_context),
        ("posts/index.html", post_index_context),
    ],
    rules=[
        (r".*\.md", render_md),
    ],
)

if __name__ == "__main__":
    copy_static()
    site.render(use_reloader="--watch" in sys.argv)
