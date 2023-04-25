Usage
=====

Example
-------

Now that ``requests`` is installed, it can be used.

#. As an example, we create the file ``main.py`` with the following content:

.. code-block:: python

    import requests

    response = requests.get('https://cusy.io')

    print(response.status_code)

#. Then the script can be executed with:

.. code-block:: console

    $ pipenv run python main.py

#. As a result of the call you should receive the HTTP status code ``200``.

Using ``pipenv run`` ensures that your installed packages are available for your
script.

Alternatively, you can also create a new shell ``pipenv shell`` with which all
installed packages can be accessed:

.. code-block:: console

    $ pipenv shell
    Launching subshell in virtual environment...
     . /srv/jupyter/.local/share/virtualenvs/myproject-CZKj6mqJ/bin/activate

Options
-------

``-venv``
    specifies the path to the Virtualenv, usually in
    ``~/.local/share/virtualenvs/``. However, if you have created a directory
    ``myproject/.venv``, ``pipenv`` use this folder to create the associated
    Python environment there.

``--py``
    specifies the path to the Python interpreter.

``--envs``
    outputs options of the environment variables.

    For ``PIPENV_DONT_LOAD_ENV``, ``PIPENV_DONT_USE_PYENV`` and
    ``PIPENV_DOTENV_LOCATION`` see :doc:`env`.

    If you want to set these environment variables per project, you can use
    `direnv <https://direnv.net/>`_.

    Also note that pip itself supports environment variables in case you need
    additional adjustments: `Pip Environment Variables
    <https://pip.pypa.io/en/stable/user_guide/#environment-variables>`_.

    Here is another example:

    .. code-block:: console

        $ PIP_INSTALL_OPTION="-- -DCMAKE_BUILD_TYPE=Release" pipenv install -e .

    Further information can be found at `Configuration With Environment
    Variables
    <https://docs.pipenv.org/advanced/#configuration-with-environment-variables>`_

``--three``, ``--two``, ``--python``
    uses Python 2 or Python 3 or a specific Python to which the path is given.

``--site-packages``
    enables site packages for the virtual environment.

``--pypi-mirror``
    indicates a PyPI mirror. The standard is the :term:`Python Package Index`
    (:term:`PyPI`)`.

    However, you can also specify your own mirrors:

    * with the environment variable ``PIPENV_PYPI_MIRROR``
    * in the command line, for example with:

      .. code-block:: console

        $ pipenv install --pypi-mirror https://pypi.cusy.io/simple
        $ pipenv update --pypi-mirror https://pypi.cusy.io/simple
        …

    * or in ``pipfile``:

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
        If a private index is used, there are currently still problems with
        hashing the packages.

    You can find more options at `pipenv <https://docs.pipenv.org/#pipenv>`_.

.. _pipenv_check:

``check``
---------

``pipenv check`` checks for security holes and for :pep:`508` markers in the pip
ile. For this it uses `safety <https://github.com/pyupio/safety>`_.

Example:

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
   :term`Pipenv` embeds an API client key from `pyup.io <>https://pyup.io`_,
   instead of including a full copy of the `CC BY-NC-SA
   <https://creativecommons.org/licenses/by-nc-sa/3.0/de/deed.en>`_ licensed
   database.

In order to install the complete database you can check it out with:

.. code-block:: console

    $ pipenv install -e git+https://github.com/pyupio/safety-db.git#egg=safety-db

To use the local database, you have to enter the path to this database, in my case:

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

``pipenv clean`` uninstalls all packages not specified in ``Pipfile.lock``.

``graph``
---------

``pipenv graph`` displays the dependency graph information for the currently
installed packages.

``install``
-----------

``pipenv install`` installs the provided packages and adds them to the pipfile.
``pipenv install`` knows the following options:

``-d``, ``--dev``
    installs the packages in ``[dev-packages]``, for example:

.. code-block:: console

        $ pipenv install --dev pytest
        …
        $ cat Pipfile
        …
        [dev-packages]
        pytest = "*"

``--deploy``
    aborts if ``Pipfile.lock`` is out of date or an incorrect Python version is
    used.

``-r``, ``--requirements`` ``<requirements.txt>``
    imports a ``requirements.txt`` file.

``--sequential``
    installs the dependency in a specific order, not at the same time.

    While this slows down the installation, it increases the determinability of
    the builds.

``sdist`` vs. ``wheel``
~~~~~~~~~~~~~~~~~~~~~~~

:term:`pip` can install packages as :term:`Source Distribution` (:term:`sdist`)
or :term:`Wheel` If both are present on :term:`PyPI`, pip will prefer a
compatible :term:`Wheel`.

.. note::
   However, dependencies on wheels are not covered by ``$ pipenv lock``.

Requirement specifier
~~~~~~~~~~~~~~~~~~~~~

