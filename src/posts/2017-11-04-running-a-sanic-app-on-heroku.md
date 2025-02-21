description: A quick guide to deploying a Python Sanic app on Heroku

# Running a Sanic App on Heroku

Here's the context; I've built lots of Python-based websites before, mostly using [Flask](http://flask.pocoo.org/). My latest side-project uses [Sanic](http://sanic.readthedocs.io/en/latest/) instead. I've hosted lots of websites on [Heroku](https://heroku.com) before, I've never hosted a Sanic app, and there didn't seem to be much in the way of documentation.  I managed to get something running, here's how.

### To Gunicorn or Not?

Normally, when it comes time to put an app in production, I turn to [Gunicorn](http://gunicorn.org/). The local flask development servers that I use until then aren't production-ready. This message, "not production-ready", is really drummed into you by the docs. Not so by the Sanic docs though. In fact, when I first read it, the [deployment section](http://sanic.readthedocs.io/en/latest/sanic/deploying.html) of their docs was incredibly sparse. This made me a bit uncertain, do I use the same server in production as I am for dev? Really? That doesn't seem right...

Turns out, it is! Whilst running behind gunicorn is possible, it [doesn't seem like it's encouraged](https://github.com/channelcat/sanic/issues/61#issuecomment-255982541). So no  pip install gunicorn, Sanic comes batteries included.

So what's in the Procfile? There are plenty of ways to get this working, here's mine:

    $ cat
    Procfile web: python web.py
    $ cat web.py
    import os

    from project import app

    if __name__ == '__main__':
        app.run(
            host='0.0.0.0',
            port=int(os.environ.get('PORT', 8000)),
            workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
            debug=bool(os.environ.get('DEBUG', ''))
        )

Pretty easy right? The only less-than-simple parts here are the environment variables:

   * PORT: This is set by Heroku to let the application know where to bind itself    to. In dev I can easily set this myself, or rely on the default 8000.
   * WEB_CONCURRENCY: This rather awesome variable is a recommendation from Heroku    on how many worker threads to use, given the dyno that the app is running in.    I'm anticipating modifying this slightly in the future, but for now, thanks    for the recommendation!
   * DEBUG: This one's pretty obvious, if there's a DEBUG environment variable,    then run Sanic in debug mode.

## Using asyncpg?

Here's a gotcha I came across. I'm using [asyncpg](https://github.com/MagicStack/asyncpg) to connect to a PostgreSQL database, I'm using a connection pool, like this:

    pool = await asyncpg.create_pool(
        dsn=os.environ['DATABASE_URL'],
        loop=loop # loop comes from sanic
    )

When I first booted my new app I tried to run the database migrations, they failed with a "max connections for role XYZ" error message. Turns out asyncpg will by default create 10 connections when the pool is created. Couple that with the 2 workers that Heroku recommend per Hobby dyno and you've hit the 20 connection limit on the free tier Postgres addon.

To connect to your DB using an external tool you have to turn off the web dynos so that your connections are freed up. That or pay more for your Heroku service :)

## Anything Else?

That's all I've got so far, I'll update this post when I come across more things worth noting down.
