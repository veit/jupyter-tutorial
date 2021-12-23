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

    $ brew install libc++ make bash gzip bzip2 git gnupg
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

Checking the installation
-------------------------

.. code-block:: console

    $ spack spec python
    Input spec
    --------------------------------
    python

    Concretized
    --------------------------------
    python@3.8.12%apple-clang@13.0.0+bz2+ctypes+dbm~debug+libxml2+lzma~nis~optimizations+pic+pyexpat+pythoncmd+readline+shared+sqlite3+ssl~tix~tkinter~ucs4+uuid+zlib patches=0d98e93189bc278fbc37a50ed7f183bd8aaf249a8e1670a465f0db6bb4f8cf87,4c2457325f2b608b1b6a2c63087df8c26e07db3e3d493caf36a56f0ecf6fb768,f2fd060afc4b4618fe8104c4c5d771f36dc55b1db5a4623785a4ea707ec72fb4 arch=darwin-bigsur-cannonlake
        ^apple-libuuid@1353.100.2%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
        ^bzip2@1.0.8%apple-clang@13.0.0~debug~pic+shared arch=darwin-bigsur-cannonlake
            ^diffutils@3.8%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
                ^libiconv@1.16%apple-clang@13.0.0 libs=shared,static arch=darwin-bigsur-cannonlake
        ^expat@2.4.1%apple-clang@13.0.0~libbsd arch=darwin-bigsur-cannonlake
        ^gdbm@1.19%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
            ^readline@8.1%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
                ^ncurses@6.2%apple-clang@13.0.0~symlinks+termlib abi=none arch=darwin-bigsur-cannonlake
                    ^pkgconf@1.8.0%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
        ^gettext@0.21%apple-clang@13.0.0+bzip2+curses+git~libunistring+libxml2+tar+xz arch=darwin-bigsur-cannonlake
            ^libxml2@2.9.12%apple-clang@13.0.0~python arch=darwin-bigsur-cannonlake
                ^xz@5.2.5%apple-clang@13.0.0~pic libs=shared,static arch=darwin-bigsur-cannonlake
                ^zlib@1.2.11%apple-clang@13.0.0+optimize+pic+shared arch=darwin-bigsur-cannonlake
            ^tar@1.34%apple-clang@13.0.0 arch=darwin-bigsur-cannonlake
        ^libffi@3.3%apple-clang@13.0.0 patches=26f26c6f29a7ce9bf370ad3ab2610f99365b4bdd7b82e7c31df41a3370d685c0 arch=darwin-bigsur-cannonlake
        ^openssl@1.1.1l%apple-clang@13.0.0~docs certs=system arch=darwin-bigsur-cannonlake
            ^perl@5.34.0%apple-clang@13.0.0+cpanm+shared+threads arch=darwin-bigsur-cannonlake
                ^berkeley-db@18.1.40%apple-clang@13.0.0+cxx~docs+stl patches=b231fcc4d5cff05e5c3a4814f6a5af0e9a966428dc2176540d2c05aff41de522 arch=darwin-bigsur-cannonlake
        ^sqlite@3.36.0%apple-clang@13.0.0+column_metadata+fts~functions~rtree arch=darwin-bigsur-cannonlake

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
