description: A quick guide to getting a small server up and running, ready to run some code

# Small Project Skeleton: The Server

Fairly often I'll need to spin up a new server for a smallish project that I'm working on. Maybe a demo/staging site for a client, or maybe I've started a new side-project again.

Over the years I've found a way of doing things that I like, and that I'm going to document here. So this post should be useful for you if you want to get a new server up and running with sensible security defaults and a largely blank slate for actually creating your site.

## The Hardware

First things first, you'll need an actual server. There are plenty of **cloud providers** to choose from. My preferred provider at the moment is [Digital Ocean](https://www.digitalocean.com/). I think they provide a very good service at a good price.

You normally have to choose what **operating system** to use on your server. I tend to pick Ubuntu or Debian, but any Linux flavour is probably a good choice. Pick a recent but LTS (long-term support) version.

If you can **setup a firewall** for your new server this is a good idea. A firewall at the level of your hosting provider will be largely pain free from your point of view. I set mine up to allow (whitelist) traffic from any IP but only to ports 80 (http), 443 (https), and 22 (ssh).

If you're given the choice of setting up a **fixed (or static) IP address,** do this too.

Some providers give you the option to pre-load your new server with an **SSH key**. This is an awesome feature, definitely do this. If you don't already have an SSH key, I'd recommend looking up the [GitHub](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) or [GitLab](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html) instructions on how to create one. They tend to keep their docs up to date with latest best practises.

Check to see if your cloud provider offer **automated backups**. This is often a very useful failsafe. Turn it on and forget about it. If you ever have a huge data loss you know for certain that you will be able to restore the entire machine to a recent-ish state.

Setup any simple **alerts and notifications** that your provider offer. It's very useful to be sent an email when your server is starting to use all of its memory, or when it's using 90% of its CPU all the time.

## DNS

Now you have a server and an IP address you should point your domain at it.

If you need to **find a domain name** first I'd recommend [Domainr](https://domainr.com) as a tool to use to quickly find available domain names. It has a cool feature where you can type in the name of your project (without a TLD like .com) and it will give you lots of options that use the letters in the name. Just like Domainr have [domai.nr](https://domai.nr) as a domain alias.

Then **register the domain** name. I'd recommend [Hover](https://www.hover.com) as a domain registrar, I've also used DNSSimple and found them to be very good.

Now add some **DNS rules**:

    A @.DOMAIN IP-ADDRESS
    A *.DOMAIN IP-ADDRESS

Pretty simple, just point the **root** of your domain (the `@` part) to your IP address, then point all **subdomains** (the `*` part) to the same IP address.

## SSH

Now you'll want to actually **connect to the new server** and get started! So open up your terminal emulator of choice (I use [iTerm2](https://iterm2.com)) and type this:

    $ ssh -i PATH_TO_PRIVATE_SSH_KEY root@IP-ADDRESS

The path to the SSH key will likely be something like this: `~/.ssh/id_rsa`.

The **default username** might be `root` but it might be something else. It depends on which operating system you picked and how your provider has set it up. I've seen things like `admin` and `ubuntu` used before. Check with the documentation for your hosting provider.

### Using Root User?

If you're logging in as `root` then let's **beef up the security** a little bit. We'll **create a new user** to log in as instead. You don't want a bad guy to crack through your SSH setup and then immediately have root access.

These **instructions are for Ubuntu,** you might have to find different instructions if you're using a different OS.

    # adduser USER
    # usermod -aG sudo USER
    # cp ~/.ssh home/USER/
    # chown -R USER:USER /home/USER/.ssh

Replace `USER` with the username you want to use.

The above commands create a new user, add that user to the `sudo` group then setup the new user's SSH to use the same authorized keys as your root user does.

Let's test the setup by trying to log in as the new user, open up a new tab/window in your terminal and try to SSH in:

    $ ssh -i PATH_TO_PRIVATE_SSH_KEY USER@IP-ADDRESS

If that works we'll now want to turn off SSH access for the root user. Open up the `/etc/ssh/sshd_config` file in your terminal editor of choice and change the `PermitRootLogin` line to say `PermitRootLogin=no`.

Whilst we're editing the config, let's change the default SSH port to give us a bit of protection from port scanning bots. Find the line that says `# Port=22` and change it to `Port=RANDOM_NUMBER`. Pick a large random number greater than 10,000. You'll have to add this port to your firewall, and remove the port 22 rule.

Then restart the SSH daemon:

    # service ssh restart

This is the basis for a pretty sound SSH setup, as far as I know anyway, I'm not a security expert.

### SSH Config

The final step I take is to add our SSH arguments to the **SSH config** file on my local machine to make accessing the remote machine nice and easy next time. Find or create the `~/.ssh/config` file and add this to it:

    Host PROJECT
        User USER
        HostName IP-ADDRESS
        PasswordAuthentication no
        Port RANDOM_NUMBER
        IdentityFile PATH_TO_PRIVATE_KEY

Replace `PROJECT` with whatever project name would make sense. Now you can do this:

    $ ssh PROJECT

You don't need to remember which user, or which SSH key. Easy!

## Done?

So now we have a server running, we've got backups, a firewall, and a reasonable SSH setup. We can now start putting applications on the server :)

## Outgrowing this Setup

This is a series on how to get a small project with low traffic up and running. The guides here are not going to suit larger projects with more requirements. Having said that, here are some ideas you might like to Google for when this setup stops working for you:

**Scale vertically** by making your server bigger. Just go to your cloud provider and give the machine a better spec. More RAM, faster processors, more processors, more hard disk space. Which bit you need to scale up will depend on what your project is using most of.

**Scale horizontally** by adding more (identical) servers. You'd also need to look at things like load balancers. Scaling horizontally is harder to do than vertically, but it does give you more flexibility.

You could consider **hosting somewhere else,** somewhere that would manage lots of this low level hardware set up for you. At a price of course. I'd recommend Heroku as a platform-as-a-service solution. Scaling to meet demand with Heroku is as easy as moving a slider up and down.
