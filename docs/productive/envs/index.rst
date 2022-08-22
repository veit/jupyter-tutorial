Reproduce environments
======================

Reproducible and secure Python environments are difficult to ensure. With
the Python package manager :term:`pip`, the call would look like this:

.. code-block:: console

    $ python -m pip install --no-deps --require-hashes ----only-binary=:all:

Dedicated environments (for example with :doc:`pipenv/index`, :doc:`devpi` and
:doc:`Spack <spack/index>` simplify this if you save the file with ther
specifications, for example ``Pipfile``, ``Pipfile.lock``, ``package-lock.json``
:abbr:`etc (et cetera)`. In this way, you and others can reproduce the
environments.

.. toctree::
    :hidden:

    spack/index
    pipenv/index
    devpi
    glossary
