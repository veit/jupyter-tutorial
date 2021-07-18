Manage data with ``DVC``
========================

For data analysis, and especially machine learning, it is extremely valuable to
be able to reproduce different versions of analyses that have been carried out
with different data sets and parameters. However, in order to obtain
reproducible analyses, both the data and the model (including the algorithms,
parameters, etc.) must be versioned. Versioning data for reproducible analysis
is a bigger problem than versioning models because of the size of the data.
Tools like `DVC <https://dvc.org/>`_ help manage data by allowing users to
transfer it to a remote data store using a :doc:`Git <../git/index>` like
workflow. This simplifies the retrieval of certain versions of data in order to
reproduce an analysis.

DVC was developed to be able to use ML models and data sets together and to
manage them in a comprehensible manner. It works with different version
managements, but does not need them. In contrast to `DataLad
<https://www.datalad.org/>`_/`git-annex <https://git-annex.branchable.com/>`_,
for example, it is not limited to Git as version management, but can also be
used together with Mercurial, see `github.com/crobarcro/dvc/dvc/scm.py
<https://github.com/crobarcro/dvc/blob/master/dvc/scm.py>`_. It also uses its
own system for storing files with support for SSH and HDFS, among others.

DataLad, on the other hand, focuses more on discovering and consuming datasets,
which are then easily managed with Git. DVC, on the other hand, stores each step
in the pipeline in a separate ``.dvc`` file that can then be managed by Git.

These ``.dvc`` files, however, allow practical tools for manipulating and
visualizing DAGs, see, for example, :doc:`visualisation of DAGs
<pipeline>`.

External dependencies can also be specified with :ref:`dvc remote <dvc-remote>`.

.. seealso::
   * `Tutorial <https://dvc.org/doc/tutorial>`_
   * `Documentation <https://dvc.org/doc>`_
   * `Git Repository <https://github.com/iterative/dvc>`_

Installation
------------

Finally, external dependencies can also be specified with Pipenv.

.. note::
   You have to explicitly state the extras. This can be ``[ssh]``, ``[s3]``,
   ``[gs]``, ``[azure]``, and ``[oss]`` or ``[all]``. For ``ssh`` the command
   looks like this:

   .. code-block:: console

        $ pipenv install dvc[ssh]

Alternatively, DVC can also be installed via the package management of
Ubuntu/Debian with:

.. code-block:: console

    $ sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list
    $ sudo apt update
    $ sudo apt install dvc

For macOS DVC can be installed with:

.. code-block:: console

    $ brew install iterative/homebrew-dvc/dvc

.. note::
    The following example was created with a current DVC version (1.0.0a9),
    which partly uses a different syntax than earlier versions. You can
    currently (8th June 2020) only install this with pip:

     .. code-block:: console

        $ pipenv install dvc[all]==1.0.0a9

.. toctree::
    :hidden:

    init
    pipeline
    params
    metrics
    dag
    reproduce
    integration
