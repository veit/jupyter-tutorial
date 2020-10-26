Advanced usage
==============

Hooks
-----

You can write pre- or post-generate hooks. The Jinja template variables will be
integrated into the scripts, for example:

.. code-block:: python

    if 'Not open source' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')

Variables, for example, can be validated in a pre-generate hook:

.. code-block:: python

    import re
    import sys


    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    module_name = '{{ cookiecutter.module_name }}'

    if not re.match(MODULE_REGEX, module_name):
        print('ERROR: %s is not a valid Python module name!' % module_name)

        # exits with status 1 to indicate failure
        sys.exit(1)

User config
-----------

If you use CookieCutter frequently, we recommend your own user config
``~/cookiecutterrc``, e.g.:

.. code-block:: bash

    default_context:
        full_name: "Veit Schiele"
        email: "veit@cusy.io"
        github_username: "veit"
    cookiecutters_dir: "~/.cookiecutters/"
    replay_dir: "~/.cookiecutter_replay/"

Replay
------

When calling ``cookiecutter`` a ``json`` file is created in
``/.cookiecutter_replay/``, for example
``~/.cookiecutter_replay/cookiecutter-namespace-template.json``:

.. code-block:: json

    {"cookiecutter": {"full_name": "Veit Schiele", "email": "veit@cusy.io", "github_username": "veit", "project_name": "vsc.example", "project_slug": "vsc.example", "namespace": "vsc", "package_name": "example", "project_short_description": "Python Namespace Package contains all you need to create a Python namespace package.", "pypi_username": "veit", "use_pytest": "y", "command_line_interface": "Click", "version": "0.1.0", "create_author_file": "y", "license": "MIT license", "_template": "https://github.com/veit/cookiecutter-namespace-template"}}

If you want to use this information without having to confirm them again in the
command line, you can simply enter the following:

.. code-block:: console

    $ cookiecutter --replay gh:veit/cookiecutter-namespace-template

Alternatively, the Python API can also be used:

.. code-block:: python

    from cookiecutter.main import cookiecutter
    cookiecutter('gh:'veit/cookiecutter-namespace-template, replay=True)

This function is helpful if you want to create a project from an updated
template, for example.

Selection variables
-------------------

Selection variables offer various options when creating a project. Depending on
the user’s choice, the template renders it differently, e.g. if in the
``cookiecutter.json`` file the following selection is offered:

.. code-block:: json

    {
      "license": ["MIT license", "BSD license", "ISC license", "Apache Software License 2.0", "GNU General Public License v3", "Other/Proprietary License"]
    }

This is interpreted in
``cookiecutter-namespace-template/{{cookiecutter.project_name}}/README.rst``

.. code-block:: jinja

    {% set is_open_source = cookiecutter.license != 'Not open source' -%}
    {% if is_open_source %}
        …
    {%- endif %}

    {% if is_open_source %}
        …
    {% endif %}

and in ``cookiecutter-namespace-template/hooks/post_gen_project.py``:

.. code-block:: python

    if 'Not open source' == '{{ cookiecutter.license }}':
        remove_file('LICENSE')
