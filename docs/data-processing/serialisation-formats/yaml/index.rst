YAML
====

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| ++    | YAML, short for *YAML Ain’t Markup Language*, supports|
|                       |       | most common data types including strings, integers,   |
|                       |       | floats and dates. YAML even supports references and   |
|                       |       | external data.                                        |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | \+    | YAML is a strongly tpyed formal standard, but it’s    |
|                       |       | hard to find schema validators.                       |
+-----------------------+-------+-------------------------------------------------------+
| Schema-IDL            | +-    | Partly with `Kwalify`_, `Rx`_ and built-in language   |
|                       |       | type defs.                                            |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | +-    | There be libraries for the most popular languages.    |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | \+    | Basic YAML is really easy to read, however YAML’s     |
|                       |       | complexity can confuse a reader.                      |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | -\-   | YAML is very slow to serialise and deserialise.       |
+-----------------------+-------+-------------------------------------------------------+
| File size             | +-    | YAML is in the medium range similar to                |
|                       |       | :doc:`../json/index` and :doc:`../toml/index`.        |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    * `Home <https://yaml.org/>`_
    * `Specification <https://yaml.org/spec/>`_
    * `YAML Validator <https://codebeautify.org/yaml-validator>`_
    * `StrictYAML <https://github.com/crdoconnor/strictyaml>`_
    * `noyaml.com <https://noyaml.com/>`_

.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: http://rx.codesimply.com/

 .. toctree::
     :hidden:
     :titlesonly:
     :maxdepth: 0

     example.ipynb
