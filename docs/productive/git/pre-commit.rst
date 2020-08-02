Git pre-commit Hooks
====================

`pre-commit <http://pre-commit.com/>`_ ist ein Framework zum Verwalten und
Pflegen mehrsprachiger pre-commit-Hooks.

Eine wesentliche Aufgabe ist es, dem gesamten Entwicklungsteam dieselben Skripte
zur Verfügung zu stellen. `pre-commit <http://pre-commit.com/>`_ von yelp
verwaltet solche pre-commit-Hooks und verteilt sie auf verschiedene Projekte und
Entwickler.

Git pre-commit Hooks werden meist verwendet um vor Code Reviews automatisch auf
Probleme im Code hinzuweisen, z.B. um die Formattierung zu überprüfen oder
Debug-Anweisungen zu finden. Pre-Commit vereinfacht das projektübergreifende
Teilen vom Pre-Commit-Hooks. Dabei ist auch die Sprache, in der z.B. ein Linter
geschrieben wurde, wegabstrahiert – so ist ``scss-lint`` in Ruby geschrieben,
Ihr könnt ihn jedoch mit Pre-Commit verwenden ohne Eurem Projekt ein Gemfile
hinzufügen zu müssen.

Installation
------------

Bevor Ihr Hooks ausführen könnt, muss der pre-commit-Paketmanager installiert
sein.

… auf macOS:

.. code-block:: console

    $ brew install pre-commit

… in Eurem Python-Projekt:

.. code-block:: console

    $ pipenv install pre-commit

Überprüfen der Installation z.B. mit

.. code-block:: console

    $ pipenv run pre-commit -V
    pre-commit 2.6.0

Ihr könnt die Hooks auch automatisch aktualisieren mit:

.. code-block:: console

    $ pipenv run pre-commit autoupdate

Weitere Optionen findet Ihr unter `pre-commit autoupdate [options]
<https://pre-commit.com/#pre-commit-autoupdate>`_.

Konfiguration
-------------

Nachdem Pre-Commit installiert ist, können mit der ``.pre-commit-
config.yaml``-Datei im Root-Verzeichnis Eures Projekts Plugins für dieses
Projekt konfiguriert werden. 

.. code-block:: yaml

    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.5.0
        hooks:
        -   id: check-yaml
        -   id: end-of-file-fixer
        -   id: trailing-whitespace
    -   repo: https://github.com/psf/black
        rev: 19.10b0
        hooks:
        -   id: black

Ihr könnt Euch diese Datei auch generieren lassen mit

.. code-block:: console

    $ pipenv run pre-commit sample-config
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.4.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files

Wenn Ihr diesen pre-commit-Hook vor jedem commit ausführen möchtet, installiert
diesen mit ``pre-commit install``. Sollen die Hooks manuell ausgeführt werden,
kann dies mit ``pre-commit run --all-files`` geschehen. Einzelne Hooks können
dann auch separat ausgeführt werden, z.B. ``pre-commit run
trailing-whitespace``.

Beim ersten Aufruf eines pre-commit-Hooks wird dieser zunächst heruntergeladen
und anschließend installiert. Dies kann einige Zeit benötigen, z.B. wenn eine
Kopie von ``node`` erstellt werden muss.

.. code-block:: console

    $ pipenv run pre-commit run --all-files
    Trim Trailing Whitespace.................................................Passed
    Fix End of Files.........................................................Passed
    Check Yaml...............................................................Passed
    Check for added large files..............................................Passed
    black....................................................................Passed

Eine vollständige Liste der Konfigurationsoptionen erhaltet Ihr in `Adding pre-commit
plugins to your project
<https://pre-commit.com/#adding-pre-commit-plugins-to-your-project>`_. 

Ihr könnt auch eigene Hooks schreiben, siehe `Creating new hooks
<https://pre-commit.com/#creating-new-hooks>`_.

Verwenden in CI
---------------

Pre-Commit kann auch für Continuous Integration verwendet werden.

Beispiel für GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    - name: set PY
      run: echo "::set-env name=PY::$(python -VV | sha256sum | cut -d' ' -f1)"
    - uses: actions/cache@v1
      with:
        path: ~/.cache/pre-commit
        key: pre-commit|${{ env.PY }}|${{ hashFiles('.pre-commit-config.yaml') }}

.. seealso::

    `pre-commit/action <https://github.com/pre-commit/action>`_

Beispiel für GitLab Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    my_job:
      variables:
        PRE_COMMIT_HOME: ${CI_PROJECT_DIR}/.cache/pre-commit
      cache:
        paths:
          - ${PRE_COMMIT_HOME}

.. seealso::

    Weitere Informationen zur Feinabstimmung des Caching findet Ihr in `Good
    caching practices
    <https://docs.gitlab.com/ee/ci/caching/#good-caching-practices>`_.
