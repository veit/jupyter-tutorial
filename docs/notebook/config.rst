Jupyter paths and configuration
===============================

Configuration files are usually stored in the :file:`~/.jupyter` directory.
However, another directory can be specified with the environment variable
:envvar:`JUPYTER_CONFIG_DIR`. If Jupyter cannot find a configuration in
:envvar:`JUPYTER_CONFIG_DIR`, Jupyter runs through the search path with
:file:`/{SYS.PREFIX}/etc/jupyter/` and then for Unix
:file:`/usr/local/etc/jupyter/` and :file:`/etc/jupyter/`, for Windows
:file:`%PROGRAMDATA%\\jupyter\\`.

You can have the currently used configuration directories listed with:

.. code-block:: console

    $ jupyter --paths
    config:
        /Users/veit/.jupyter
        /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/../etc/jupyter
        /usr/local/etc/jupyter
        /etc/jupyter
    ...

Create the configuration files
------------------------------

You can create a standard configuration with:

.. code-block:: console

    $ jupyter notebook --generate-config
    Writing default config to: /Users/veit/.jupyter/jupyter_notebook_config.py

More generally, configuration files can be created for all Jupyter applications
with :samp:`jupyter {APPLICATION} --generate-config`.

Change the configuration
------------------------

… by editing the configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

e.g. in ``jupyter_notebook_config.py``:

.. code-block:: python

    c.NotebookApp.port = 8754

If the values are saved as ``list``, ``dict`` or ``set``, they can also be
supplemented with  ``append``, ``extend``, ``prepend``, ``add`` and
``update``, e.g.:

.. code-block:: python

    c.TemplateExporter.template_path.append('./templates')

… with the command line
~~~~~~~~~~~~~~~~~~~~~~~

for example:

.. code-block:: console

    $ jupyter notebook --NotebookApp.port=8754

There are aliases for frequently used options such as for ``--port`` or
``--no-browser``.

The command line options override options set in a configuration file.

.. seealso::
   `traitlets.config
   <https://traitlets.readthedocs.io/en/latest/config.html#module-traitlets.config>`_
