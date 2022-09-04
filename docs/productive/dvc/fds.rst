FastDS
======

`FastDS <https://dagshub.com/pages/fds>`_ is an open source tool that combines
:doc:`Git <../git/index>` and :doc:`DVC <index>` to allow easy versioning of
code and data.

Installation
------------

FastDS can be easily installed with:

.. code-block:: console

    $ pipenv install fastds

Introduction
------------

Even the creation of the initial repository is greatly simplified:

.. code-block:: console

    $ git init
    $ dvc init
    $ git add .
    $ dvc add data/data.xml
    $ git add data/.gitignore data/data.xml.dvc
    $ git commit -m "Initial commit"
    $ dvc push -r origin
    $ git push origin

becomes:

.. code-block:: console

    $ fds init
    $ fds add .
    $ fds save -m "Initial commit"

FastDS abbreviates Git and DVC commands to minimise input errors and automate
repetitive tasks:

``init``
    initialises both the Git and DVC repositories.
``status``
    returns the status of both repositories.
``add``
    adds files to the Git or DVC repository.
``commit``
    commits changes to the Git or DVC repository.
``clone``
    clones the Git repository and fetches data from the remote DVC repository.
``push``
    pushes data to the remote Git and DVC repositories.
``save``
    adds changes to the project and commits them to the remote Git and DVC
    repositories.
