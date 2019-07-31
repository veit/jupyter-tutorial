Fortgeschrittene Nutzung
========================

Hooks
-----

Ihr könnt Pre- oder Post-Generate-Hooks schreiben. Dabei werden die
Jinja-Template-Variablen in die Skripte integriert werden, z.B.::

    if 'Not open source' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')

In einem Pre-Generate-Hook können z.B. Variablen validiert werden::

    import re
    import sys


    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    module_name = '{{ cookiecutter.module_name }}'

    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: %s is not a valid Python module name!' % module_name)

        # exits with status 1 to indicate failure
        sys.exit(1)

User Config
-----------

Wenn ihr Cookiecutter häufig verwendet, empfiehlt sich eine eigene User-Config:
``~/cookiecutterrc``, z.B.::

    default_context:
        full_name: "Veit Schiele"
        email: "veit@cusy.io"
        github_username: "veit"
    cookiecutters_dir: "~/.cookiecutters/"
    replay_dir: "~/.cookiecutter_replay/"

Replay
------

Beim Aufruf von ``ookiecutter`` wird eine ``json``-Datei angelegt in
``/.cookiecutter_replay/``, z.B.
``~/.cookiecutter_replay/cookiecutter-namespace-template.json``::

    {"cookiecutter": {"full_name": "Veit Schiele", "email": "veit@cusy.io", "github_username": "veit", "project_name": "vsc.example", "project_slug": "vsc.example", "namespace": "vsc", "package_name": "example", "project_short_description": "Python Namespace Package contains all you need to create a Python namespace package.", "pypi_username": "veit", "use_pytest": "y", "command_line_interface": "Click", "version": "0.1.0", "create_author_file": "y", "license": "MIT license", "_template": "https://github.com/veit/cookiecutter-namespace-template"}}

Sollen diese Informationen verwendet werden ohne diese erneut in der
Kommandozeile bestätigen zu müssen, könnt ihr einfach z.B. folgendes eingeben::

    $ cookiecutter --replay gh:veit/cookiecutter-namespace-template

Alternativ kann auch die Python-API verwendet werden::

    from cookiecutter.main import cookiecutter
    cookiecutter('gh:'veit/cookiecutter-namespace-template, replay=True)

Diese Funktion ist hilfreich, wenn ihr z.B. ein Projekt aus einer aktualisierten
Vorlage erstellen wollt.

Auswahlvariablen
----------------

Auswahlvariablen bieten verschiedene Möglichkeiten beim Erstellen eines
Projekts. Abhängig von der Wahl des Benutzers rendert die Vorlage diese
anders, z.B. wenn in der ``cookiecutter.json``-Datei folgende Auswahl angeboten
wird:

.. code-block:: json

    {
      "license": ["MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "GNU General Public License v3", "Other/Proprietary License"]
    }

Dies wird dann ausgewertet in
``cookiecutter-namespace-template/{{cookiecutter.project_name}}/README.rst``

.. code-block:: jinja

    {% set is_open_source = cookiecutter.license != 'Not open source' -%}
    {% if is_open_source %}
        …
    {%- endif %}

    {% if is_open_source %}
        …
    {% endif %}

und in ``cookiecutter-namespace-template/hooks/post_gen_project.py``:

.. code-block:: python

    if 'Not open source' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')

