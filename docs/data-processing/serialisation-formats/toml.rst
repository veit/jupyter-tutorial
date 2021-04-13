TOML
====

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| \+    | TOML (Tom’s Obvious, Minimal Language) supports most  |
|                       |       | common including strings, integers, floats and dates, |
|                       |       | but not references like :doc:`yaml` does.             |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | ++    | TOML is a formal strongly typed standard.             |
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | +-    | Partly with `JSON Schema Everywhere`_                 |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | ++    | TOML is a relatively new serialization format and     |
|                       |       | doesn’t have the same broad support as JSON, CSV or   |
|                       |       | XML for various programming languages.                |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | ++    | One of TOML’s primary goals was to be very easy to    |
|                       |       | read.                                                 |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | +-    | TOML can be processed at medium speed.                |
+-----------------------+-------+-------------------------------------------------------+
| File size             | \-    | Only :doc:`xml` is less compact.                      |
+-----------------------+-------+-------------------------------------------------------+

Example
-------

`pyproject.toml
<https://github.com/veit/jupyter-tutorial/blob/master/pyproject.toml>`_

.. code-block:: toml

    [tool.black]
    line-length = 79

    [tool.isort]
    atomic=true
    force_grid_wrap=0
    include_trailing_comma=true
    lines_after_imports=2
    lines_between_types=1
    multi_line_output=3
    not_skip="__init__.py"
    use_parentheses=true

    known_first_party="jupyter-tutorial"
    known_third_party=["mpi4py", "numpy", "requests"]

.. seealso::

    * `Home <https://toml.io/>`_
    * `GitHub <https://github.com/toml-lang/toml>`_
    * `Wiki <https://github.com/toml-lang/toml/wiki>`_
    * `What is wrong with TOML?
      <https://hitchdev.com/strictyaml/why-not/toml/>`_
    * `An INI critique of TOML
      <https://github.com/madmurphy/libconfini/wiki/An-INI-critique-of-TOML>`_

.. _`JSON Schema Everywhere`: https://json-schema-everywhere.github.io/toml
