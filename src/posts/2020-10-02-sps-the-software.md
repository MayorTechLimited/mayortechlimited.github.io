# Small Project Skeleton: The Software

Assuming you've read the first part to this guide: Small Project Skeleton: The Server [/sps-server], you're now ready with a blank machine and you need to install things on it.

## System Updates

The first thing I'd do is run any system updates and upgrades. It's always good to start from the most recent working version of things:

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get autoremove

Performing these kinds of updates whilst the project is running can be trickier sometimes as updates to software your project relies on can break things. So run future updates with caution.

## Dokku

Now we're going to install dokku. dokku is a open source tool that makes your server act a bit like Heroku. The eventual goal is that deployments become as simple as git push dokku.

Dokku will manage databases, caches, SSL certificates, nginx, and a whole bunch of things. It's going to make our lives much easier.

Here's dokku's website: http://dokku.viewdocs.io/dokku/

Open that link and run the installation commands on your server. They'll look something like this: (but dokku may have been updated since this post)

    $ wget https://raw.githubusercontent.com/dokku/dokku/v0.20.3/bootstrap.sh
    $ sudo DOKKU_TAG=v0.20.3 bash bootstrap.sh

Let than run whilst it installs things. Then browse to your server's IP address or domain name using your browser. There are a few setup steps to go through.

First of all copy your SSH public key into the public key box in the Dokku settings page, that's nice and easy.

Then tell it what domain you'd like to use. You can add/remove domains later one so don't worry too much about this one. Just plug in the domain you connected up to the machine previously.

Then I always tick the box to use vhost naming. This just means that you can have nice URLs per app.

Then hit the save button and you're done installing Dokku!

## Dokku Plugins

There are a bunch of dokku plugins that I almost always install, check out Dokku's docs for a list of all of them though. I won't go into installation steps here because things might change between when I wrote this guide and when you read it. Just read the docs on the plugin's page.

For running a database take a look at [dokku-postgres](https://github.com/dokku/dokku-postgres). You install the plugin, create a DB, link the database to your apps and you're done. Lovely :)

There's also [dokku-redis](https://github.com/dokku/dokku-redis) which is great for asyncronous workers, caching, or simple key/value storage. Again, the plugin makes managing redis instances really easy.

I love the [dokku-letsencrypt](https://github.com/dokku/dokku-letsencrypt) plugin, it manages the SSL certs for you in a really easy way. Remember to run this command to make sure your certs are auto-renewed:

    $ dokku letsencrypt:cron-job --add

## Other Things

You have a domain name and a website. The next logical thing to get would be an email address. There are so many email providers out there you've really got too much choice. Here are the ones I've used and could recommend:

[GSuite](https://gsuite.google.com/) from Google offers GMail using your own domain. With GSuite you also get access to Google Drive, Calendars, Hangouts (or Meet, or Duo), etc. etc. It's a huge offering. I've found GSuite to be very reliable, but it can be expensive as they charge per user. I'm also less inclined to give Google yet more of my data.

[FastMail](https://www.fastmail.com/) offer email using your own domain. This is a rock solid email service that I can't recommend enough. They don't have the feature set of GSuite but if you care about privacy then maybe this is a better choice.

Finally, if you have too many side projects to pay for GSuite on each one I'd go for [Migadu](https://www.migadu.com/en/index.html). You pay for one account but you can set up as many domains as you like. It's a great service.

## Outgrowing this Setup

This is a series on how to get a small project with low traffic up and running. The guides here are not going to suit larger projects with more requirements. Having said that, here are some ideas you might like to Google for when this setup stops working for you:

Cache things (or use a CDN) to speed up responses. Lots of website content updates quite rarely and there's no need to have your webserver do the hard work of rendering and returning that data. Static assets like images, CSS, and JS often fall into this category. Sometimes you can cache full rendered HTML pages too. One of the easiest ways to cache this kind of content is to use CloudFlare. You set up CloudFlare to sit between your website and your users. When your users request a page CloudFlare will either send that request over to your site, or immediately return a cached version. It's free too!

So far we've got all of our services on one machine. This probably won't last us long. So we'll have to think about moving some of our dependencies onto different machines. Probably the easiest one to start with is the database. There are lots of hosted database services out there, Digital Ocean provide  managed Postgres and Redis. AWS has RDS and just about every service you could think of. Similarly for Google Cloud and Microsoft Azure.
