Spack-Installation
==================

Anforderungen
-------------

* Python 2 oder Python 3
* C/C++ compiler
* ``git`` und ``curl``
* ``gnupg2`` für ``gpg``-Subcommand

.. code-block:: console

    $ apt install curl git environment-modules

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

    export SPACK_ROOT=/srv/jupyter/spack
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
    netcdf@4.6.3%gcc@6.3.0~dap~hdf4 maxdims=1024 maxvars=8192 +mpi~parallel-netcdf+pic+shared arch=linux-debian9-x86_64
        ^hdf5@1.10.5%gcc@6.3.0~cxx~debug~fortran+hl+mpi+pic+shared~szip~threadsafe arch=linux-debian9-x86_64
            ^openmpi@3.1.3%gcc@6.3.0~cuda+cxx_exceptions fabrics=auto ~java~legacylaunchers~memchecker~pmi schedulers=auto ~sqlite3~thread_multiple+vt arch=linux-debian9-x86_64
                ^hwloc@1.11.11%gcc@6.3.0~cairo~cuda~gl+libxml2~nvml+pci+shared arch=linux-debian9-x86_64
                    ^libpciaccess@0.13.5%gcc@6.3.0 arch=linux-debian9-x86_64
                        ^libtool@2.4.6%gcc@6.3.0 arch=linux-debian9-x86_64
                            ^m4@1.4.18%gcc@6.3.0 patches=3877ab548f88597ab2327a2230ee048d2d07ace1062efe81fc92e91b7f39cd00,c0a408fbffb7255fcc75e26bd8edab116fc81d216bfd18b473668b7739a4158e,fc9b61654a3ba1a8d6cd78ce087e7c96366c290bc8d2c299f09828d793b853c8 +sigsegv arch=linux-debian9-x86_64
                                ^libsigsegv@2.11%gcc@6.3.0 arch=linux-debian9-x86_64
                        ^pkgconf@1.6.0%gcc@6.3.0 arch=linux-debian9-x86_64
                        ^util-macros@1.19.1%gcc@6.3.0 arch=linux-debian9-x86_64
                    ^libxml2@2.9.8%gcc@6.3.0~python arch=linux-debian9-x86_64
                        ^libiconv@1.15%gcc@6.3.0 arch=linux-debian9-x86_64
                        ^xz@5.2.4%gcc@6.3.0 arch=linux-debian9-x86_64
                        ^zlib@1.2.11%gcc@6.3.0+optimize+pic+shared arch=linux-debian9-x86_64
                    ^numactl@2.0.12%gcc@6.3.0 arch=linux-debian9-x86_64
                        ^autoconf@2.69%gcc@6.3.0 arch=linux-debian9-x86_64
                            ^perl@5.26.2%gcc@6.3.0+cpanm patches=0eac10ed90aeb0459ad8851f88081d439a4e41978e586ec743069e8b059370ac +shared+threads arch=linux-debian9-x86_64
                                ^gdbm@1.18.1%gcc@6.3.0 arch=linux-debian9-x86_64
                                    ^readline@7.0%gcc@6.3.0 arch=linux-debian9-x86_64
                                        ^ncurses@6.1%gcc@6.3.0~symlinks~termlib arch=linux-debian9-x86_64
                        ^automake@1.16.1%gcc@6.3.0 arch=linux-debian9-x86_64


Compiler-Konfiguration
----------------------

.. code-block:: console

    $ spack compilers
    ==> Available compilers
    -- gcc debian9-x86_64 -------------------------------------------
    gcc@6.3.0

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

