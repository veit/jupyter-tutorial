``prettier``
============

`prettier <https://prettier.io/>`_ bietet automatische Formatierer für andere
Dateitypen, u.a. für `TypeScript <https://www.typescriptlang.org/>`_, `JSON
<https://json.org/>`_, `Vue <https://vuejs.org/>`_, `YAML <https://yaml.org/>`_,
`TOML
<https://github.com/bd82/toml-tools/tree/master/packages/prettier-plugin-toml>`_
und `XML <https://github.com/prettier/plugin-xml>`_ an.

Installation
------------

.. code-block:: console

    $ npm install prettier --save-dev --save-exact

Konfiguration
--------------

.. code-block:: console

    $ npx prettier --write path/to/my/file.js

Pre-commit-Hook für ``prettier``
--------------------------------

Installation
~~~~~~~~~~~~
.. code-block:: console

    $ npm install pretty-quick husky --save-dev

Konfiguration
~~~~~~~~~~~~~

In der ``package.json``-Datei kann der Pre-commit-Hook folgendermaßen
konfiguriert werden:

.. code-block:: json

    { "husky": { "hooks": { "pre-commit": "pretty-quick --staged" } } }

.. seealso::
    * `Prettier docs <https://prettier.io/docs/en/index.html>`_
