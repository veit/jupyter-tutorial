Umgebungsvariablen
==================

``pipenv``-Umgebungsvariablen
-----------------------------

``pipenv --envs`` gibt Optionen der Environment-Variablen aus.

Weitere Informationen hierzu findet ihr unter
`Configuration With Environment Variables
<https://docs.pipenv.org/advanced/#configuration-with-environment-variables>`_.

``.env``-Datei
--------------

Wenn eine ``.env``-Datei in eurer virtuellen Umgebung vorhanden ist, werden
``$ pipenv shell`` und ``$ pipenv run`` diese automatisch laden:

.. code-block:: console

    $ cat .env
    USERNAME=Veit⏎

    $ pipenv run python
    Loading .env environment variables…
    …
    >>> import os
    >>> os.environ['USERNAME']
    'Veit'

Auch die Credentials, z.B. der Versionsverwaltung lassen sich im ``Pipfile``
angeben, z.B.:

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

Ihr könnt die ``.env``-Datei auch außerhalb eures Virtual Environments
speichern. Ihr müsst dann nur den Pfad zu dieser Datei angeben in
``PIPENV_DOTENV_LOCATION``:

.. code-block:: console

    $ PIPENV_DOTENV_LOCATION=/path/to/.env pipenv shell

Ihr könnt auch verhindern, dass ``pipenv`` eine vorhanden ``.env``-Datei
verwenet mit:

.. code-block:: console

    $ PIPENV_DONT_LOAD_ENV=1 pipenv shell

