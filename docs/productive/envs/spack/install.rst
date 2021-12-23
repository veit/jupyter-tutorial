Spack installation
==================

Requirements
------------

* Interpreter for Spack:

  * Python 2.7 or Python 3.5–3.9

* Building software

  * C/C++ compilers
  * ``make``,  ``patch`` and ``bash``

* Create and extract archives

  * ``tar``, ``gzip`` and ``bzip``

* Manage software repositories

  * ``git``

* Sign and verify Build caches

  * ``gnupg2``

… for Debian/Ubuntu:

.. code-block:: console

    $ sudo apt install build-essential patch tar gzip bzip2 git gnupg2

… or for macOS:

.. code-block:: console

    $ xcode-select --install
    $ brew install make bash gzip bzip2 git gnupg
    $ brew link gnupg

Installation
------------

.. code-block:: console

    $ git clone https://github.com/spack/spack.git
    Cloning into 'spack'...
    ...
    $ cd spack
    $ $ git checkout releases/v0.17

Configure the shell
-------------------

#. To configure the bash environment, the following is entered in the
   ``~/.bashrc``:

   .. code-block:: bash

    export SPACK_ROOT=~/spack
    . $SPACK_ROOT/share/spack/setup-env.sh

#. The changed configuration is read with

   .. code-block:: console

    $ source ~/.bashrc

Bootstrapping ``clingo``
------------------------

Spack uses `clingo <https://potassco.org/clingo/>`_ to resolve optimal versions
and variants of dependencies when installing packages. To install clingo from
pre-built binaries you can simply specify a package:

.. code-block:: console

    $ spack spec zlib
    Input spec
    --------------------------------
    zlib

    Concretized
    --------------------------------
    ==> Bootstrapping clingo from pre-built binaries
    ==> Fetching https://mirror.spack.io/bootstrap/github-actions/v0.1/build_cache/darwin-catalina-x86_64/apple-clang-12.0.0/clingo-bootstrap-spack/darwin-catalina-x86_64-apple-clang-12.0.0-clingo-bootstrap-spack-omsvlh5v6fi2saw5qyqvzsbvqpvrf5yw.spack
    ==> Installing "clingo-bootstrap@spack%apple-clang@12.0.0~docs~ipo+python build_type=Release arch=darwin-catalina-x86_64" from a buildcache
    zlib@1.2.11%apple-clang@13.0.0+optimize+pic+shared arch=darwin-bigsur-cannonlake


.. note::
   When bootstrapping from pre-built binaries, Spack requires ``patchelf`` on
   Linux or ``otool`` on macOS. Otherwise Spack built it from sources and with a
   C++ compiler.

Compiler configuration
----------------------

.. code-block:: console

    $ $ spack compilers
    ==> Available compilers
    -- apple-clang bigsur-x86_64 ------------------------------------
    apple-clang@13.0.0

GPG signing
-----------

Spack supports the signing and verification of packages with GPG keys. A
separate key ring is used for Spack, why no keys are available from users’ home
directories.

When Spack is first installed, this key ring will be empty. The keys stored in
``/var/spack/gpg`` are the standard keys for a Spack installation. These keys
are imported by ``spack gpg init``. This will import the standard keys into the
keyring as trusted keys.

Trust keys
~~~~~~~~~~

Additional keys can be added to the key ring using ``spack gpg trust
<keyfile>``. Once a key is trusted, packages signed by the owner of that key can
be installed.

Create a key
~~~~~~~~~~~~

You can also create your own keys to be able to sign your own packages with

.. code-block:: console

    $ spack gpg export <location> [<key>…]

List keys
~~~~~~~~~

The keys available in the keyring can be listed with

.. code-block:: console

    $ spack gpg list

Remove a key
~~~~~~~~~~~~

Keys can be removed with

.. code-block:: console

    $ spack gpg untrust <keyid>

Key IDs can be email addresses, names or fingerprints.
