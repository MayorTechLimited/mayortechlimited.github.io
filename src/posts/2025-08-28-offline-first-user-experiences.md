---
description: Creating an offline-first user experience for invelope
---

# Creating an offline-first user experience for invelope

[invelope](https://invelope.co) is one of my many side projects. This one is a
family-friendly envelope budgeting tool. It's something I built so that my daughter and
I could organise the family's monthly shopping budget together, giving her some
important life skills.

One of the things I wanted to do with invelope was make it free for users. Or at least
as free as I could make it, without having to fork out lots of money each month to keep
things ticking over.

Hosting is basically free nowadays, especially for small projects that don't have a lot
of users. I'm using [Vercel](https://vercel.com) for invelope, it currently costs me
nothing to run, and when invelope becomes the next big thing, it'll only cost me about
$20 per month.

But that's just to host the app, it doesn't include a database. Those tend to be a bit
more expensive.

There are solutions out there that will give you a generous free tier that includes a
database. Supabase is one of my favourites, another side project,
[billabl](https://billabl.co) runs over there.

I wanted to try something different with invelope. I wanted to have the user's data
stored locally in their browser, and nothing stored on any servers that I manage. This
makes the free tier of invelope almost infinitely scalable, it doesn't matter how many
people use the service, the data storage and processing all happens on their computer,
not mine. I could even re-build invelope to be a static site, making hosting even
cheaper.

So I turned to [IndexedDB](https://en.wikipedia.org/wiki/IndexedDB) for the local
database side of things. This gives me a NoSQL database that I can use, that runs in the
user's browser. It's a bit fiddly to use, but here's a basic example of adding a budget:

```javascript
let open = indexedDB.open('invelope', 1);
open.onsuccess = function() {
    let db = open.result;
    db.createObjectStore('budgets', {
        keyPath: 'id'
    });
    let budgets = db.transaction('budgets', 'readwrite');
    budgets.add({
        id: 1,
        name: 'August',
        amount: 1000
    });
};
```

There's a lot more you can do here around versioning and error handling, but I've
skipped that for brevity.

There are some obvious downsides to a local database like this. The data is only every
held on a single browser on a single device. So there are no backups, if you lose your
phone or your laptop breaks then you've lost all of your data. You also can't share
between devices, so you can't have the same budget on your phone and on your laptop at
the same time (or in my case, on my laptop and my daughter's laptop).

The obvious solution is to have some kind of cloud sync feature, which mirrors the local
database state into the cloud and can then pull that state down on every extra device.
There are quite a few solutions out there for adding cloud sync to an IndexedDB
database, for invelope I went with [Dexie](https://dexie.org/).

Dexie is a lightweight wrapper around IndexedDB that, in my opinion, makes the syntax
nicer, and has extra features for syncing into the Dexie Cloud. Now the snippet above
looks like this:

```javascript
import Dexie from "dexie";

const db = new Dexie('invelope');
db.version(1).stores({
    budgets: '++id'
});
await db.budgets.add({
    name: 'August',
    amount: 1000,
});
```

There's no callback to open the database, and no transaction for these kinds of basic
edits. The code is just simpler and nicer to read. Also, the schema for the budgets
store declares an `id++` field, which means that Dexie will auto-create an `id` field
for every document and will give it a locally unique ID.

To add cloud sync:

```javascript
import Dexie from "dexie";
import dexieCloud from "dexie-cloud-addon";

const db = new Dexie('invelope', {
    addons: [dexieCloud]
});
db.version(1).stores({
    budgets: '@id'
});
db.cloud.configure({
    databaseUrl: "https://UNIQUE_ID.dexie.cloud"
});
await db.budgets.add({
    name: 'August',
    amount: 1000,
});
```

Now the ID field is declared using `@id` which means it gets a globally unique ID.
There's also some config to connect to the correct database endpoint in the cloud. But
that's it. When the user makes changes to their local database it will get pushed up to
the cloud and then pulled down to every other device signed into the same account. Dexie
even manages the authentication flow as part of the service.

There's lots more you can do with Dexie. It plays really nicely with svelte because the
result objects conform to the Observable interface meaning that svelte can treat them
like regular stores and use the `$budgets` notation to access the value. I've been
customising the authentication flow to add invelope branding to the popups, and
eventually I'll change from the default emails too.

Crucially, my Vercel servers don't know anything about Dexie or anything about my users'
data. The invelope app could be re-built as a static site, with no server-side code at
all, and it would still work as it currently does. It's not quite a cop-out to rely on
Dexie to do the server-side sync bits because, unlike regular webapps, there isn't any
server-side database querying happening, Dexie is effectively moving a blob of data
around between machines, it doesn't need to look inside that blob, it doesn't need to do
any processing.

This should mean that I can continue to run invelope on a shoe string budget for a long
time (of course it would be great if people would sign up to the premium tier as well).
