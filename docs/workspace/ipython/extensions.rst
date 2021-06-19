IPython extensions
==================

IPython extensions are Python modules that change the behavior of the shell.
They are identified by an importable module name and are usually located in
``.ipython/extensions/``.

Some important extensions are already included in IPython:
:label:`extensions_autoreload` and :label:`extensions_storemagic`. You can find
other extensions in the `Extensions Index
<https://github.com/ipython/ipython/wiki/Extensions-Index>`_ or on PyPI with
the  `IPython tag <https://pypi.org/search/?c=Framework+%3A%3A+IPython>`_.

.. seealso::
    * `IPython extensions docs
      <https://ipython.readthedocs.io/en/stable/config/extensions/index.html>`_

Use extensions
--------------

The ``%load_ext`` magic can be used to load extensions while IPython is running.

.. code-block:: ipython

    %load_ext myextension

Alternatively, an extension can also be loaded each time IPython is started by
listing it in the IPython configuration file:

.. code-block:: Python

    c.InteractiveShellApp.extensions = [
        'myextension'
    ]

If you haven’t created an IPython configuration file yet, you can do this with:

.. code-block:: console

    $ ipython profile create [profilename]

If no profile name is given, ``default` is used. The file is usually created in
``~/.ipython/profile_default/`` and named depending on the purpose:
``ipython_config.py`` is used for all IPython commands, while
``ipython_notebook_config.py`` is only used for commands in IPython notebooks.

Writing IPython extensions
--------------------------

An IPython extension is an importable Python module that has special functions
for loading and unloading:

.. code-block:: python

    def load_ipython_extension(ipython):
        # The `ipython` argument is the currently active `InteractiveShell`
        # instance, which can be used in any way. This allows you to register
        # new magics or aliases, for example.

    def unload_ipython_extension(ipython):
        # If you want your extension to be unloadable, put that logic here.

.. seealso::
    * :label:`defining_magics`
