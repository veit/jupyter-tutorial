``prettier``
============

`prettier <https://prettier.io/>`_ offers automatic formatters for other file
types, including `TypeScript <https://www.typescriptlang.org/>`_, `JSON
<https://json.org/>`_, `Vue <https://vuejs.org/>`_, `YAML <https://yaml.org/>`_,
`TOML
<https://github.com/bd82/toml-tools/tree/master/packages/prettier-plugin-toml>`_
and `XML <https://github.com/prettier/plugin-xml>`_.

Installation
------------

.. code-block:: console

    $ npm install prettier --save-dev --save-exact

Configuration
-------------

.. code-block:: console

    $ npx prettier --write path/to/my/file.js

Pre-commit hook for ``prettier``
--------------------------------

Installation
~~~~~~~~~~~~
.. code-block:: console

    $ npm install pretty-quick husky --save-dev

Configuration
~~~~~~~~~~~~~

In the ``package.json`` file you can configure the pre-commit hook as follows:

.. code-block:: json

    { "husky": { "hooks": { "pre-commit": "pretty-quick --staged" } } }

.. seealso::
    * `Prettier docs <https://prettier.io/docs/en/index.html>`_
