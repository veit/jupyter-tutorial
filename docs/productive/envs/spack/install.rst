Spack installation
==================

Requirements
------------

* Python 2 or Python 3
* C/C++ compiler
* ``git`` and ``curl``

  For Linux:

  .. code-block:: console

    $ apt install curl git environment-modules

  … or for macOS:

  .. code-block:: console

    $ brew install curl git modules

  Then the shell is configured by entering for example the following in the Bash
  configuration:

  .. code-block:: console

    $ source /usr/local/opt/modules/init/bash

* ``gnupg2`` for the ``gpg`` subcommand

Installation
------------

.. code-block:: console

    $ git clone https://github.com/spack/spack.git
    Cloning into 'spack'...
    ...

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

Checking the installation
-------------------------

.. code-block:: console

    $ spack spec python
    Input spec
    --------------------------------
    python

    Concretized
    --------------------------------
    python@3.7.6%gcc@7.4.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4~uuid+zlib arch=linux-ubuntu18.04-sandybridge
        ^bzip2@1.0.8%gcc@7.4.0+shared arch=linux-ubuntu18.04-sandybridge
            ^diffutils@3.7%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
                ^libiconv@1.16%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
        ^expat@2.2.9%gcc@7.4.0+libbsd arch=linux-ubuntu18.04-sandybridge
            ^libbsd@0.10.0%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
        ^gdbm@1.18.1%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
            ^readline@8.0%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
                ^ncurses@6.1%gcc@7.4.0~symlinks+termlib arch=linux-ubuntu18.04-sandybridge
                    ^pkgconf@1.6.3%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
        ^gettext@0.20.1%gcc@7.4.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=linux-ubuntu18.04-sandybridge
            ^libxml2@2.9.9%gcc@7.4.0~python arch=linux-ubuntu18.04-sandybridge
                ^xz@5.2.4%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
                ^zlib@1.2.11%gcc@7.4.0+optimize+pic+shared arch=linux-ubuntu18.04-sandybridge
            ^tar@1.32%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
        ^libffi@3.2.1%gcc@7.4.0 arch=linux-ubuntu18.04-sandybridge
        ^openssl@1.1.1d%gcc@7.4.0+systemcerts arch=linux-ubuntu18.04-sandybridge
            ^perl@5.30.1%gcc@7.4.0+cpanm+shared+threads arch=linux-ubuntu18.04-sandybridge
        ^sqlite@3.30.1%gcc@7.4.0~column_metadata+fts~functions~rtree arch=linux-ubuntu18.04-sandybridge

Compiler configuration
----------------------

.. code-block:: console

    $ spack compilers
    ==> Available compilers
    -- clang mojave-x86_64 ------------------------------------------
    clang@10.0.1-apple

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
