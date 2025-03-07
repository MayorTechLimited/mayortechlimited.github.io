description: An explaination of how this website is built, maintained, and hosted.

# This Blog's Tech Stack

This feels like one of those trite blog posts that every software engineer writes, so I apologise if this post is dull. However, I wanted to get back into writing blog posts, something I've never been able to manage very well, and this seemed like an easy win.

So here goes...

## Hosting

It's hosted on GitHub Pages, for free! It's a static site, and I wanted it to be fast, always available, and hassle free. GitHub Pages is exactly that, so this was a bit of a no-brainer.

## Analytics

I use a privacy-first analytics tool called [Pirsch](https://pirsch.io), it doesn't set cookies or anything like that, it just tells me which pages people are visiting.

They have a useful system where you can create dashboards of data and share it with other people. For instance you can see all of the analytics data for my blog on the public dashboard: [https://mayortech.pirsch.io](https://mayortech.pirsch.io). As you can see, I don't get much traffic :)

You can also create private links that only your clients have access to, this is super useful when you want to share a lightweight, easily digestible dashboard of their site's performance.

It supports campaign tracking, goals, conversions, all the stuff that you care about. Excellent tool.

## Building

On to the fun stuff!

The GitHub repo for this site is here: [https://github.com/MayorTechLimited/www](https://github.com/MayorTechLimited/www). You can look at the raw contents of the site, and the scripts that build it, on the `develop` branch. The `main` branch has just the built version of everything.

I'm a Python developer, I've used lots of Flask and Jinja2 templates over the years. I wanted my site to use Jinja2 for templates, so that it would always be easy for me to drop in and understand what's going on. I didn't want to have to learn a new JS template language just to render a few markdown files. I found a tool called [staticjinja](https://staticjinja.readthedocs.io/en/stable/) that works really well for me. You give it a directory of template files and it renders them all into an output directory. If you have files that aren't Jinja2 templates (e.g. markdown files) then you add some config to tell it what to do with those files. You can add hooks that pass in variables/data, so your pages can be properly templated and dynamic. For instance the blog post list page on my site is updated by using Python to walk through the directory and list all the files, passing the result to the template to render. It's pretty simple, understandable, and it uses the tech that I'm already really familiar with, so it feels easy.

My blog posts are written in markdown, using the Python library [Markdown](https://pypi.org/project/Markdown/) to render them into HTML, and then using Jinja2 to place that HTML inside my webpage.

The staticjinja library doesn't do anything with static files, it only cares about taking templates and outputting HTML files. So I needed something to watch an input directory of static files and copy them over to a destination/build directory when something changes. I ended up over engineering this, because it was fun.

I have a script called `watch_static.py` that uses the [watchdog](https://pypi.org/project/watchdog/) package to respond to file change events inside a folder called `static`. When a file is changed inside that folder the script runs a function to synchronise the contents of the `static` folder into the `dist` directory where the rest of the website is built. It keeps a record of all of the static files that it deals with in a file called `.static`. This way when a file is removed from the `static` directory, it can be removed from the `dist` directory too.

What this doesn't do is append any kind of cache busting hashes to the file names. This is something that you'd get for free if you used any of the popular JS libraries, it's a really useful feature. Hopefully I'll be able to build it into my script in the future.

The final piece is the CSS that makes the site look nice. This is all based on tailwind. I use the standalone executable that the tailwind people provide. This is nice and simple and produces a minified and tree shaken CSS file.
