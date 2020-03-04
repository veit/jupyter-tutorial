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

  Anschließend wird die Shell konfiguriert indem z.B. für die Bash folgendes in
  die Bash-Konfiguration eingetragen wird:

  .. code-block:: console

    $ source /usr/local/opt/modules/init/bash

* ``gnupg2`` für ``gpg``-Subcommand

Installation
------------

.. code-block:: console

    $ git clone https://github.com/spack/spack.git
    Cloning into 'spack'...
    ...

Shell konfigurieren
-------------------

#. Zur Konfiguration des Bash-Environment wird folgendes in ``~/.bashrc``
   eingetragen:

   .. code-block:: bash

    export SPACK_ROOT=~/spack
    . $SPACK_ROOT/share/spack/setup-env.sh

#. Die geänderte Konfiguration wird nun übernommen mit

   .. code-block:: console

    $ source ~/.bashrc 

Überprüfen der Installation
---------------------------

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

