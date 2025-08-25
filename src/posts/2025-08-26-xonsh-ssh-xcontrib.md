---
description: How I got Xonsh to auto-complete using my SSH config
---

# Xonsh SSH auto-complete

I recently tried switching over to the [xonsh shell](https://xon.sh/index.html). I'm
normally a very happy bash user, but a few years ago MacOS started shipping with zsh as
the default shell and that started me on a journey of new shell discovery. Don't get me
wrong, zsh is pretty good, and I'm a big fan of [oh-my-zsh](https://ohmyz.sh/) and all
of the plugins and themes it comes with. But now that I'm not always using bash, I'm
free to take a look around and explore the other options.

xonsh appeals to me because it's a python-based shell. That means the code that runs the
shell is written in Python, so it's easy for me to take a look if I want. It also means
that interacting with the shell means writing Python code, which I'm very happy to do.
Plugins and extensions are all in Python too.

When I first installed it I noticed something that was missing. SSH host autocomplete. I
start up the shell, type `ssh <tab>` and nothing, it doesn't present me with a list of
SSH command options, or hostnames, nothing. I'm used to hostname autocompletion from
zsh, it's very handy.

I couldn't find anything in the docs about hostname autocomplete, so I don't think it's
something supported out of the box. I did find lots about how to make your own
autocomplete plugin (or a xontrib in xonsh parlance).

This felt like an opportunity too good to miss. So I built one, here it is:

```python
from pathlib import Path

from xonsh.built_ins import XonshSession
from xonsh.completers.tools import contextual_command_completer_for
from xonsh.completers.completer import add_one_completer, remove_completer


def make_absolute(path):
    if not path.is_absolute():
        return Path.home() / ".ssh" / path
    return path


def find_hosts(config_file):
    config_file = make_absolute(config_file)
    if config_file.exists():
        with open(config_file, "r") as f:
            for line in f:
                line = line.strip()
                if line.lower().startswith("host "):
                    # Skip wildcards like '*'
                    hosts = line.split()[1:]
                    for host in hosts:
                        if "*" not in host and "?" not in host:
                            yield host
                elif line.lower().startswith("include "):
                    includes = line.split()[1:]
                    for include in includes:
                        if "*" in include:
                            root, rest = include.split("*", 1)
                            root = make_absolute(Path(root))
                            for p in root.glob(f"*{rest}"):
                                yield from find_hosts(p)
                        else:
                            yield from find_hosts(Path(include))


def get_ssh_hosts():
    ssh_config_files = [
        Path.home() / ".ssh" / "config",
        Path("/etc/ssh/ssh_config"),
    ]
    for config_file in ssh_config_files:
        yield from find_hosts(config_file)


@contextual_command_completer_for("ssh")
def ssh_completer(context):
    hosts = get_ssh_hosts()
    return {host for host in hosts if host.startswith(context.prefix)}


def _load_xontrib_(xsh: XonshSession, **kwargs) -> dict:
    add_one_completer("ssh-hosts", ssh_completer, "start")
    return {}


def _unload_xontrib_(xsh: XonshSession, **kwargs) -> dict:
    remove_completer("ssh-hosts")
    return {}
```

Most of the file is setup and installation code, nothing interesting happening that you
couldn't just read in the xonsh docs. The interesting parts are the `get_ssh_hosts` and
`find_hosts` functions. The former is responsible for looking in directories that
commonly contain SSH config files, when it finds one it passes it to the latter,
`find_hosts`, and yields the responses.

`find_hosts` goes through the config file line by line looking for config that is either
a) a host directive that can be yielded back as a named host for the user to pick from,
or b) is a nested include directive that calls `find_hosts` again with a new config
file.

!!! info "Heads up"
    This file was written to be installed on my computer, and might not work on yours. You
    might have to tweak the file paths and change some of the assumptions I've made.

You can install and use this xcontrib on your own machine. Copy and paste the contents
into a file, I called mine "ssh_host_completer.py". Then save that file to a location
you like. Then update your `.xonshrc` file to add the location to your path and then
load the xontrib:

```python
path.append("/path/to/location")
xontrib load ssh_host_completer
```
