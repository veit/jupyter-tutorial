Upload
======

Schließlich solltet ihr das Paket auf dem :term:`Python Package Index (PyPI)`
oder einem anderen Index bereitstellen.

Hierfür solltet ihr euch bei *Test PyPI* registrieren. *Test-PyPI* ist eine
separate Instanz, die zum Testen und Experimentieren vorgesehen ist. Um dort
ein Konto einzurichten, geht ihr auf https://test.pypi.org/account/register/.
Weitere Informationen findet ihr unter `Using TestPyPI
<https://packaging.python.org/guides/using-testpypi/>`_.

Nachdem ihr registriert seid, könnt ihr euer :term:`Distribution Package` mit
`twine <https://packaging.python.org/key_projects/#twine>`_ hochladen. Hierzu
müsst ihr jedoch zunächst twine installieren mit:

.. code-block:: console

    $ pipenv install twine
    Installing twine…
    Collecting twine
    …

Nach der Installation von Twine könnt ihr alle Archive unter ``/dist`` auf den
Python Package Index hochladen mit:

.. code-block:: console

    $ pipenv run twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Ihr werdet nach Benutzernamen und Passwort gefragt, mit dem ihr euch bei *Test
PyPI* registriert habt. Anschließend solltet ihr eine ähnliche Ausgabe sehen:

.. code-block:: console

    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: veit
    Enter your password:
    Uploading example-0.0.1-py3-none-any.whl
    100%|█████████████████████| 4.65k/4.65k [00:01<00:00, 2.88kB/s]
    Uploading example-0.0.1.tar.gz
    100%|█████████████████████| 4.25k/4.25k [00:01<00:00, 3.05kB/s]

.. note::
   Wenn ihr eine ähnliche Fehlermeldung erhaltet wie

   .. code-block:: console

    The user 'veit' isn't allowed to upload to project 'example'

   müsst ihr einen eindeutigen Namen für euer Paket auswählen. 

   Eine gute Wahl ist ``minimal_example``. Aktualisiert das
   ``name``-Argument in der ``setup.py``-Datei, entfernt das
   ``dist``-Verzeichnis und generiert die Archive neu.


.. seealso::
    Wenn ihr die PyPI-Anmeldung automatisieren wollt, lest bitte `Careful With
    That PyPI
    <https://glyph.twistedmatrix.com/2017/10/careful-with-that-pypi.html>`_.

Installation
============

Ihr könnt :term:`pipenv` verwenden um euer Paket zu installieren und zu überprüfen,
ob es funktioniert. Erstellt eine neue :term:`virtuelle Umgebung` und
installiert euer Paket von *Test PyPI*:

.. code-block:: console

    $ mkdir test
    $ cd !$
    $ pipenv install --extra-index-url https://test.pypi.org/simple/ minimal_example

.. note::
   Wenn ihr einen anderen Paketnamen verwendet habt, ersetzt ihn im obigen
   Befehl durch euren Paketnamen.

:term:`pip` sollte das Paket von *Test PyPI* installieren und die Ausgabe sollte
in etwa so aussehen:

.. code-block:: console

    Collecting example_pkg
      Downloading https://test-files.pythonhosted.org/packages/.../minimal_example-0.0.1-py3-none-any.whl
    Installing collected packages: minimal_example
    Successfully installed minimal_example-0.0.1

Ihr könnt testen, ob euer Paket korrekt installiert wurde indem ihr das Modul
importiert und auf die ``name``-Eigenschaft referenziert, die zuvor in
``__init__.py`` eingegeben wurde:

.. code-block:: console

    $ pipenv run python
    Python 3.7.0 (default, Aug 22 2018, 15:22:29) 
    …
    >>> import minimal_example
    >>> minimal_example.name
    'minimal_example'

