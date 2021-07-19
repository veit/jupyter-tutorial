Codecov
=======

Codecov collects coverage reports for Python, C#/.net, Java,
Node/Javascript/Coffee, C/C++, D, Go, Groovy, Kotlin, PHP, R, Scala, Xterm,
Xcode, Lua, and other languages, then submits them to `codecov.io
<https://about.codecov.io/>`_

.. seealso::
   * `GitHub <https://github.com/codecov/codecov-python>`_
   * `Docs <https://docs.codecov.io/docs>`_

Installation
------------

Codecov can be easily installed with

.. code-block:: console

    $ pipenv install codecov

Use
---

… in Terminal
~~~~~~~~~~~~~

.. code-block:: console

    $ codecov -t <repository-upload-token>

.. _together-with-github-actions:

… together with GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To do this, you can add the following to your :file:`ci.yml` file, for example:

.. code-block:: yaml
   :emphasize-lines: 3-6

    - name: "Convert coverage"
      run: "python -m coverage xml"
    - name: "Upload coverage to Codecov"
      uses: "codecov/codecov-action@v1"
      with:
        fail_ci_if_error: true

.. seealso::
   * `Codecov GitHub Action <https://github.com/codecov/codecov-action>`_

… together with Travis CI
~~~~~~~~~~~~~~~~~~~~~~~~~

For this you can add the following in the ``.travis.yml`` file:

.. code-block:: yaml

    language:
      python
    after_success:
      - bash <(curl -s https://codecov.io/bash)

… together with ``tox``
~~~~~~~~~~~~~~~~~~~~~~~

Codecov can be set up with :doc:`../tox`:

.. code-block:: ini

    [testenv]
    passenv = TOXENV CI TRAVIS TRAVIS_* CODECOV_*
    deps = codecov>=1.4.0
    commands = codecov -e TOXENV

.. _codecov-badge:

Badge
-----

Finally, you can also add a badge for code coverage in your :file:`README.rst`
file, for example with:

   .. code-block::

    .. image:: https://codecov.io/gh/YOU/YOUR_PROJECT/branch/main/graph/badge.svg
       :target: https://codecov.io/gh/YOU/YOUR_PROJECT
       :alt: Code Coverage Status (Codecov)
