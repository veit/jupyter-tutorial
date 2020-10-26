CookieCutter features
=====================

* Cross-platform: Windows, Mac and Linux are supported
* works with Python 3.6, 3.7, 3.8 and PyPy3
* The project templates can be created for any programming language and any
  markup format: Python, JavaScript, Ruby, ReST, CSS, HTML. Several languages
  can also be used in the same template.
* Templates can be easily adapted in the terminal:

  .. code-block:: console

    $ cookiecutter https://github.com/veit/cookiecutter-namespace-template
    full_name [Veit Schiele]:
    …

* You can also use local templates:

  .. code-block:: console

    $ cookiecutter cookiecutter-namespace-template

* Alternatively you can also use CookieCutter with Python:

  .. code-block:: console

    $ bin/python
    >>> from cookiecutter.main import cookiecutter
    >>> cookiecutter('.https://github.com/veit/cookiecutter-namespace-template.git')
    full_name [Veit Schiele]:
    …

* Directory and file names can be assigned to templates, for example:

  .. code-block:: jinja

    {{cookiecutter.project_name}}/{{cookiecutter.namespace}}/{{cookiecutter.package_name}}/{{cookiecutter.project_slug}}.py

* The nesting depth is unlimited
* The templating is based on `Jinja2 <http://jinja.pocoo.org/>`_
* You can simply save your template variables in a ``cookiecutter.json`` file,
  for example:

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

* You can also save the values for several templates in ``~/cookiecutterrc``:

  .. code-block:: bash

    default_context:
        full_name: "Veit Schiele"
        email: "veit@cusy.io"
        github_username: "veit"
    cookiecutters_dir: "~/.cookiecutters/"

* CookieCutter templates loaded from a repository are usually stored in
  ``~/.cookiecutters/``. Then they can be referenced directly via their
  directory name, e.g. with:

  .. code-block:: console

    $ cookiecutter cookiecutter-namespace-package
