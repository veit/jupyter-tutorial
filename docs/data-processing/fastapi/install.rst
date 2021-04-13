Installation
============

Requirements
------------

.. code-block:: console

    $ pipenv install fastapi
    Adding fastapi to Pipfile's [packages]…
    ✔ Installation Succeeded
    Locking [dev-packages] dependencies…
    ✔ Success!
    Locking [packages] dependencies…
    ✔ Success!
    …

Optional requirements
~~~~~~~~~~~~~~~~~~~~~

For production you also need an `ASGI <https://asgi.readthedocs.io/en/latest/>`_
server, such as `uvicorn <http://www.uvicorn.org/>`_:

.. code-block:: console

    $ pipenv install uvicorn
    Adding uvicorn to Pipfile's [packages]…
    ✔ Installation Succeeded
    Locking [dev-packages] dependencies…
    ✔ Success!
    Locking [packages] dependencies…
    ✔ Success!
    Updated Pipfile.lock (051f02)!
    …

Pydantic can use the optional dependencies

`ujson <https://github.com/ultrajson/ultrajson>`_
    for faster JSON parsing.
`email_validator <https://github.com/JoshData/python-email-validator>`_
    for email validation.

Starlette can use the optional dependencies

:doc:`requests <../data/requests/index>`
    if you want to use the ``TestClient``.
`aiofiles <https://github.com/Tinche/aiofiles>`_
    if you want to use ``FileResponse`` or ``StaticFiles``.
`jinja2 <https://jinja.palletsprojects.com/>`_
    if you want to use the default template configuration.
`python-multipart <https://andrew-d.github.io/python-multipart/>`_
    if you want to support form parsing, with ``request.form()``.
`itsdangerous <https://pythonhosted.org/itsdangerous/>`_
    required for ``SessionMiddleware`` support.
`pyyaml <https://pyyaml.org/wiki/PyYAMLDocumentation>`_
    for Starlette’s ``SchemaGenerator`` support.
`graphene <https://graphene-python.org/>`_
    for ``GraphQLApp`` support.
`ujson <https://github.com/ultrajson/ultrajson>`__
    if you want to use ``UJSONResponse``.
`orjson <https://github.com/ijl/orjson>`_
    if you want to use ``ORJSONResponse``.

They can be installed, e.g. with:

.. code-block:: console

    $ pipenv install fastapi[ujson]

Alternatively you can install all of these with:

.. code-block:: console

    $ pipenv install fastapi[all]
