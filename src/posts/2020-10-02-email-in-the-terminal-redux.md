# Email in the Terminal: Redux

More than two years ago I wrote a post about [reading my emails via a terminal interface](/posts/using-the-terminal-for-my-email/) instead of a GUI. That solution lasted me a good while but eventually I gave up and switched to a new GUI. I switched because it was too much of a pain not having access to my emails when I was out and about. With my emails only ever on my laptop I couldn't easily do things like find a ticket to an event that had been emailed to me, or quickly reply to something whilst on the bus.

I used an email client that offered fantastic sync features between all my devices. If I added an account on my laptop, it just appeared on my phone. Problem solved.

Then the slow bugginess of GUI email clients came to get on my nerves again. So now I'm back looking for a snappy Terminal User Interface (TUI) option that will let me access my emails on the go.

Here are my requirements for an email client solution:

 * Fast (to start up, to search, to fetch, to send)
 * Easy to use on multiple devices
 * Easy to add new accounts and access on all devices
 * Keeps emails safe (offline backup)

Here's the new plan:

I'm going to create a server in the cloud specifically for coping with my emails. I'll SSH into it when I want to read my emails. This way I can access them from any computer that can SSH.

I'm going to use OfflineIMAP and notmuch to sync and index my emails. This gives me an offline backup of all of my emails and also gives me really fast search and tagging.

I'm going to use aerc to read and send email.
