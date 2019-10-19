Distribution Package erstellen
==============================

:term:`Distribution Packages <Distribution Package>` sind Archive, die in einen
Paket-Index hochgeladen und mit :term:`Pip` installiert werden können.

.. note::
    Beachtet bitte, dass es immer noch viele Anleitungen gibt, die einen Schritt
    zum Aufruf der ``setup.py`` enthalten, z.B. ``python setup.py sdist``. Dies
    wird jedoch heutzutage von Teilen der `Python Packaging Authority (PyPA)
    <https://github.com/pypa/>`_ als `Anti-Pattern
    <https://twitter.com/pganssle/status/1152695229105000453>`_ angesehen.

``setup.py``
------------

Eine minimale und dennoch funktionale ``setup.py`` findet ihr z.B. im `attrs
<https://github.com/python-attrs/attrs/>`_-Paket: `setup.py
</https://github.com/python-attrs/attrs/blob/0023e5b/setup.py>`_. Daran könnt
ihr erkennen, dass das meiste *Boilerplate* ist und lediglich die Zeilen 10–37
Metadaten für diese spezielle Paket sind. Die meisten anderen Metadaten sind in
der `__init__
<https://github.com/python-attrs/attrs/blob/master/src/attr/__init__.py>`_
gespeichert und werden mit regulären Ausdrücken erschlossen. Alternativ können
diese Daten auch in ein separates Modul ausgelagert und mit Python analysiert
werden, wie dies z.B. in `cryptography
<https://github.com/pyca/cryptography/blob/e575e3d/setup.py#L37-L39>`_
erfolgt.

In beiden Fällen werden doppelte Metadaten in Paket und Code vermieden.

``src``-Package
---------------

Das `packages`-Feld verwendet setuptools’s `find_packages()
<https://setuptools.readthedocs.io/en/latest/setuptools.html#using-find-packages>`_
um darunterliegende Pakete zu finden und das `package_dir
<https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages>`_-Feld
beschreibt, wo das Root-Verzeichnis ist.

.. note::
    ``find_packages()`` ohne ``src/``-Verzeichnis würde alle Verzeichnisse mit
    einer ``__init__.py``-Datei paketieren, also auch ``tests/``-Verzeichnisse.

``version``
-----------

Für ``version`` gibt es verschiedene Möglichkeiten, die in `PEP 0440
<https://www.python.org/dev/peps/pep-0440/>`_ beschrieben sind.

``classifiers``
---------------

`classifiers <https://pypi.org/classifiers/>`_ haben eine nützliche
Zusatzfunktion: PyPI lehnt unbekannte *Classifiers* ab, sodass damit auch ein
versehentlicher Upload vermieden werden kann.

.. seealso::
    `Add invalid classifier for non open source license to avoid upload to…
    <https://github.com/veit/cookiecutter-namespace-template/commit/f4fff8ee8595ae2e59e5feb92211c8e3f1252461>`_

Abhängigkeiten
--------------

Versionsnummern von Abhängigkeiten sollten üblicherweise nicht in der
``setup.py`` festgeschrieben werden sondern in der `requirements.txt
<https://pip.pypa.io/en/latest/user_guide/#requirements-files>`_-Datei.

.. seealso::
    `setup.py vs requirements.txt
    <https://caremad.io/posts/2013/07/setup-vs-requirement/>`_

Andere Dateien
--------------

``MANIFEST.in``
~~~~~~~~~~~~~~~

Die Datei enthält alle Dateien und Verzeichnisse, die nicht bereits mit
``packages`` oder ``py_module`` erfasst werden. Sie kann z.B. so aussehen:
`attrs/MANIFEST.in
<https://github.com/python-attrs/attrs/blob/a9a32a2/MANIFEST.in>`_.

Weitere Anweisungen in `Manifest.in` findet ihr in `Creating a source
distribution
<https://docs.python.org/3/distutils/commandref.html?highlight=manifest#creating-a-source-distribution-the-sdist-command>`_.

.. note::
    Häufig wird die Aktualisierung der ``Manifest.in``-Datei vergessen. Um dies
    zu vermeiden, könnt ihr `check-manifest
    <https://pypi.org/project/check-manifest/>`_ in einem ``pre-commit``-Hook
    verwenden.

.. note::
    Wenn ihr Dateien und Verzeichnisse aus ``MANIFEST.in`` auch installiert
    werden sollen, z.B. wenn es sich um laufzeitrelevante Daten handelt, könnt
    ihr dies mit ``include_package_data=True`` in eurem ``setup()``-Aufruf
    angeben.

