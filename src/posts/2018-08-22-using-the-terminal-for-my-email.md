# Using the Terminal for my Email

Over the last several years I've flitted from email client to email client, never satisfied. They were either too ugly, too hard to use, or too slow. Too slow has been the bane of my existence for the past several months, my client of choice just ground to halt. I had to open it up and wait for minutes (!!) whilst it \"indexed\" things.

So last week I decided to make a change and switch to reading and writing emails in the terminal. I knew it was possible, I just hadn't had the impulse to switch until now.

Which Software? After reading several websites, guides, and man pages I settled on:

 * OfflineIMAP (for downloading my email)
 * notmuch (for indexing and tagging my email)
 * alot (for searching and reading my email)
 * MSMTP (for sending email)

 Installing things was a bit of a pain, and was actually the deciding factor in some of my choices above. I cannot work out how to install the latest version of alot, I'm a Python dev, I know how to pip install things, but I couldn't get it to work here. In the end I settled for whatever I could install via brew.

 Configuring things is a dream! You write everything down in text files! I couldn't be happier. I've got lots of email account that use very similar settings (e.g. same IMAP server), it's just a case of copy pasting things. Wonderful! Plus, all my settings are now part of my backups. This is how all config should be.

 Actually using things? That's pretty good too. I've got a script that bundles my sync+tag+read+sync flow, and I just run it whenever I want to read email. I'm slowly getting there with customising things to my liking. alot has lots of options and I'm adding new things in as I go.

It's been lovely to have more control over syncing my email. I only run the offlineIMAP stuff when I want new email. If all I want to do is read an old email, then I can boot up alot separately. That's been a surprising benefit to this process.

What don't I like? So far I think I'm not a fan of just how many tools I need to get things done. Especially when those tools overlap in lots of ways. The biggest example is how offlineIMAP and MSMTP both need credentials to download and send emails. That means I'm duplicating config all over the place. The config files are in slightly different places and at the moment I'm not sure which bit of config I need to change to get something done.

Overall, I'm really liking it. It's a whole new, pretty, simple, and fast email experience!
