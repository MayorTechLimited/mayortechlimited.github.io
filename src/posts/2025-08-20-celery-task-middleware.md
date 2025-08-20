---
description: How to add code that gets run before/after every time celery executes a Task
---

# Celery task "middleware"

I was looking for a way to run some logging code before and after every task execution
in my celery set up. I couldn't find anything that was immediately and obviously the
solution in Google. I tried Claude Sonnet 4 and it gave me 3 solutions, one of which,
after some tweaking, worked. (Which is my experience with LLMs in general.)

I'm using Django, and I've got some custom Django middleware that logs every database
query (not the values of the parameters, so no personal data is logged, just the SQL
statement with placeholders for values). This is useful for keeping an eye on which
queries are executed lots of times, which ones take a lot of time to run, and if there
are any requests that fire off too many queries (which would be evidence of a 1+N
problem).

The problem is that the middleware runs on every Django request, but a celery task
execution doesn't happen within a request. So any database queries being made in my
tasks weren't being logged.

I solved this by creating a custom Task class and overwriting the `__call__` method to
add the same logging that my middleware does.

I've got a file called `celery_.py` where I put my celery config, and it looks something
like this:

```python
from celery.contrib.django.task import DjangoTask
from django.db import connection


class DatabaseLogger:
    def __call__(self, execute, sql, params, many, context):
        instruction = sql.split(" ", 1)
        with logfire.span(instruction[0], type="query", sql=sql, many=many):
            return execute(sql, params, many, context)


class DatabaseLoggingTask(DjangoTask):
    def __call__(self, *args, **kwargs):
        with connection.execute_wrapper(DatabaseLogger()):
            return super().__call__(*args, **kwargs)


app = Celery("PROJECT", task_cls="PROJECT.celery_:DatabaseLoggingTask")
```

The `DatabaseLogger` class isn't that interesting really, it's a class with a call
method that conforms to the spec laid out by Django in their
[database instrumentation](https://docs.djangoproject.com/en/5.2/topics/db/instrumentation/)
docs. When called, it logs some details of the SQL query.

I'm using the excellent [logfire](https://logfire.dev/) library and service to do the
logging.

I'm making a best guess about the SQL instruction (SELECT, INSERT, DELETE etc.) by
looking at the first word in the query. It's probably not going to be correct in all
cases, for instance something with a CTE would say "WITH", which wouldn't be hugely
useful. But it will be enough when scanning over the logs quickly, you can always look
inside the span to see the actual details.

The `DatabaseLoggingTask` class is only slightly more interesting, and that's because
there aren't really many details on how to extend a `Task` class in the
[celery docs on Tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html#custom-task-classes).

There are a number of candidate methods on Task that could be overwritten to add our
logging code, they are `__call__`, `run`, `apply`, and `apply_async`. I considered each,
with the help of Claude.

Looking at the code we can see that `apply_async` calls `apply`, so we can rule that one
out. Any change we could make to `apply` would have the desired effect in `apply_async`
straightaway.

It wasn't super clear to me from reading the code when `apply` would get executed over
`run`, so I just tried it out. I overwrote `apply` and wrapped a call to `super().apply`
in the `execute_wrapper` as above... it didn't work. Nothing got logged, and a simple
print statement showed me that apply wasn't even getting called as far as I could see,
it must be used elsewhere.

`run` is interesting because the `@shared_task` decorator seems to set the `run`
function to be whatever function was decorated. So trying to overwrite `run` didn't seem
to work because it just got overwritten a second time.

That left `__call__`, which after a quick test, did what I needed. It's always in the
last place you look isn't it.

So if you're using celery in Django and want to add some celery "middleware" you should
be able to adapt the `DatabaseLoggingTask` above to fit your needs. If you're not using
Django, then replacing the parent class `DjangoTask` with the regular celery `Task`
should be enough to have the same effect.
