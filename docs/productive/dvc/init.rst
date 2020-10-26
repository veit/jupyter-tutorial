Create a project
================

DVC can be easily initialised with:

.. code-block:: console

    $ mkdir -p dvc-example/data
    $ cd dvc-example
    $ git init
    $ dvc init
    $ git add .dvc
    $ git commit -m "Initialise DVC"

``dvc init``
    creates a directory ``.dvc/`` with ``config``, ``.gitignore`` and
    ``cache`` directory.
``git commit``
    puts ``.dvc/config`` and ``.dvc/.gitignore`` under version control.

Configure
---------

.. _dvc-remote:

Before DVC is used, even a remote storage is established. This should be
accessible to everyone who should access the data or the model. It’s similar to
using a Git server. Often, however, this is also an NFS mount, which can be
integrated as follows, for example:

.. code-block:: console

    $ sudo mkdir -p /var/dvc-storage
    $ dvc remote add -d local /var/dvc-storage
    Setting 'local' as a default remote.
    $ git commit .dvc/config -m "Configure local remote"
    [master efaeb84] Configure local remote
     1 file changed, 4 insertions(+)

``-d``, ``--default``
    Default value for the space removed
``local``
    Name of the remote location
``/var/dvc-storage``
    URL of the remote location

    In addition, other protocols are supported, which are preceded by the path,
    including ``ssh:``, ``hdfs:`` and ``https:``.

Another remote data storage can simply be added, e.g. with:

.. code-block:: console

    $ dvc remote add webserver https://dvc.example.org/myproject

The associated configuration file ``.dvc/config`` looks like this:

.. code-block:: ini

    ['remote "local"']
    url = /var/dvc-storage
    [core]
    remote = local
    ['remote "webserver"']
    url = https://dvc.example.org/myproject

Add data and directories
------------------------

With DVC you can save and version files, ML models, directories and intermediate
results with Git without having to check the file content into Git:

.. code-block:: console

    $ dvc get https://github.com/iterative/dataset-registry get-started/data.xml \
        -o data/data.xml
    $ dvc add data/data.xml

This will add the file ``data/data.xml`` in ``data/.gitignore`` and write the
meta information in ``data/data.xml.dvc``. Further information on the file
format of the ``*.dvc`` can be found under `DVC-File Format
<https://dvc.org/doc/user-guide/dvc-file-format>`_.

In order to be able to manage different versions of your project data with Git,
you only have to add the CVS file:

.. code-block:: console

    $ git add data/.gitignore data/fortune500.csv.dvc
    $ git commit -m "Add raw data to project"

Store and retrieve data
-----------------------

The data can be copied from the working directory of your Git repository to the
remote storage space with

.. code-block:: console

    $ dvc push

If you want to call up more current data, you can do so with

.. code-block:: console

    $ dvc pull

Import and update
-----------------

You can also import data and models from another project with the command ``dvc
import``, e.g.:

.. code-block:: console

    $ dvc import https://github.com/iterative/dataset-registry  get-started/data.xml
    Importing 'get-started/data.xml (https://github.com/iterative/dataset-registry)' -> 'data.xml'

This loads the file from the `dataset-registry
<https://github.com/iterative/dataset-registry>`_ into the current working
directory, adds ``.gitignore`` and creates ``data.xml.dvc``.

With ``dvc update`` we can update these data sources before we reproduce a
pipeline that depends on these data sources,  e.g.

.. code-block:: console

    $ dvc update data.xml.dvc
    Stage 'data.xml.dvc' didn't change.
    Saving information to 'data.xml.dvc'.
