FastAPI
=======

FastAPI is a web framework for building APIs with Python 3.6+ based type hints.

Key features are:

* very high performance thanks to `pydantic
  <https://pydantic-docs.helpmanual.io/>`_ for the data part and `Starlette
  <https://www.starlette.io/>`_ for the web part.

* fast and easy to code
* validation for most Python data types, including

  * JSON objects (``dict``)
  * JSON array (``list``)
  * string (``str``), defining min and max length
  * numbers (``int``, ``float``) with min and max values, etc.
  * URLs
  * email with `python-email-validator
    <https://github.com/JoshData/python-email-validator>`_
  * UUID
  * … and others

* robust, production-ready code with automatic interactive documentation
* based on the open standards for APIs: `OpenAPI <https://www.openapis.org/>`_
  formerly known as Swagger) and `JSON Schema <http://json-schema.org/>`_

.. seealso::
    * `Home <https://fastapi.tiangolo.com/>`_
    * `GitHub <https://github.com/tiangolo/fastapi>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    example
