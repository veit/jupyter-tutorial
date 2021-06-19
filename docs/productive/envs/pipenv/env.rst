Environment variables
=====================

``pipenv`` environment variables
--------------------------------

``pipenv --envs`` outputs options of the environment variables.

For more information, see `Configuration With Environment Variables
<https://docs.pipenv.org/advanced/#configuration-with-environment-variables>`_.

``.env`` file
-------------

If an ``.env`` file exists in your virtual environment, ``$ pipenv shell`` and
``$ pipenv run`` will automatically load it:

.. code-block:: console

    $ cat .env
    USERNAME=Veit⏎

    $ pipenv run python
    Loading .env environment variables…
    …
    >>> import os
    >>> os.environ['USERNAME']
    'Veit'

The credentials, e.g. of the version management, can also be specified in the
``Pipfile``, e.g.:

.. code-block:: ini

    [[source]]
    url = "https://$USERNAME:${PASSWORD}@pypi.cusy.io/simple"
    verify_ssl = true
    name = "cusy-pypi"

.. note::
   ``pipenv`` hashes the ``Pipfile`` before determining the environment
   variables, and the environment variables are also written in
   ``Pipfile.lock``, so that no credentials need to be stored in the version
   management.

You can also save the ``.env`` file outside your virtual environment. You then
only have to specify the path to this file in ``PIPENV_DOTENV_LOCATION``:

.. code-block:: console

    $ PIPENV_DOTENV_LOCATION=/path/to/.env pipenv shell

You can also prevent ``pipenv`` from using an existing ``.env`` file with:

.. code-block:: console

    $ PIPENV_DONT_LOAD_ENV=1 pipenv shell
