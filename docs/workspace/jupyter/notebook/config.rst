Jupyter paths and configuration
===============================

Configuration files are usually stored in the ~``~/.jupyter`` directory.
However, another directory can be specified with the environment variable
``JUPYTER_CONFIG_DIR``. If Jupyter cannot find a configuration in
``JUPYTER_CONFIG_DIR``, Jupyter runs through the search path with
``{sys.prefix}/etc/jupyter/`` and then for Unix ``/usr/local/etc/jupyter/`` and
``/etc/jupyter/``, for Windows ``%PROGRAMDATA%\jupyter\``.

You can have the currently used configuration directories listed with:

.. code-block:: console

    $ pipenv run jupyter --paths
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

    $ pipenv run jupyter notebook --generate-config
    Writing default config to: /Users/veit/.jupyter/jupyter_notebook_config.py

More generally, configuration files can be created for all Jupyter applications
with:

.. code-block:: console

    $ pipenv run jupyter {application} --generate-config

Change the configuration
------------------------

… by editing the configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

e.g. in ``jupyter_notebook_config.py``:

.. code-block:: python

    c.NotebookApp.port = 8754

If the values are saved as ``list``, ``dict`` od ``set``, they can also be
supplemented with  ``append``, ``extend``, ``prepend``, ``add`` and
``update``, e.g.:

.. code-block:: python

    c.TemplateExporter.template_path.append('./templates')

… with the command line
~~~~~~~~~~~~~~~~~~~~~~~

e.g.:

.. code-block:: console

    $ pipenv run jupyter notebook --NotebookApp.port=8754

There are aliases for frequently used options such as for ``--port`` or
``--no-browser``.

The command line options override options set in a configuration file.

.. seealso::
   `traitlets.config
   <https://traitlets.readthedocs.io/en/latest/config.html#module-traitlets.config>`_
