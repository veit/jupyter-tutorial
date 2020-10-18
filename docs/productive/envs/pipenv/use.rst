Nutzung
=======

Beispiel
--------

Nachdem nun ``requests`` installiert ist, kann es verwendet werden.

#. Exemplarisch legen wir hierfür die Datei ``main.py`` mit folgendem Inhalt
   an:

.. code-block:: python

    import requests

    response = requests.get('https://cusy.io')

    print(response.status_code)

#. Anschließen kann das Skript ausgeführt werden mit:

.. code-block:: console

    $ pipenv run python main.py

#. Als Ergebnis des Aufrufs solltet ihr den HTTP-Status-Code ``200`` erhalten.

Die Verwendung von ``pipenv run`` stellt sicher, dass eure installierten Pakete
für Ihr Skript verfügbar sind.

Alternativ könnt ihr euch auch eine neue Shell mit ``pipenv shell`` erstellen,
mit der auf alle installierten Pakete zugegriffen werden kann:

.. code-block:: console

    $ pipenv shell
    Launching subshell in virtual environment…
    bash-4.3.30$  . /Users/veit/.local/share/virtualenvs/myproject-9TTuTZjx/bin/activate

Optionen
--------

``-venv``
    gibt den Pfad zum Virtualenv an, üblicherweise in
    ``~/.local/share/virtualenvs/``. Falls ihr jedoch ein Verzeichnis
    ``myproject/.venv`` angelegt habt, verwendet ``pipenv`` diesen Ordner um
    dort die zugehörige Python-Umgebung anzulegen.

``--py``
    gibt den Pfad zum Python-Interpreter an.

``--envs``
    gibt Optionen der Environment-Variablen aus.

    Für ``PIPENV_DONT_LOAD_ENV``, ``PIPENV_DONT_USE_PYENV`` und
    ``PIPENV_DOTENV_LOCATION`` siehe :doc:`env`.

    Wenn ihr diese Umgebungsvariablen pro Projekt festlegen möchtet, könnt ihr
    `direnv <https://direnv.net/>`_ verwenden.

    Beachtet auch, dass pip selbst Umgebungsvariablen unterstützt, falls ihr
    zusätzliche Anpassungen benötigt: `Pip Environment Variables
    <https://pip.pypa.io/en/stable/user_guide/#environment-variables>`_.

    Hier noch ein Beispiel:

    .. code-block:: console

        $ PIP_INSTALL_OPTION="-- -DCMAKE_BUILD_TYPE=Release" pipenv install -e .

    Weitere Informationen hierzu findet ihr unter
    `Configuration With Environment Variables
    <https://docs.pipenv.org/advanced/#configuration-with-environment-variables>`_

``--three``, ``--two``, ``--python``
    verwendet Python 2 oder Python 3 oder ein spezifisches Python, zu dem der
    Pfad angegeben wird.

``--site-packages``
    aktiviert site packages für das virtual environment.

``--pypi-mirror``
    gibt einen PyPI-Mirror an. Der Standard ist der
    :term:`Python Package Index (PyPI)`.

    Ihr könnt jedoch auch eure eigenen Mirror angeben:

    * mit der Umgebungsvariablen ``PIPENV_PYPI_MIRROR``
    * in der Kommandozeile, z.B. mit:

      .. code-block:: console

        $ pipenv install --pypi-mirror https://pypi.cusy.io/simple
        $ pipenv update --pypi-mirror https://pypi.cusy.io/simple
        …

    * oder im ``pipfile``:

      .. code-block:: ini

        [[source]]
        url = "https://pypi.python.org/simple"
        verify_ssl = true
        name = "pypi"

        [[source]]
        url = "https://pypi.cusy.io/simple"
        verify_ssl = true
        name = "cusy-mirror"

        [dev-packages]

        [packages]
        requests = {version="*", index="cusy-mirror"}
        maya = {version="*", index="pypi"}
        records = "*"

      .. note::
        Wird ein privater Index verwendet, kommt es aktuell noch zu Problemen
        mit dem Hashing der Pakete.

    Weitere Optionen findet ihr unter `pipenv
    <https://docs.pipenv.org/#pipenv>`_.

