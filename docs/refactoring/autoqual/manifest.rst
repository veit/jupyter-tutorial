``check-manifest``
==================

`check-manifest <https://pypi.org/p/check-manifest>`_ ist ein Werkzeug, mit dem
ihr schnell überprüfen könnt, ob die Datei ``Manifest.in`` für Pyton-Pakete
vollständig ist. 

Installation
------------

.. code-block:: console

    $ pipenv install check-manifest

Überprüfen
----------

.. code-block:: console

    $ cd /path/to/MANIFEST.in
    $ pipenv run check-manifest

oder für eine automatische Aktualisierung

.. code-block:: console

    $ pipenv run check-manifest -uv
    listing source files under version control: 6 files and directories
    building an sdist: check-manifest-0.7.tar.gz: 4 files and directories
    lists of files in version control and sdist do not match!
    missing from sdist:
      tests.py
      tox.ini
    suggested MANIFEST.in rules:
      include *.py
      include tox.ini
    updating MANIFEST.in

    $ cat MANIFEST.in
    include *.rst

    # added by check_manifest.py
    include *.py
    include tox.ini

Konfiguration
-------------

Ihr könnt ``check-manifest`` so konfigurieren, dass bestimmte Dateimuster
ignoriert werden, indem ihr einen Abschnitt ``[tool.check-manifest]`` in eurer
``pyproject.toml``-Datei oder einen Abschnitt ``[check-manifest]`` in eurer
``setup.cfg`` oder ``tox.ini``-Datei anlegt, z.B.:

.. code-block:: yaml

    [tool.check-manifest]
    ignore = [".travis.yml"]

    # setup.cfg or tox.ini
    [check-manifest]
    ignore =
        .travis.yml

``check-manifest`` kennt die folgenden Optionen:

``ignore``
    Eine Liste von Dateinamenmustern, die von ``check-manifest`` ignoriert
    werden. Verwendet diese Option, wenn ihr Dateien in eurem
    Versionskontrollsystem behalten möchtet, die nicht in eurem
    Quelldistributionen enthalten sein sollen. Die Standardliste ist:

    .. code-block:: 

        PKG-INFO 
        * .egg-info 
        * .egg-info / * 
        setup.cfg 
        .hgtags 
        .hgsigs 
        .hgignore 
        .gitignore 
        .bzrignore 
        .gitattributes 
        .github / * 
        .travis.yml 
        Jenkinsfile 
        * .mo

``ignore-default-rules``
    wenn ``true``, dann ersetzen deine ``ignore``-Angaben die Standardliste,
    anstatt sie zu ergänzen.
``ignore-bad-ideas``
    Eine Liste von Dateinamenmustern, de von der Prüfung der generierten Dateien
    ignoriert werden. Damit könnt ihr generierte Dateien in eurem
    Versionskontrollsystem behalten, auch wenn dies üblicherweise eine schlechte
    Idee ist.

Integration in die Versionskontrolle
------------------------------------

Mit :doc:`pre-commit` kann `check-manifest` Teil eures Git-Workflows sein. Fügt
hierfür eurer `.pre-commit-config.yaml`-Datei folgendes hinzu:

.. code-block:: yaml

    repos:
    -   repo: https://github.com/mgedmin/check-manifest
        rev: "0.39"
        hooks:
        -   id: check-manifest

