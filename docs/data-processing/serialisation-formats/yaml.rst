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
|                       |       | :doc:`json/index` and :doc:`toml`.                    |
+-----------------------+-------+-------------------------------------------------------+

Example
-------

`CITATION.cff <https://citation-file-format.github.io/>`_

.. code-block:: yaml

    # YAML 1.2
    ---
    cff-version: 1.1.0
    message: If you use this software, please cite it as below.
    authors:
      - family-names: Druskat
        given-names: Stephan
        orcid: https://orcid.org/0000-0003-4925-7248
    title: "My Research Software"
    version: 2.0.4
    doi: 10.5281/zenodo.1234
    date-released: 2017-12-18

.. seealso::

    * `Home <https://yaml.org/>`_
    * `Specification <https://yaml.org/spec/>`_
    * `YAML Validator <https://codebeautify.org/yaml-validator>`_
    * `StrictYAML <https://github.com/crdoconnor/strictyaml>`_
    * `noyaml.com <https://noyaml.com/>`_

.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: http://rx.codesimply.com/