``check``
---------

``pipenv check`` prüft auf Sicherheitslücken und auf `PEP 508
<https://www.python.org/dev/peps/pep-0508/>`_-Marker im Pipfile. Hierzu
verwendet es `safety <https://github.com/pyupio/safety>`_.

Beispiel:

.. code-block:: console

    $ pipenv install django==1.10.1
    Installing django==1.10.1...
    …
    $ pipenv check
    Checking PEP 508 requirements…
    Passed!
    Checking installed package safety…

    33075: django >=1.10,<1.10.3 resolved (1.10.1 installed)!
    Django before 1.8.x before 1.8.16, 1.9.x before 1.9.11, and 1.10.x before 1.10.3, when settings.DEBUG is True, allow remote attackers to conduct DNS rebinding attacks by leveraging failure to validate the HTTP Host header against settings.ALLOWED_HOSTS.

    33076: django >=1.10,<1.10.3 resolved (1.10.1 installed)!
    Django 1.8.x before 1.8.16, 1.9.x before 1.9.11, and 1.10.x before 1.10.3 use a hardcoded password for a temporary database user created when running tests with an Oracle database, which makes it easier for remote attackers to obtain access to the database server by leveraging failure to manually specify a password in the database settings TEST dictionary.

    33300: django >=1.10,<1.10.7 resolved (1.10.1 installed)!
    CVE-2017-7233: Open redirect and possible XSS attack via user-supplied numeric redirect URLs
    ============================================================================================

    Django relies on user input in some cases  (e.g.
    :func:`django.contrib.auth.views.login` and :doc:`i18n </topics/i18n/index>`)
    to redirect the user to an "on success" URL. The security check for these
    redirects (namely ``django.utils.http.is_safe_url()``) considered some numeric
    URLs (e.g. ``http:999999999``) "safe" when they shouldn't be.

    Also, if a developer relies on ``is_safe_url()`` to provide safe redirect
    targets and puts such a URL into a link, they could suffer from an XSS attack.

    CVE-2017-7234: Open redirect vulnerability in ``django.views.static.serve()``
    =============================================================================

    A maliciously crafted URL to a Django site using the
    :func:`~django.views.static.serve` view could redirect to any other domain. The
    view no longer does any redirects as they don't provide any known, useful
    functionality.

    Note, however, that this view has always carried a warning that it is not
    hardened for production use and should be used only as a development aid.

.. note::
   ``pipenv`` bettet hierfür einen API-Clientschlüssel von ``pyup.io`` ein,
    anstatt eine vollständige Kopie der CC-BY-NC-SA lizenzierten Datenbank
    aufzunehmen.

Um nun die vollständige Datenbank zu installieren könnt ihr
diese auschecken mit:

.. code-block:: console

    $ pipenv install -e git+https://github.com/pyupio/safety-db.git#egg=safety-db

Um die lokale Datenbank zu verwenden, müsst ihr den Pfad zu dieser Datenbank
angeben, in meinem Fall also:

.. code-block:: console

    $ pipenv check --db /Users/veit/.local/share/virtualenvs/myproject-9TTuTZjx/src/safety-db/data
    ╒══════════════════════════════════════════════════════════════════════════════╕
    │                                                                              │
    │                               /$$$$$$            /$$                         │
    │                              /$$__  $$          | $$                         │
    │           /$$$$$$$  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$   /$$   /$$           │
    │          /$$_____/ |____  $$| $$$$   /$$__  $$|_  $$_/  | $$  | $$           │
    │         |  $$$$$$   /$$$$$$$| $$_/  | $$$$$$$$  | $$    | $$  | $$           │
    │          \____  $$ /$$__  $$| $$    | $$_____/  | $$ /$$| $$  | $$           │
    │          /$$$$$$$/|  $$$$$$$| $$    |  $$$$$$$  |  $$$$/|  $$$$$$$           │
    │         |_______/  \_______/|__/     \_______/   \___/   \____  $$           │
    │                                                          /$$  | $$           │
    │                                                         |  $$$$$$/           │
    │  by pyup.io                                              \______/            │
    │                                                                              │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ REPORT                                                                       │
    │ checked 21 packages, using local DB                                          │
    ╞══════════════════════════════════════════════════════════════════════════════╡
    │ No known security vulnerabilities found.                                     │
    ╘══════════════════════════════════════════════════════════════════════════════╛

