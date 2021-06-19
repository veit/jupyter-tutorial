``check-manifest``
==================

`check-manifest <https://pypi.org/project/check-manifest/>`_ is a tool with
which you can quickly check whether the file ``Manifest.in`` for Pyton packages
is complete.

Installation
------------

.. code-block:: console

    $ pipenv install check-manifest

Check
-----

.. code-block:: console

    $ cd /path/to/MANIFEST.in
    $ pipenv run check-manifest

… or for an automatic update

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

Configuration
-------------

You can configure ``check-manifest`` so that certain file patterns are ignored
by creating a section  ``[tool.check-manifest]`` in your  ``pyproject.toml``
file or a section ``[check-manifest]`` in your  ``setup.cfg`` or ``tox.ini``
file, for example:

.. code-block:: yaml

    [tool.check-manifest]
    ignore = [".travis.yml"]

    # setup.cfg or tox.ini
    [check-manifest]
    ignore =
        .travis.yml

``check-manifest`` knows the following options:

``ignore``
    A list of filename patterns that are ignored by ``check-manifest``. Use this
    option if you want to keep files in your version control system that
    shouldn’t be in your source distributions. The standard list is:

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
    If ``true``, your ``ignore`` entries replace the standard list instead of
    completing it.
``ignore-bad-ideas``
    A list of filename patterns that will be ignored by checking the generated
    files. This allows you to keep generated files in your version control
    system, even if this is usually a bad idea.

Integration with version control
--------------------------------

With :doc:`/productive/git/pre-commit`, `check-manifest` can be part of your Git
workflow. To do this, add the following to your  `.pre-commit-config.yaml` file:

.. code-block:: yaml

    repos:
    -   repo: https://github.com/mgedmin/check-manifest
        rev: "0.39"
        hooks:
        -   id: check-manifest
