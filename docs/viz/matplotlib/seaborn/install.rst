seaborn-Installation
====================

Mit :doc:`/productive/envs/spack/index` könnt ihr seaborn in eurem Kernel
bereitstellen, z.B. mit:

.. code-block:: console

    $ spack env activate python-374
    $ spack install py-seaborn ^python@3.7.4%gcc@9.1.0

Alternativ könnt ihr seaborn auch mit anderen Paketmanagern installieren, z.B.

.. code-block:: console

    $ pipenv install seaborn

.. note::
    Falls ihr pipenv noch nicht installiert habt, findet ihr eine Anleitung
    hierzu unter :ref:`pipenv-installieren`.

Die Installation könnt ihr überprüfen mit

.. code-block:: python

    >>> import seaborn as sns