``clean``
---------

``pipenv clean`` deinstalliert alle Pakete, die nicht in ``Pipfile.lock``
angegeben sind.

``graph``
---------

``pipenv graph`` zeigt für die aktuell installierten Pakete die
Abhängigkeitsgrapheninformationen an.

``install``
-----------

``pipenv install`` installiert bereitgestellte Pakete und fügt sie dem Pipfile
hinzu. ``pipenv install`` kennt die folgenden Optionen:

``-d``, ``--dev``
    installiert die Pakete in ``[dev-packages]``, z.B.:

.. code-block:: console

        $ pipenv install --dev pytest
        …
        $ cat Pipfile
        …
        [dev-packages]
        pytest = "*"

``--deploy``
    bricht ab, wenn ``Pipfile.lock`` nicht aktuell ist oder eine falsche
    Python-Version verwendet wird.

``-r``, ``--requirements`` ``<requirements.txt>``
    importiert eine ``requirements.txt``-Datei

``--sequential``
    installiert die Abhängigkeit in einer bestimmten Reihenfolge, nicht
    gleichzeitig.

    Dies verlangsamt zwar die Installation, erhöht jedoch die Determinierbarkeit
    der Builds.

``sdist`` vs. ``wheel``
~~~~~~~~~~~~~~~~~~~~~~~

Pip kann sowohl Pakete als :term:`Source Distribution (sdist)` oder
:term:`Wheel` installieren. Wenn beide auf PyPI vorhanden sind, wird pip ein
kompatibles :term:`Wheel` bevorzugen.

.. note::
   Abhängigkeiten von Wheels werden jedoch nicht erfasst von ``$ pipenv lock``.

Requirement specifier
~~~~~~~~~~~~~~~~~~~~~

Dabei konkretisieren `Requirement specifier <https://www.python.org/dev/peps/pep-0508/>`_
das jeweilige Paket.

* Die aktuelleste Version kann installiert werden, z.B.:

  .. code-block:: console

    $ pipenv install requests

* Eine spezifische Version kann installiert werden, z.B.:

  .. code-block:: console

    $ pipenv install requests==2.18.4

* Soll die Version in einem bestimmten Versionsbereich liegen, kann dies
  ebenfalls angegeben werden:

  .. code-block:: console

    $ pipenv install requests>=2,<3

* Auch eine kompatible Version lässt sich installieren:

  .. code-block:: console

    $ pipenv install requests~=2.18

  Dies ist kompatibel mit ``==2.18.*``.

* Für einige Pakete können auch Installationsoptionen mit `Extras
  <https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies>`_
  mit eckigen Klammern angegeben werden:

  .. code-block:: console

    $ pipenv install requests[security]

* Es kann auch angegeben werden, dass bestimmte Pakete nur auf bestimmten
  Systemen installiert werden, so wird bei folgendem ``Pipfile`` das Modul
  ``pywinusb`` nur auf Windows-Systemen installiert:

  .. code-block:: ini

    [packages]
    pywinusb = {version = "*", sys_platform = "== 'win32'"}

  Ein komplexeres Beispiel unterscheidet, welche Modul-Versionen mit welchen
  Python-Versionen installiert werden soll:

  .. code-block:: ini

    [packages]
    unittest2 = {version = ">=1.0,<3.0", markers="python_version < '2.7.9' or (python_version >= '3.0' and python_version < '3.4')"}

VCS
~~~

Ihr könnt auch Python-Pakete aus Versionsverwaltungen installieren, z.B.:

.. code-block:: console

    $ pipenv install -e git+https://github.com/requests/requests.git#egg=requests

.. note::
   Wenn ``editable=false``, werden Unterabhängigkeiten nicht aufgelöst.

Weitere Informationen zu pipenv und VCS erhaltet ihr in `Pipfile spec
<https://github.com/pypa/pipfile>`_.

Auch die Credentials der Versionsverwaltung lassen sich im Pipfile angeben,
z.B.:

