# `cell_shell_magic`

Install with:

`pip install --upgrade git+https://github.com/innovationOUtside/cell_shell_magic.git`

Call it by:

`%load_ext cell_shell`


A really simple piece of magic that hacks the IPython input transformation ([docs](https://ipython.readthedocs.io/en/stable/config/inputtransforms.html)) to rewrite the contents of a cell that is *not* prefixed in the first line by a `%` so that the first line is a Python block cell magic: `%%python`

This has the effect of executing the code in each code cell in its own Python shell.

So no hidden state. In face, no state outside the cell. Like running a py file.

I bet you that folk will still complain though. *"Oh, it doesn't have state. It's really rubbish and not a REPL at all..."*