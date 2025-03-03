description: An explaination of how this website is built, maintained, and hosted.

# This Blog's Tech Stack

This feels like one of those trite blog posts that every software engineer writes, so I apologise if this post is dull. However, I wanted to get back into writing blog posts, something I've never been able to manage very well, and this seemed like an easy win.

So here goes...

## Hosting

It's hosted on GitHub Pages, for free! It's a static site, and I wanted it to be fast, always available, and hassle free. GitHub Pages is exactly that, so this was a bit of a no-brainer.

## Analytics

I use a privacy-first analytics tool called [Pirsch](https://pirsch.io), it doesn't set cookies or anything like that, it just tells me which pages people are visiting.

They have a useful system where you can create dashboards of data and share it with other people. For instance you can see all of the analytics data for my blog on the public dashboard: [https://mayortech.pirsch.io](https://mayortech.pirsch.io). As you can see, I don't get much traffic :)

You can also create private links that only your clients have access to, this is super useful when you want to share a lightweight, easily digestable dashboard of their site's performance.

It supports campaign tracking, goals, conversions, all the stuff that you care about. Excellent tool.

## Building

On to the fun stuff!

I'm a Python developer, I've used lots of Flask and Jinja2 templates over the years. I wanted my site to use Jinja2 for templates, so that it would always be easy for me to drop in and understand what's going on. I didn't want to have to learn a new JS template language just to render a few markdown files. I found a tool called [staticjinja](https://staticjinja.readthedocs.io/en/stable/) that works really well for me. You give it a directory of template files and it renders them all into an output directory. If you have files that aren't Jinja2 templates (e.g. markdown files) then you add some config to tell it what to do with those files. You can add hooks that pass in variables/data, so your pages can be properly templated and dynamic. For instance the blog post list page on my site is updated by using Python to walk through the directory and list all the files, passing the result to the template to render. It's pretty simple, understandable, and it uses the tech that I'm already really familiar with, so it feels easy.

My blog posts are written in markdown, using the Python library [Markdown](https://pypi.org/project/Markdown/) to render them into HTML, and then using Jinja2 to place that HTML inside my webpage.
