Extensions
==========

Administration
--------------

`SQLAlchemy Admin for Starlette/FastAPI <https://github.com/aminalaee/sqladmin>`_
    Flexible admin interface for :doc:`/data-processing/postgresql/sqlalchemy`
    models.
`Piccolo Admin <https://github.com/piccolo-orm/piccolo_admin>`_
    Simple but powerful admin interface over Piccolo tables that lets you easily
    add, edit and filter your data

Authentication
--------------

`AuthX <https://github.com/yezz123/AuthX>`_
    Ready-to-use and customisable authentication and Oauth2 management
`FastAPI Security <https://github.com/jacobsvante/fastapi-security>`_
    Authentication and authorisation
`FastAPI simple security <https://github.com/mrtolkien/fastapi_simple_security>`_
    API key-based security package focused on ease of use
`FastAPI Users <https://github.com/fastapi-users/fastapi-users>`_
    Quickly adds a customisable registration and authentication system

ORMs
----

`FastAPI-SQLAlchemy <https://github.com/mfreeborn/fastapi-sqlalchemy>`_
    Easy integration between FastAPI,
    :doc:`/data-processing/postgresql/sqlalchemy` and application
`FastAPIwee <https://github.com/Ignisor/FastAPIwee>`_
    Easy way to create a REST API based on `PeeWee
    <https://github.com/coleifer/peewee>`_ models
`GINO <https://github.com/python-gino/gino>`_
    Lightweight asynchronous ORM built on SQLAlchemy Core for Python
    :doc:`asyncio </performance/asyncio-example>`, supporting PostgreSQL with
    `asyncpg <https://github.com/MagicStack/asyncpg>`_, and MySQL with `aiomysql
    <https://github.com/aio-libs/aiomysql>`_ (→ `example
    <https://github.com/leosussan/fastapi-gino-arq-uvicorn>`_)
`ORM <https://github.com/encode/orm>`_
    async ORM, which builds on SQLAlchemy Core, `Databases
    <https://github.com/encode/databases>`_ and `TypeSystem
    <https://github.com/encode/typesystem>`_
`ormar <https://github.com/collerek/ormar/>`_
    Asynchronous mini-ORM, with which you only need to maintain one set of
    models and migrate them with :doc:`/data-processing/postgresql/alembic` if
    necessary (→ `example <https://collerek.github.io/ormar/fastapi/>`__); it is
    also supported by `fastapi-users
    <https://github.com/fastapi-users/fastapi-users>`_, `fastapi-crudrouter
    <https://github.com/awtkns/fastapi-crudrouter>`_ and `fastapi-pagination
    <https://github.com/uriyyo/fastapi-pagination>`_
`Piccolo <https://github.com/piccolo-orm/piccolo>`_
    Fast, user-friendly ORM and query builder that supports Asyncio (→ `examples
    <https://github.com/piccolo-orm/piccolo_examples>`__)
`Prisma Client Python <https://github.com/RobertCraigie/prisma-client-py>`_
    Building on the TypeScript ORM `Prisma
    <https://github.com/prisma/prisma>`_ with support for PostgreSQL, MySQL,
    SQLite, MongoDB and SQL Server (→ `Example
    <https://github.com/RobertCraigie/prisma-client-py/tree/main/examples/fastapi-basic>`__)
`Tortoise ORM <https://github.com/tortoise/tortoise-orm>`_
    Easy-to-use asyncio ORM inspired by Django (→ `examples
    <https://tortoise.github.io/examples/fastapi.html>`__); `Aerich
    <https://github.com/tortoise/aerich>`_ is a database migration tool for
    Tortoise ORM.
`SQLModel <https://github.com/tiangolo/sqlmodel>`_
    Library for the interaction of SQL databases with Python objects

SQL Query Builders
------------------

`asyncpgsa <https://github.com/CanopyTax/asyncpgsa>`_
    Python wrapper around `asyncpg <https://github.com/MagicStack/asyncpg>`_ for
    use with :doc:`/data-processing/postgresql/sqlalchemy`
`Databases <https://github.com/encode/databases>`_
    Simple asyncio support for the database drivers `asyncpg
    <https://github.com/MagicStack/asyncpg>`_, `aiopg
    <https://github.com/aio-libs/aiopg>`_, `aiomysql
    <https://github.com/aio-libs/aiomysql>`_, `asyncmy
    <https://github.com/long2ice/asyncmy>`_ and `aiosqlite
    <https://github.com/omnilib/aiosqlite>`_

ODMs
----

`Beanie <https://github.com/roman-right/beanie>`_
    Asynchronous Python object document mapper (ODM) for MongoDB, based on
    `Motor <https://motor.readthedocs.io/en/stable/>`_ and `Pydantic
    <https://pydantic-docs.helpmanual.io/>`__
`MongoEngine <https://github.com/MongoEngine/mongoengine>`_
    Python Object-Document Mapper for working with MongoDB