`Requirement specifier <https://www.python.org/dev/peps/pep-0508/>`_ specify the
respective package.

* The latest version can be installed, for example:

  .. code-block:: console

    $ pipenv install requests

* A specific version can be installed, for example:

  .. code-block:: console

    $ pipenv install requests==2.18.4

* If the version has to be in a specific version range, this can also be
  specified:

  .. code-block:: console

    $ pipenv install requests>=2,<3

* A compatible version can also be installed:

  .. code-block:: console

    $ pipenv install requests~=2.18

 This is compatible with ``==2.18.*``.

* For some packages, installation options  `Extras
  <https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies>`_
  can also be specified with square brackets:

  .. code-block:: console

    $ pipenv install requests[security]

* It can also be specified that certain packages are only installed on certain
  systems, so for the following ``Pipfile`` the module ``pywinusb`` is only
  installed on Windows systems.

  .. code-block:: ini

    [packages]
    pywinusb = {version = "*", sys_platform = "== 'win32'"}

  A more complex example differentiates which module versions should be
  installed with which Python versions:

  .. code-block:: ini

    [packages]
    unittest2 = {version = ">=1.0,<3.0", markers="python_version < '2.7.9' or (python_version >= '3.0' and python_version < '3.4')"}

VCS
~~~

You can also install Python packages from version control, for example:

.. code-block:: console

    $ pipenv install -e git+https://github.com/requests/requests.git#egg=requests

.. note::
   If ``editable=false``, sub-dependencies are not resolved.

Further information on pipenv and VCS can be found in `Pipfile spec
<https://github.com/pypa/pipfile>`_.

The version management credentials can also be specified in the pipfile, for
example

.. code-block:: ini

    [[source]]
    url = "https://$USERNAME:${PASSWORD}@pypi.cusy.io/simple"
    verify_ssl = true
    name = "cusy-pypi"

.. note::
   ``pipenv`` hashes ``Pipfile`` before the environment variables are determine,
   and the environment variables are also written to ``Pipfile.lock``, so that
   no credentials need to be stored in the version control.

.. _pipenv_lock:

``lock``
--------

``pipenv lock`` generates the file ``Pipfile.lock`` that lists all the
dependencies and sub-dependencies of your project including the latest available
versions and the current hash values for the downloaded files. This ensures
repeatable and, above all, deterministic builds.

.. note::
   In order to increase the determinism, the installation sequence can also be
   guaranteed in addition to the hash values. The  ``--sequential`` flag is used
   for this.

Security features
~~~~~~~~~~~~~~~~~

``pipfile.lock`` uses some security enhancements from ``pip``: by default,
sha256 hashes are generated for each downloaded package.

We strongly recommend ``lock`` using to deploy development environments to
production. In the development environment you use ``pipenv lock`` to compile
your dependencies and then you can use the compiled file ``Pipfile.lock`` in the
production environment for reproducible builds.

``open``
--------

``pipenv open MODULE`` shows a specific module in your editor.

If you use ´PyCharm <https://www.jetbrains.com/pycharm/>`_, you have to
configure ``pipenv`` for your Python project. How to do this is described in
`Configuring Pipenv Environment
<https://www.jetbrains.com/help/pycharm/pipenv.html>`_.

``run``
-------

``pipenv run`` spawns a command that is installed in the virtual environment,
for example:

    $ pipenv run python main.py

``shell``
---------

``pipenv shell`` spawns a shell in the virtual environment. This gives you a
Python interpreter that contains all Python packages and is therefore ideal for
debugging and testing, for example:

.. code-block:: console

    $ pipenv shell --fancy
    Launching subshell in virtual environment…
    bash-4.3.30$ python
    Python 3.6.4 (default, Jan  6 2018, 11:51:59)
    >>> import requests
    >>>

.. note::
   Shells are usually not configured so that a subshell can be used. This can
   lead to unexpected results. In these cases ``pipenv shell`` should be used
   instead of ``pipenv shell --fancy`` as this uses a compatibility mode.

``sync``
--------

``pipenv sync`` installs all packages specified in ``Pipfile.lock``.

``uninstall``
-------------

``pipenv uninstall`` uninstalls all provided packages and removes them from the
``Pipfile``. ``uninstall`` supports all parameters of `install <#install>`_ plus
the following two options:

``--all``
    deletes all files from the virtual environment, but leaves the ``Pipfile``
    untouched.
``--all-dev``
    removes all development packages from the virtual environment and removes
    them from the ``Pipfile``.

.. _pipenv_update:

``update``
----------

``pipenv update`` runs first ``pipenv lock``, then ``pipenv sync``.

``pipenv update`` has the following options:

``--clear``
    clears the *dependency cache*.
``--outdated``
    lists obsolete dependencies.
