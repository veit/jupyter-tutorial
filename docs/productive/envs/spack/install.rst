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

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install build-essential patch tar gzip bzip2 git gnupg2

.. tab:: macOS

   .. code-block:: console

      $ xcode-select --install
      $ brew install make bash gzip bzip2 git gnupg
      $ brew link gnupg

Installation
------------

To install Spack the repository is cloned and then changed from the `develop`
branch to the branch of the current release, in our case to `v0.17.1`:

.. code-block:: console

    $ git clone https://github.com/spack/spack.git
    Cloning into 'spack'...
    ...
    $ cd spack
    $ git switch v0.19

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
    zlib@1.2.13%gcc@11.3.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-sandybridge
    ==> Bootstrapping clingo from pre-built binaries
    ==> Fetching https://mirror.spack.io/bootstrap/github-actions/v0.4/build_cache/linux-centos7-x86_64-gcc-10.2.1-clingo-bootstrap-spack-idkenmhnscjlu5gjqhpcqa4h7o2a7aow.spec.json
    ==> Fetching https://mirror.spack.io/bootstrap/github-actions/v0.4/build_cache/linux-centos7-x86_64/gcc-10.2.1/clingo-bootstrap-spack/linux-centos7-x86_64-gcc-10.2.1-clingo-bootstrap-spack-idkenmhnscjlu5gjqhpcqa4h7o2a7aow.spack
    ==> Installing "clingo-bootstrap@spack%gcc@10.2.1~docs~ipo+python+static_libstdcpp build_type=Release arch=linux-centos7-x86_64" from a buildcache

.. note::
   When bootstrapping from pre-built binaries, Spack requires ``patchelf`` on
   Linux or ``otool`` on macOS. Otherwise Spack built it from sources and with a
   C++ compiler.

Bootstrap store
---------------

All tools Spack needs are installed in a separate store, which lives in the
:file:`${HOME}/.spack` directory. The software installed there can be queried
with:

.. code-block:: console

    $ spack find --bootstrap
    ==> Showing internal bootstrap store at "/srv/jupyter/.spack/bootstrap/store"
    ==> 3 installed packages
    -- linux-rhel5-x86_64 / gcc@9.3.0 -------------------------------
    clingo-bootstrap@spack  python@3.8

    -- linux-ubuntu20.04-sandybridge / gcc@9.3.0 --------------------
    patchelf@0.13

Compiler configuration
----------------------

.. code-block:: console

    $ spack compilers
     ==> Available compilers
     -- gcc ubuntu22.04-x86_64 ---------------------------------------
     gcc@11.3.0

Build your own compiler
-----------------------

.. code-block:: console

    $ spack install gcc
    ...
    ==> gcc: Successfully installed gcc-11.2.0-azhiay4ugfrs634hqlez7u3f2li3wvzd
      Fetch: 12.09s.  Build: 2h 8m 13.92s.  Total: 2h 8m 26.01s.
    [+] /Users/veit/spack/opt/spack/darwin-bigsur-cannonlake/apple-clang-13.0.0/gcc-11.2.0-azhiay4ugfrs634hqlez7u3f2li3wvzd

However, Spack doesn’t find the compiler at first:

.. code-block:: console

    $ spack compilers
    ==> Available compilers
    -- gcc ubuntu20.04-x86_64 ---------------------------------------
    gcc@9.3.0

Now, you can add the compiler with ``spack compiler find``:

.. code-block:: console

    $ spack compiler find /srv/jupyter/spack/opt/spack/linux-ubuntu22.04-sandybridge/gcc-11.3.0/gcc-12.2.0-gbaw464qxjuz6i3uud42cd5mb4xujxia/
     ==> Added 1 new compiler to /srv/jupyter/.spack/linux/compilers.yaml
         gcc@12.2.0
     ==> Compilers are defined in the following files:
         /srv/jupyter/.spack/linux/compilers.yaml

``spack compilers`` should now also find the newly installed compiler:

.. code-block:: console

    $ spack compilers
     ==> Available compilers
     -- gcc ubuntu22.04-x86_64 ---------------------------------------
     gcc@12.2.0  gcc@11.3.0

If you want to overwrite the default and site settings, you can edit
:file:`${HOME}/.spack/packages.yaml`:

.. code-block:: yaml

    packages:
      all:
        compiler: [gcc@12.2.0]

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