`ODMantic <https://github.com/art049/odmantic/>`_
    Asynchronous ODM (Object Document Mapper) for MongoDB based on Python type
    hints and `pydantic <https://pydantic-docs.helpmanual.io/>`__

Code generators
---------------

`fastapi-code-generator <https://github.com/koxudaxi/fastapi-code-generator>`_
    Code generator creates a FastAPI application from an openapi file, using
    `datamodel-code-generator
    <https://github.com/koxudaxi/datamodel-code-generator>`_ to generate the
    pydantic model
`FastAPI-based API Client Generator <https://github.com/dmontagu/fastapi_client>`_
    mypy- and IDE-friendly API client from an OpenAPI specification using the
    `OpenAPI Generator
    <https://github.com/OpenAPITools/openapi-generator>`_

Utilities
---------

Caching
~~~~~~~

`FastAPI Cache <https://github.com/comeuplater/fastapi_cache>`_
    Lightweight cache system
`fastapi-cache <https://github.com/long2ice/fastapi-cache>`_
    Caching of fastapi responses and function results, with backends supporting
    `redis`, `memcache` and `dynamodb`

E-mail
~~~~~~

`Fastapi-mail <https://github.com/sabuhish/fastapi-mail>`_
    Easy mail system for sending e-mails and attachments, individually or in
    large quantities

GraphQL
~~~~~~~

`Strawberry GraphQL <https://github.com/strawberry-graphql/strawberry>`_
    Python GraphQL library based on data classes

Logging
~~~~~~~

`ASGI Correlation ID middleware <https://github.com/snok/asgi-correlation-id>`_
    Middleware to load or generate correlation IDs for each incoming request
`starlette context <https://github.com/tomwojcik/starlette-context>`_
    Middleware for Starlette that allows you to store and access the contextual data of a request.
    Middleware for Starlette that allows you to store and access the contextual
    data of a request

Prometheus
~~~~~~~~~~

`Prometheus FastAPI Instrumentator <https://github.com/trallnag/prometheus-fastapi-instrumentator>`_
    Configurable and modular Prometheus instrumentator
`starlette_exporter <https://github.com/stephenhillier/starlette_exporter>`_
    Prometheus export programme for Starlette and FastAPI
`Starlette Prometheus <https://github.com/perdy/starlette-prometheus>`_
    Prometheus integration for Starlette

Templating
~~~~~~~~~~

`fastapi-jinja <https://github.com/AGeekInside/fastapi-jinja>`_
    Integration of the Jinja template language
`fastapi-chameleon <https://github.com/mikeckennedy/fastapi-chameleon>`_
    Integration of the template language Chameleon

Pagination
~~~~~~~~~~

`FastAPI Pagination <https://github.com/uriyyo/fastapi-pagination>`_
    Easy-to-use pagination for FastAPI with integration in sqlalchemy, gino,
    databases and ormar, among others

Websockets
~~~~~~~~~~

`fastapi-socketio <https://github.com/pyropy/fastapi-socketio>`_
    Easy integration of `socket.io in <https://socket.io/>`_ into your FastAPI
    application
`FastAPI Websocket Pub/Sub <https://github.com/permitio/fastapi_websocket_pubsub>`_
    Fast and permanent pub/sub channel via websockets
`FASTAPI Websocket RPC <https://github.com/permitio/fastapi_websocket_rpc>`_
    Fast and permanent bidirectional JSON RPC channel via websockets

Other tools
-----------

`Pydantic-SQLAlchemy <https://github.com/tiangolo/pydantic-sqlalchemy>`_
    Creating Pydantic models from SQLAlchemy models
`Fastapi Camelcase <https://github.com/nf1s/fastapi-camelcase>`_
    Provision of a class of request and response bodies for FastAPI
`fastapi_profiler <https://github.com/sunhailin-Leo/fastapi_profiler>`_
    FastAPI middleware based on `pyinstrument
    <https://github.com/joerick/pyinstrument>`_ for performance testing
`fastapi-versioning <https://github.com/DeanWay/fastapi-versioning>`_
    API versioning for FastAPI web applications
`Jupter Notebook REST API <https://github.com/Invictify/Jupter-Notebook-REST-API>`_
    Run Jupyter notebooks as REST API endpoint
`manage-fastapi <https://github.com/ycd/manage-fastapi>`_
    Project generator and manager for FastAPI
`msgpack-asgi <https://github.com/florimondmanca/msgpack-asgi>`_
    Automatic negotiation of MessagePack content in ASGI applications
`fastapi-plugins <https://github.com/madkote/fastapi-plugins>`_
    Production-ready plug-ins for the FastAPI framework, including for caching
    with memcached or Redis, scheduler, configuration and logging
`fastapi-serviceutils <https://github.com/skallfass/fastapi_serviceutils>`_
    Optimised logging, exception handling and configuration