``setup.cfg``
~~~~~~~~~~~~~

Diese Datei wird nicht mehr benötigt, zumindest nicht für die Paketierung.
``wheel`` sammelt heutzutage alle erforderlichen Lizenzdateien automatisch und
``setuptools`` kann mit dem ``options``-Keyword-Argument universelle
``whell``-Pakete bauen, z.B. ``attrs-19.3.0-py2.py3-none-any.whl``.

``pyproject.toml``
~~~~~~~~~~~~~~~~~~

`PEP 517 <https://www.python.org/dev/peps/pep-0517/>`_ und `PEP 518
<https://www.python.org/dev/peps/pep-0518/>`_ brachten Plugable Build-Backends,
isolierte Builds und ``pyproject.toml``. Da wir ``setuptools`` verwenden,
sollte die Datei so, oder so ähnlich, aussehen:

.. code-block:: toml

    [build-system]
    requires = ["setuptools>=40.6.0", "wheel"]
    build-backend = "setuptools.build_meta"

LICENSE
~~~~~~~

Wenn ihr eine möglichst große Verbreitung eures Pakets erreichen wollt, sind
MIT- oder die BSD-Varianten eine gute Wahl. Die Apache-Lizenz schützt euch
besser vor Patentverletzungen ist jedoch nicht kompatibel mit der GPL v2.

README.rst
~~~~~~~~~~

Diese Datei teilt potentiellen Nutzern mit, worauf sie bei der Verwendung des
Pakets achten müssen. Schreibt das Dokument in `ReStructuredText (ReST)
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer>`_,
sodass ihr es später problemlos mit ``.. include:: ../../README.rst`` in die
Sphinx-Dokumentation übernehmen könnt.

Build
-----

Wechselt in das Verzeichnis, in dem sich die ``setup.py``-Datei befindet.

.. code-block:: console

    $ rm -rf build dist
    $ pipenv run python3 -m pep517.build .

Die erste Zeile stellt sicher, dass ein sauberes Build ohne Artefakte
früherer Builds erstellt wird. Die zweite Zeile baut ein ``sdist``-Archiv unter
Linux/Mac als gezippte Tar-Datei (``.tar.gz``) und unter Windows eine ZIP-Datei
sowie ein ``bdist_wheel``-Archiv  mit ``.whl`` im ``dist``-Verzeichnis.

Dieser Befehl sollte also die folgenden beiden Dateien erzeugen::

    dist/
      example-0.0.1-py3-none-any.whl
      example-0.0.1.tar.gz

``py3``
    Python-Version, mit der das Paket gebaut wurde
``none``
    nicht OS-spezifisch
``any``
    geeignet für jede Prozessorarchitektur

Die Referenz für die Dateinamen findet ihr in `File name convention
<https://www.python.org/dev/peps/pep-0427/#file-name-convention>`_.

.. seealso::
    Weitere Infos zu ``sdist`` erhaltet ihr in `Creating a Source Distribution
    <https://docs.python.org/2/distutils/sourcedist.html#creating-a-source-distribution>`_.
    und `PEP 376 <https://www.python.org/dev/peps/pep-0376/>`_.

.. note::
    Die Verwendung von `pep517.build <https://www.python.org/dev/peps/pep-0517/>`_
    zum Erstellen von Paketen ist aktuell (Oktober 2019) noch `etwas umstritten
    <https://discuss.python.org/t/building-distributions-and-drawing-the-platypus/2062>`_.
    Es scheint Konsens zu sein, dass diese Funktionalität entweder in Pip oder in Twine
    zusammengeführt werden sollte. Derzeit scheint der oben genannte Weg jedoch der
    sauberste zu sein, ein Paket zu erstellen. Ich werde diesen Artikel
    aktualisieren, sobald sich eine andere Lösung durchsetzt.

Testen
------

.. code-block:: console

    $  pipenv --rm
    $ pipenv install dist/attrs-19.3.0.tar.gz
    …
    Successfully built attrs
    Installing collected packages: attrs
    Successfully installed attrs-19.3.0
    $ pipenv run python
    …
    >>> import attr; attr.__version__
    '19.3.0'

oder

.. code-block:: console

    $  pipenv --rm
    $ pipenv install install dist/attrs-19.3.0-py2.py3-none-any.whl
    …
    Successfully built attrs
    Installing collected packages: attrs
    Successfully installed attrs-19.3.0
    $ pipenv run python
    …
    >>> import attr; attr.__version__
    '19.3.0'

