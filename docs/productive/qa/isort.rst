``isort``
=========

`isort <https://github.com/timothycrosley/isort>`_ formats your ``import``
statements in separate and sorted blocks.

Installation
------------

.. code-block:: console

    $ pipenv install isort

Configuration
-------------

``isort`` can be configured for example in the ``pyproject.toml`` file:

.. code-block:: ini

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

In order to recognise third-party packages for your project imports, you can
install your project together with ``isort``.

.. note::
    With isort 5 you can use profiles. This simplifies the configuration of
    isort in order to continue to play with :doc:`black` in the future:

    .. code-block:: ini

        isort --profile black .