.. code-block:: ini

    [[source]]
    url = "https://$USERNAME:${PASSWORD}@pypi.cusy.io/simple"
    verify_ssl = true
    name = "cusy-pypi"

.. note::
   ``pipenv`` hasht das ``Pipfile``, bevor die Umgebungsvariablen ermittelt
   werden, und auch in ``Pipfile.lock`` werden die Umgebungsvariablen
   geschrieben, sodass keine Credentials in der Versionsverwaltung gespeichert
   werden müssen.

``lock``
--------

``pipenv lock`` generiert die Datei ``Pipfile.lock``, die alle Abhängigkeiten
und Unterabhängigkeiten eures Projekts aufführt inklusive der neuesten
verfügbaren Versionen und der aktuellen Hashwerte für die heruntergeladenen
Dateien. Dies stellt wiederholbare und vor allem deterministische Builds sicher.

.. note::
   Um den Determinismus zu erhöhen, kann neben den Hashwerten auch die
   Installationsreihenfolge gewährleistet werden. Hierfür gibt es das
   ``--sequential``-Flag.

Security Features
~~~~~~~~~~~~~~~~~

``pipfile.lock`` nutzt einige Sicherheitsverbesserungen von ``pip``. So werden
standardmäßig sha256-Hashes jedes heruntergeladenen Pakets generiert.

Wir empfehlen dringend, ``lock`` zum Deployment von Entwicklungsumgebungen in
die Produktion zu verwenden. Hierbei verwendet ihr ``pipenv lock`` zum
Kompilieren eurer Abhängigkeiten in der Entwicklungsumgebung und anschließend
könnt ihr die kompilierte ``Pipfile.lock``-Datei in der Produktionsumgebung
für reproduzierbare Builds zu verwenden.


``open``
--------

``pipenv open MODULE`` zeigt ein bestimmtes Modul in eurem Editor an.

Falls ihr `PyCharm <https://www.jetbrains.com/pycharm/>`_ verwendet, müsst ihr
``pipenv`` für euer Python-Projekt konfigurieren. Wie dies geht, ist in
`Configuring Pipenv Environment
<https://www.jetbrains.com/help/pycharm/pipenv.html>`_ beschrieben.

``run``
-------

``pipenv run`` spawnt einen Befehl, der im virtual environment installiert ist,
z.B.:

    $ pipenv run python main.py

``shell``
---------

``pipenv shell`` spawnt eine Shell, im virtual environment. Damit erhaltet ihr
einen Python-Interpreter, der alle Python-Pakete enthält und sich somit
hervorragend z.B. zum Debugging und Testen eignet:

.. code-block:: console

    $ pipenv shell --fancy
    Launching subshell in virtual environment…
    bash-4.3.30$ python
    Python 3.6.4 (default, Jan  6 2018, 11:51:59)
    >>> import requests
    >>>

.. note::
   Shells sind meist nicht so konfiguriert, dass eine Subshell verwendet werden
   kann. Dies kann dazu führen, dass ``pipenv shell --fancy`` zu unerwarteten
   Ergebnissen führt. In diesen Fällen sollte ``pipenv shell`` verwendet
   werden, da diese einen Kompatibilitätsmodus verwendet.

``sync``
--------

``pipenv sync`` installiert alle in ``Pipfile.lock`` angegebenen Pakete.

``uninstall``
-------------

``pipenv uninstall`` deinstalliert alle bereitgestellten Pakete und entfernt sie
aus dem ``Pipfile``. ``uninstall`` unterstützt alle Parameter von `install
<#install>`_ und darüberhinaus die folgenden beiden Optionen:

``--all``
    löscht alle Dateien aus der virtuellen Umgebung, lässt aber ``Pipfile``
    unberührt.
``--all-dev``
    entfernt alle Entwicklungspakete aus der virtuellen Umgebung und entfernt
    sie aus ``Pipfile``.

``update``
----------

``pipenv update`` führt zunächst ``pipenv lock`` aus, dann ``pipenv sync``.

``pipenv update`` hat u.a. folgende Optionen:

``--clear``
    löscht den *Dependency Cache*.
``--outdated``
    listet veraltete Abhängigkeiten auf.
