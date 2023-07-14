``nbviewer``
============

`nbviewer <https://github.com/jupyter/nbviewer>`_
    :doc:`nbconvert` as web service: Renders Jupyter notebooks as static web
    pages.

Installation
------------

#. The Notebook Viewer requires several binary packages that have to be
   installed on our system, for

.. tab:: Debian/Ubuntu

    .. code-block:: console

        $ sudo apt install libmemcached-dev libcurl4-openssl-dev pandoc libevent-dev

.. tab:: macOS

    .. code-block:: console

        $ brew install libmemcached openssl pandoc libevent

#. The Jupyter Notebook Viewer can then be installed in a new virtual
   environment with:

   .. code-block:: console

    $ mkdir nbviewer
    $ cd !$
    cd nbviewer

   .. note::
        The notebook app outputs the error ``AttributeError: module
        'tornado.gen' has no attribute 'Task'`` with current versions of
        `Tornado <https://www.tornadoweb.org/en/stable/>`_. This error does not
        occur with ``tornado<6.0``, , see also `Delete Terminal Not Working
        with Tornado version 6.0.1
        <https://github.com/jupyter/terminado/issues/62>`_:

        .. code-block:: console

            $ pipenv install "tornado<6.0"

   Now ``nbviewer`` can also be installed:

   .. code-block:: console

    $ pipenv install nbviewer

#. For testing, the server can be started with:

   .. code-block:: console

    $ pipenv run python -m nbviewer --debug --no-cache

Extending the Notebook Viewer
-----------------------------

The notebook viewer can be extended to include providers, see
`Extending the Notebook Viewer
<https://github.com/jupyter/nbviewer/tree/main#extending-the-notebook-viewer>`_.


Access control
--------------

If the viewer is run as :doc:`hub/nbviewer-service`, only users who have
authenticated themselves on the JupyterHub can access the nbviewer’s notebooks.
