Jupyter Notebook Viewer
=======================

`nbviewer <https://github.com/jupyter/nbviewer>`_
    :doc:`nbconvert` als Web-Service: Rendert Jupyter Notebooks als statische
    Webseiten.

Installation
------------

#. Der Notebook Viewer benötigt mehrere Binärpakete, die auf unserem System
   installiert werden müssen,

   für Ubuntu und Debian:

   .. code-block:: console

    $ sudo apt install libmemcached-dev libcurl4-openssl-dev pandoc libevent-dev

   für Mac OSX:

   .. code-block:: console

    $ brew install libmemcached openssl pandoc libevent

#. Anschließend kann der Jupyter Notebook Viewer in einem neuen virtuellen
   Umgebung installiert werden mit:

   .. code-block:: console

    $ mkdir nbviewer
    $ cd !$
    cd nbviewer

   .. note::
        Die Notebook-App gibt bei aktuellen Versionen von `Tornado
        <https://www.tornadoweb.org/en/stable/>`_ den Fehler ``AttributeError:
        module 'tornado.gen' has no attribute 'Task'`` aus. Mit ``tornado<6.0``
        tritt dieser Fehler jedoch nicht auf, s.a. `Delete Terminal Not Working
        with Tornado version 6.0.1
        <https://github.com/jupyter/terminado/issues/62>`_:

        .. code-block:: console

            $ pipenv install "tornado<6.0"

    Anschließend kann dann auch ``nbviewer`` installiert werden:

    .. code-block:: console

        $ pipenv install nbviewer

#. Zum Testen kann der Server gestartet werden mit:

   .. code-block:: console

    $ pipenv run python -m nbviewer --debug --no-cache

Erweitern des Notebook-Viewers
------------------------------

Der Notebook-Viewer lässt sich um Provider erweitern, s.
`Extending the Notebook Viewer
<https://github.com/jupyter/nbviewer#extending-the-notebook-viewer>`_.


Zugriffsbeschränkung
--------------------

Wenn der Viewer als :doc:`jupyterhub/nbviewer-service` ausgeführt wird, können nur Benutzer, die
sich am JupyterHub authentifiziert haben, auf die Notebooks des nbviewer
zugreifen.

