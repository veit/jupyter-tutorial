Spack-Überblick
===============

Modellierungs- und Simulationsumgebungen sind sehr heterogen. Spack unterstützt
daher viele verschiedene Produktionsumgebungen:

* 7 verschiedene Compiler: Intel, GCC, Clang, PGI, …
* Auflösen von Abhängigkeiten
* Auflösen verschiedener Versionen von Abhängigkeiten

Bisherige Systeme
-----------------

Sie bieten meist keine Unterstützung für kombinatorische Versionierung.

* Traditionelle Binärpaketmanager wie RPM, yum, APT, yast, etc.

    * sind konzipiert um einen einzelnen Software-Stack zu verwalten
    * installieren eine Version eines Pakets
    * üblicherweise problemlose Upgrades auf einen stabilen, gut getesteten
      Stack

* Port-Systeme

    * BSD Ports, portage, NixOS, Macports, Homebrew, etc.
    * meist kaum Unterstützung für Builds, die parametrisiert sind durch
      Compiler oder abhängige Versionen

* Virtuelle Maschinen und Linux-Container

    * Container erlauben die Erstellung unterschiedlicher Umgebungen für
      unterschiedliche Anwendungen
    * Sie lösen jedoch nicht das Build-Problem für das Image
    * Performance, Security und Upgrades werden bei vielen unterschiedlichen
      Builds sehr aufwändig.

.. toctree::
    :hidden:

    combinatorial-builds
    build-automatisation
    usecase1
    usecase2
    future

