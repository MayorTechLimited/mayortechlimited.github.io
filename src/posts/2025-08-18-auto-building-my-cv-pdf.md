description: How I setup Puppeteer to automatically generate a PDF of my CV

# Automatically building a PDF of my CV

I have a web version of [my CV online](/cv/).

I'm currently applying for lots of jobs, so I'm making tweaks to my CV all the time. In a previous post I
talked about how (and why) I've [made the CV editable online](/posts/2025-08-09-editable-cv/).
The problem I was facing this time is that when I make changes to the original CV I want
to have the web version and PDF version stay in sync, without me having to remember to
manually save the web version as a PDF.

Changing the HTML side of things is nice and easy. But regenerating the PDF is a fiddly pain, so I decided to automate it.

## 1. Add Puppeteer to my project

I already had a Docker-based build system for my website, I just needed to add Puppeteer
as a new dependency. Puppeteer is a node library so I needed to install node and npm, and
then use npm to install Puppeteer. All standard stuff.

What makes it fun is that my local dev machine is an M1 Mac, and I've been using the
Linux ARM64 runners in GitHub Actions to run the build system (in order to have a little
bit of parity between my dev machine and the "production" machine). Most of the world
(but certainly the Puppeteer docs) assume that you're running x86_64 and the installation
instructions often end up causing very confusing errors. In this case I had an ubuntu
linux docker image printing a rosetta error message:

```
rosetta error: failed to open elf at /lib64/ld-linux-x86-64.so.2
```

But rosetta is a MacOS utility, not something you'd find installed in a Linux Docker image!

After a fair amount of fiddling with how to get ARM64 builds running with Chromium I've
ended up with this setup in the Dockerfile:

```
FROM debian:latest

RUN apt update && apt install -y --no-install-recommends \
    chromium \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /pdf

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash && \
    bash -c "source /root/.nvm/nvm.sh && \
        nvm install 22.18.0 && \
        nvm use 22.18.0 && \
        npm install puppeteer"
```

What ended up being super important was a) to switch from ubuntu to debian because the
chromium build in ubuntu requires using snap, which seemed like a very silly/complex dependency to have to add to a docker image, and b) to install
chromium manually, and not rely on Puppeteer to install it itself (which it didn't seem
to be able to do).

!!! info "Side bar"
    The Docker system I'm talking about here is only the build system. It outputs static
    HTML that is hosted using GitHub pages. So there are no Docker containers in my stack
    that a reader would ever interact with.

The next fiddly bit was to get the nvm managed version of node to be loaded up and
recognised when using `docker run`. Outside of docker this is done by adding
`source /root/.nvm/nvm.sh` to your shell profile, but that isn't going to work here very
well. You don't normally run a full/modern interactive shell inside a docker image, it's
wasteful, you don't need history and bash completions etc. Normally you're using something
super lightweight like `sh`. So I can't easily rely on shell startup profile scripts,
instead I modified the entrypoint of the docker image, but only when running the `pdf`
service, here's what I added to my docker compose file:

```
pdf:
    build: .
    tty: true
    stop_signal: SIGINT
    working_dir: /pdf
    entrypoint: ["bash", "-c", 'source /root/.nvm/nvm.sh && exec "$@"', "--"]
    command: ["node", "/pdf/makePdf.js"]
    volumes:
        - .:/app
```

It's that entrypoint part that's doing the heavy lifting, sourcing the nvm set up script
and then immediately executing whatever the original command was.

## 2. Write/run JS script

Next I needed to be able to load the local HTML file with my CV in it into Puppeteer and
have it save the page as a PDF:

```
const browser = await puppeteer.launch({
    executablePath: "/usr/bin/chromium",
    args: [
        "--no-sandbox",
        "--headless",
        "--disable-gpu",
        "--font-render-hinting=none",
    ],
});
const page = await browser.newPage();

await page.setRequestInterception(true);
page.on("request", (request) => {
    const headers = {
        ...request.headers(),
        Origin: "https://www.mayortech.co.uk",
    };
    request.continue({
        headers: headers,
    });
});
await page.goto("file:///app/dist/cv/index.html", {
    waitUntil: "networkidle0",
});
await page.pdf({
    path: "/app/dist/William Mayor's CV.pdf",
    format: "A4",
    margin: {
        top: "0px",
        left: "0px",
        right: "0px",
        bottom: "0px",
    },
    printBackground: true,
});
await browser.close();
```

This is mostly a pretty simple set up. I've got a full page background on my CV, so I
had to set the margins to be 0 (relying on the HTML padding in the page to push the
content away from the edges), and then use the `printBackground: true` setting to allow
the "printed" PDF to use the background colour.

The most fun issue to solve was that the Font Awesome icons wouldn't load. At first I
thought it was a timing issue; maybe the assets were loading in but the page wasn't
given enough time for Font Awesome to switch out the `<i>` elements with the `<svg>`s
they actually use for the icons. But I added in some really large timeouts and it didn't
solve the problem.

So I loaded up the file in my local browser using the `file://` protocol, not
`http://` as I normally use. This replicated the issue that Puppeteer was seeing and I
could see from the network tab that Font Awesome was returning a 403 error saying that
the origin for the page wasn't set. This makes sense, I'm loading up a local file, I'm
not serving a page in the normal manner, there is no origin. I looked to see if I could
whitelabel the `file://` protocol in my Font Awesome settings, but I don't think you can.
So next I looked into spoofing the origin to get Font Awesome to be happy. You can do
this really easily using curl:

```
$ curl -H "Origin: https://example.com" https://kit.fontawesome.com/YOUR_KIT_CODE.js
```

After I verified that this would work I looked at how to add the origin header in
Puppeteer. You should be able to add it using `page.setExtraHTTPHeaders` but this didn't
work for me, Font Awesome still returned a 403 error. So instead I used request
intercepting to add the header to each request as it left the browser:

```
await page.setRequestInterception(true);
page.on("request", (request) => {
    const headers = {
        ...request.headers(),
        Origin: "https://www.mayortech.co.uk",
    };
    request.continue({
        headers: headers,
    });
});
```

At the time of writing there's an open bug ticket in the Puppeteer repo about
inconsistent text rendering in the headless vs non-headless modes. The fix is to add
that `--font-render-hinting=none` parameter to the launch args.

## 3. Tell GitHub Actions to generate, save, and deploy the PDF version

This one was the simplest bit, once I had the system working locally I then needed to add
a step to my GitHub Actions:

```
- name: Build PDF version of CV
  run: docker compose run --rm pdf
```

That's it! The hard work is done inside Docker, so once it's working locally, getting it
to run in GitHub is usually pretty easy (ignoring the pain that can come with trying to
get GitHub to run anything at all).
