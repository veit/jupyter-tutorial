Use Case 1: Verwalten kombinatorischer Installationen
=====================================================

Anzeige aller installierten Konfigurationen
-------------------------------------------

.. code-block:: console

    $ spack find
    ==> 103 installed packages.
    -- linux-x86_64 / gcc@4.8.2 --------------------------------
    gdk-pixbuf@2.31.2   libpng@1.6.16        otf2@1.4            qhull@1.0
    adept-utils@1.0.1   boost@1.55.0         cmake@5.6-special   libdwarf@20130729   mpich@3.0.4
    adept-utils@1.0.1   cmake@5.6 dyninst@8.1.2 libelf@0.8.13 openmpi@1.8.2
    -- linux-x86_64 / intel@14.0.2 -----------------------------
    hwloc@1.9           mpich@3.0.4          starpu@1.1.4
    -- linux-x86_64 / intel@15.0.0 -----------------------------
    adept-utils@1.0.1   boost@1.55.0         libdwarf@20130729   libelf@0.8.13       mpich@3.0.4
    -- linux-x86_64 / intel@15.0.1 -----------------------------
    adept-utils@1.0.1   callpath@1.0.2       libdwarf@20130729   mpich@3.0.4
    boost@1.55.0        hwloc@1.9            libelf@0.8.13       starpu@1.1.4


* ``spack find`` zeigt alle installierten Konfigurationen
* Dabei kann es auch verschiedene Versionen desselben Pakets geben
* Pakete werden differenziert zwischen Architektur und Compiler
* Spack generiert ebenfalls ``modulefiles``, diese müssen jedoch nicht genutzt
  werden

Spack-Syntax zum Einschränken der Anfragen
------------------------------------------

.. code-block:: console

    $ spack find mpich
    ==> 5 installed packages.
    -- linux-x86_64 / gcc@4.4.7 --------------------------------
    mpich@3.0.4
    -- linux-x86_64 / gcc@4.8.2 --------------------------------
    mpich@3.0.4
    -- linux-x86_64 / intel@14.0.2 -----------------------------
    mpich@3.0.4

.. code-block:: console

    $ spack find libelf %intel
    -- linux-x86_64 / intel@15.0.0 ------
    libelf@0.8.13
    -- linux-x86_64 / intel@15.0.1 ------
    libelf@0.8.13

.. code-block:: console

    $ spack find libelf %intel@15.0.1
    -- linux-x86_64 / intel@15.0.1 ------
    libelf@0.8.13

Spack-Syntax zum Anzeigen der Abhängigkeiten
--------------------------------------------

.. code-block:: console

    $ spack find callpath
    ==> 2 installed packages.
    -- linux-x86_64 / clang@3.4 ————————    -- linux-x86_64 / gcc@4.9.2 -------------
    callpath@1.0.2                          callpath@1.0.2

.. code-block:: console

    $ spack find -dl callpath
    ==> 2 installed packages.
    -- linux-x86_64 / clang@3.4 -----------    -- linux-x86_64 / gcc@4.9.2 -----------
    xv2clz2    callpath@1.0.2                  udltshs callpath@1.0.2
    ckjazss        ^adept-utils@1.0.1          rfsu7fb ^adept-utils@1.0.1
    3ws43m4        ^boost@1.59.0               ybet64y ^boost@1.55.0
    ft7znm6        ^mpich@3.1.4                aa4ar6i ^mpich@3.1.4
    qqnuet3        ^dyninst@8.2.1              tmnnge5 ^dyninst@8.2.1
    3ws43m4        ^boost@1.59.0               ybet64y ^boost@1.55.0
    g65rdud        ^libdwarf@20130729          g2mxrl2 ^libdwarf@20130729
    cj5p5fk        ^libelf@0.8.13              ynpai3j ^libelf@0.8.13
    cj5p5fk        ^libelf@0.8.13              ynpai3j ^libelf@0.8.13
    g65rdud        ^libdwarf@20130729          g2mxrl2 ^libdwarf@20130729
    cj5p5fk        ^libelf@0.8.13              ynpai3j ^libelf@0.8.13
    cj5p5fk        ^libelf@0.8.13              ynpai3j ^libelf@0.8.13
    ft7znm6        ^mpich@3.1.4                aa4ar6i ^mpich@3.1.4

