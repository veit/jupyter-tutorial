Spack-Installation
==================

Anforderungen
-------------

* Python 2 oder Python 3
* C/C++ compiler
* ``git`` und ``curl``

  Für Linux:

  .. code-block:: console

    $ apt install curl git environment-modules

  … oder für Mac OS X:

  .. code-block:: console

    $ brew install curl git modules

* ``gnupg2`` für ``gpg``-Subcommand

Installation
------------

.. code-block:: console

    $ git clone https://github.com/spack/spack.git
    Cloning into 'spack'...
    …

Shell konfigurieren
-------------------

#. Zur Konfiguration des Bash-Environment wird folgendes in ``~/.bashrc``
   eingetragen:

   .. code-block:: console

    export SPACK_ROOT=~/spack
    . $SPACK_ROOT/share/spack/setup-env.sh

#. Die geänderte Konfiguration wird nun übernommen mit

   .. code-block:: console

    $ source ~/.bashrc 

Überprüfen der Installation
---------------------------

.. code-block:: console

    $ spack spec netcdf
    Input spec
    --------------------------------
    netcdf

    Concretized
    --------------------------------
    netcdf@4.7.0%clang@10.0.1-apple~dap~hdf4 maxdims=1024 maxvars=8192 +mpi~parallel-netcdf patches=10a1c3f7fa05e2c82457482e272bbe04d66d0047b237ad0a73e87d63d848b16c +pic+shared arch=darwin-mojave-x86_64
        ^autoconf@2.69%clang@10.0.1-apple arch=darwin-mojave-x86_64
            ^m4@1.4.18%clang@10.0.1-apple patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 +sigsegv arch=darwin-mojave-x86_64
                ^libsigsegv@2.11%clang@10.0.1-apple arch=darwin-mojave-x86_64
            ^perl@5.26.2%clang@10.0.1-apple+cpanm patches=0eac10ed90aeb0459ad8851f88081d439a4e41978e586ec743069e8b059370ac +shared+threads arch=darwin-mojave-x86_64
                ^gdbm@1.18.1%clang@10.0.1-apple arch=darwin-mojave-x86_64
                    ^readline@7.0%clang@10.0.1-apple arch=darwin-mojave-x86_64
                        ^ncurses@6.1%clang@10.0.1-apple~symlinks~termlib arch=darwin-mojave-x86_64
                            ^pkgconf@1.6.1%clang@10.0.1-apple arch=darwin-mojave-x86_64
        ^automake@1.16.1%clang@10.0.1-apple arch=darwin-mojave-x86_64
        ^hdf5@1.10.5%clang@10.0.1-apple~cxx~debug~fortran+hl+mpi+pic+shared~szip~threadsafe arch=darwin-mojave-x86_64
            ^openmpi@3.1.4%clang@10.0.1-apple~cuda+cxx_exceptions fabrics=none ~java~legacylaunchers~memchecker~pmi schedulers=none ~sqlite3~thread_multiple+vt arch=darwin-mojave-x86_64
                ^hwloc@1.11.11%clang@10.0.1-apple~cairo~cuda~gl+libxml2~nvml~pci+shared arch=darwin-mojave-x86_64
                    ^libxml2@2.9.9%clang@10.0.1-apple~python arch=darwin-mojave-x86_64
                        ^libiconv@1.15%clang@10.0.1-apple arch=darwin-mojave-x86_64
                        ^xz@5.2.4%clang@10.0.1-apple arch=darwin-mojave-x86_64
                        ^zlib@1.2.11%clang@10.0.1-apple+optimize+pic+shared arch=darwin-mojave-x86_64
        ^libtool@2.4.6%clang@10.0.1-apple arch=darwin-mojave-x86_64

Compiler-Konfiguration
----------------------

.. code-block:: console

    $ spack compilers
    ==> Available compilers
    -- clang mojave-x86_64 ------------------------------------------
    clang@10.0.1-apple

GPG Signing
-----------

Spack unterstützt das Signieren und Verifizieren von Paketen mit
GPG-Schlüsseln. Für Spack wird ein separater Schlüsselring verwendet, weswegen
keine Schlüssel aus dem Home-Verzeichnis von Nutzern verfügbar sind.

Wenn Spack zum ersten Mal installiert wird, ist dieser Schlüsselring leer.
Die in ``/var/spack/gpg`` gespeicherten Schlüssel sind die Standardschlüssel
für eine Spack-Installation. Diese Schlüssel werden durch ``spack gpg init``
importiert. Dadurch werden die Standardschlüssel als vertrauenswürdige Schlüssel
in den Schlüsselbund importiert.

Schlüsseln vertrauen
~~~~~~~~~~~~~~~~~~~~

Zusätzliche Schlüssel können dem Schlüsselring hinzugefügt werden mit
``spack gpg trust <keyfile>``. Sobald ein Schlüssel vertrauenswürdig ist,
können Pakete, die vom Besitzer dieses Schlüssels signiert wurden, installiert
werden.

Schlüssel erstellen
~~~~~~~~~~~~~~~~~~~

Ihr könnt auch eigene Schlüssel erstellen um eure eigenen Pakete signieren
zu können mit

.. code-block:: console

    $ spack gpg export <location> [<key>…] 

Schlüssel auflisten
~~~~~~~~~~~~~~~~~~~

Die im Schlüsselbund verfügbaren Schlüssel können aufgelistet werden mit

.. code-block:: console

    $ spack gpg list

Schlüssel entfernen
~~~~~~~~~~~~~~~~~~~

Schlüssel können entfernt werden mit

.. code-block:: console

    $ spack gpg untrust <keyid>

Schlüssel-IDs können E-Mail-Adressen, Namen oder Fingerprints sein.

