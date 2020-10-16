CookieCutter-Features
=====================

* Cross-platform: Windows, Mac und Linux werden unterstützt
* Funktioniert mit Python 3.6, 3.7, 3.8 und PyPy3
* Die Projektvorlagen können für jede Programmiersprache und jedes
  Markup-Format erstellt werden: Python, JavaScript, Ruby, ReST, CSS, HTML.
  Es können auch mehrere Sprachen im selben Template verwendet werden.
* Templates lassen sich einfach im Terminal anpassen:

  .. code-block:: console

    $ cookiecutter https://github.com/veit/cookiecutter-namespace-template
    full_name [Veit Schiele]:
    …

* Ihr könnt auch lokale Templates verwenden:

  .. code-block:: console

    $ cookiecutter cookiecutter-namespace-template

* Alternativ könnt ihr CookieCutter auch mit Python verwenden:

  .. code-block:: console

    $ bin/python
    >>> from cookiecutter.main import cookiecutter
    >>> cookiecutter('.https://github.com/veit/cookiecutter-namespace-template.git')
    full_name [Veit Schiele]:
    …

* Verzeichnis- und Dateinamen können Vorlagen zugewiesen werden, z.B.:

  .. code-block:: jinja

    {{cookiecutter.project_name}}/{{cookiecutter.namespace}}/{{cookiecutter.package_name}}/{{cookiecutter.project_slug}}.py

* Die Verschachtelungstiefe ist unbegrenzt
* Das Templating basiert auf `Jinja2 <http://jinja.pocoo.org/>`_
* Ihr könnt eure Template-Variablen einfach in einer ``cookiecutter.json``-Datei
  speichern, beispielsweise:

  .. code-block:: json

    {
      "full_name": "Veit Schiele",
      "email": "veit@example.org",
      "github_username": "veit",
      "project_name": "vsc.example",
      "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}",
      "namespace": "{{ cookiecutter.project_slug.split('.')[0] }}",
      "package_name": "{{ cookiecutter.project_slug.split('.')[1] }}",
      "project_short_description": "Python Namespace Package contains all you need to create a Python namespace package.",
      "pypi_username": "veit",
      "use_pytest": "y",
      "command_line_interface": ["Click", "No command-line interface"],
      "version": "0.1.0",
      "create_author_file": "y",
      "license": ["MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "GNU General Public License v3", "Not open source"]
    }

* Ihr könnt die Werte auch für mehrere Vorlagen hinterlegen in
  ``~/cookiecutterrc``:

  .. code-block:: bash

    default_context:
        full_name: "Veit Schiele"
        email: "veit@cusy.io"
        github_username: "veit"
    cookiecutters_dir: "~/.cookiecutters/"

* CookieCutter-Templates, die aus einem Repository geladen wurden, werden
  üblicherweise in ``~/.cookiecutters/`` gespeichert. Anschließend können sie
  direkt über ihren Verzeichnisnamen referenziert werden, also z.B. mit:

  .. code-block:: console

    $ cookiecutter cookiecutter-namespace-package
