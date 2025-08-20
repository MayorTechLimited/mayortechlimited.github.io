---
description: How to set up Zed to autoformat markdown files that are using frontmatter/metadata
---

# Autoformatting markdown files that have frontmatter in Zed

I write the posts on this blog in Markdown, using the
[python markdown library](https://github.com/Python-Markdown/markdown) to render them to
HTML. The library has some nice extra features that extend the markdown syntax, one that
I'm using is the
[frontmatter extension](https://python-markdown.github.io/extensions/meta_data/) that
lets me add metadata to the top of the markdown file, something like this:

```markdown
---
description: How to set up Zed to autoformat markdown files that are using frontmatter/metadata
---

# Autoformatting markdown files that have frontmatter in Zed

I write the posts on this blog in Markdown, using the python markdown library to render...
```

I wanted [Zed (my text editor)](https://zed.dev/) to auto format the markdown files when
I hit save. Mostly I wanted it to wrap the text so that each line didn't go over 88
characters. This is the standard line length in Python code and I've become used to
reading things that width. When lines get longer they often have to either soft wrap or
scroll and that can be annoying. I'd much rather have the computer format the lines to a
readable 88 characters.

Zed uses [prettier](https://prettier.io/) by default to format markdown files, and you
can turn on autoformatting on save by changing the Zed settings:

```json
{
    "languages": {
        "Markdown": {
            "format_on_save": "on"
        }
    }
}
```

The problem is that prettier doesn't like the frontmatter and squishes it all up onto a
single line.

I poked around in the prettier documentation for a while, looking for solutions. The
most obvious one was to get the formatter to ignore the frontmatter entirely and only
format the actual markdown parts of the file. I tried adding some ignore blocks to get
prettier to not format the frontmatter:

```markdown
<!-- prettier-ignore-start -->
---
description: How to set up Zed to autoformat markdown files that are using frontmatter/metadata
---
<!-- prettier-ignore-end -->
```

This worked, in that prettier no longer mangled the frontmatter, the problem was that
the python markdown library no longer recognised the frontmatter because it expects the
metadata part of the file to start on the first line, but I'd now added a comment there
instead.

I couldn't get the python markdown library and prettier to play nicely together. So, I
decided to switch formatters. I found a python based formatter called
[mdformat](https://github.com/hukkin/mdformat) that comes with plugins that extended the
formatter to understand the extra syntax I was using.

Installing it was as simple as this:

```bash
$ pipx install mdformat
$ pipx inject mdformat mdformat-frontmatter
```

I used the `pipx inject` command to add a bunch of plugins that I thought would be
useful. The list of available plugins is on the
[mdformat GitHub topic](https://github.com/topics/mdformat).

Then I only had to update my Zed config to use the new formatter:

```json
{
    "languages": {
        "Markdown": {
            "format_on_save": "on",
            "formatter": {
                "external": {
                    "command": "mdformat",
                    "arguments": ["--wrap", "88", "-"]
                }
            }
        }
    }
}
```

Now, whenever I save a markdown file when editing my blog, the file gets autoformatted.
