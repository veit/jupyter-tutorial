pre-commit scripts
==================

`pre-commit-hooks <https://github.com/pre-commit/pre-commit-hooks>`_
    The pre-commit framework already comes with a whole range of scripts,
    including:

    ``check-added-large-files``
        prevents large files from being transferred
    ``check-case-conflict``
        looks for files that would conflict in case-insensitive file systems
    ``check-executables-have-shebangs``
        makes sure that (non-binary) executables have a shebang line
    ``check-shebang-scripts-are-executable``
        makes sure (non-binary) files are executable with a shebang line
    ``check-symlinks``
        checks for symlinks that don’t point to anything
    ``destroyed-symlinks``
        detects symlinks that have been changed into regular files with the
        contents of the path the symlink points to.

`pygrep-hooks <https://github.com/pre-commit/pygrep-hooks>`_
    provides regular expressions for Python and reStructuredText, including:

    ``python-no-log-warn``
        search for the deprecated ``.warn()`` method of Python loggers
    ``python-use-type-annotations``
        forces type-annotations to be used instead of type-comments
    ``rst-backticks``
        detects the use of single backticks when writing reStructuredText
    ``rst-directive-colons``
        detects that reStructuredText directives do not end with a colon or a
        space before the colon
    ``rst-inline-touching-normal``
        detects that inline code is used in normal text in reStructuredText
    ``text-unicode-replacement-char``
        prevents files that contain UTF-8 Unicode Replacement Characters

Linters and formatters
    They are provided in separate repositories, including:

    `autopep8 <https://github.com/pre-commit/mirrors-autopep8>`_
        provides `autopep8 <https://github.com/hhatto/autopep8>`__ for the
        pre-commit framework
    `mypy <https://github.com/pre-commit/mirrors-mypy>`_
        provides `mypy <https://github.com/python/mypy>`__
    `clang-format <https://github.com/pre-commit/mirrors-clang-format>`_
        provides `clang-format-wheel
        <https://github.com/ssciwr/clang-format-wheel>`__
    `csslint <https://github.com/pre-commit/mirrors-csslint>`_
        provides `csslint <https://github.com/CSSLint/csslint>`__
    `scss-lint <https://github.com/pre-commit/mirrors-scss-lint>`_
        provides `scss-lint <https://github.com/sds/scss-lint>`__
    `eslint <https://github.com/pre-commit/mirrors-eslint>`_
        provides `eslint <https://github.com/eslint/eslint>`__
    `fixmyjs <https://github.com/pre-commit/mirrors-fixmyjs>`_
        provides `fixmyjs <https://github.com/jshint/fixmyjs>`__
    `prettier <https://github.com/pre-commit/mirrors-prettier>`_
        provides `prettier <https://github.com/prettier/prettier>`__

`black <https://github.com/psf/black>`_
    for formatting Python code

    ``black``
        Python code formatter
    ``black-jupyter``
        Python code formatter for Jupyter notebooks

Python Code Quality Authority
    Code quality tools (and plugins) for the Python programming language:

    `flake8 <https://github.com/PyCQA/flake8>`_
        promotes the enforcement of a consistent Python style
    `autoflake <https://github.com/PyCQA/autoflake>`_
        removes unused imports and unused variables from Python code
    `bandit <https://github.com/PyCQA/bandit>`_
        tool for finding security vulnerabilities in Python code
    `pydocstyle <https://github.com/PyCQA/pydocstyle>`_
        static analysis tool to check compliance with Python docstring
        conventions
    `docformatter <https://github.com/PyCQA/docformatter>`_
        formats docstrings according to :pep:`257`
    `pylint <https://github.com/PyCQA/pylint>`_
        Python linter
    `doc8 <https://github.com/PyCQA/doc8>`_
        executes doc8 for linting documents
    `prospector <https://github.com/PyCQA/prospector>`_
        analyses Python code with prospector
    `isort <https://github.com/PyCQA/isort>`_
        sorts Python imports

`nbQA <https://github.com/nbQA-dev/nbQA>`_
    runs isort, pyupgrade, mypy, pylint, flake8 and more on Jupyter notebooks:

    ``nbqa``
        runs any standard Python code quality tool on a Jupyter notebook
    ``nbqa-black``
        runs ``black`` on a Jupyter notebook
    ``nbqa-check-ast``
        runs ``check-ast`` on a Jupyter notebook
    ``nbqa-flake8``
        runs ``flake8`` on a Jupyter notebook
    ``nbqa-isort``
        runs ``isort`` on a Jupyter notebook
    ``nbqa-mypy``
        runs ``mypy`` on a Jupyter notebook
    ``nbqa-pylint``
        runs ``pylint`` on a Jupyter notebook
    ``nbqa-pyupgrade``
        runs ``ppyupgrade`` on a Jupyter notebook
    ``nbqa-yapf``
        runs ``yapf`` on a Jupyter notebook
    ``nbqa-autopep8``
        runs ``autopep8`` on a Jupyter notebook
    ``nbqa-pydocstyle``
        runs ``pydocstyle`` on a Jupyter notebook
    ``nbqa-ruff``
        runs ``ruff`` on a Jupyter notebook

`blacken-docs <https://github.com/adamchainz/blacken-docs>`_
    applies ``black`` to Python code blocks in documentation files

Miscellaneous

`pyupgrade <https://github.com/asottile/pyupgrade>`_
    automatically updates the syntax for newer versions
`reorder-python-imports <https://github.com/asottile/reorder_python_imports>`_
    reorders imports into Python files
`dead <https://github.com/asottile/dead>`_
    detects dead Python code
`python-safety-dependencies-check <https://github.com/Lucas-C/pre-commit-hooks-safety>`_
    analyses Python requirements for known security vulnerabilities
`gitlint <https://github.com/jorisroovers/gitlint>`_
    Git commit message linter
`nbstripout <https://github.com/kynan/nbstripout>`_
    removes the output of Jupyter Notebooks
`detect-secrets <https://github.com/Yelp/detect-secrets>`_
    detects high entropy strings that are likely to be passwords
`pip-compile <https://github.com/jazzband/pip-tools>`_
    automatically compiles requirements
`kontrolilo <https://github.com/kontrolilo/kontrolilo>`_
    Tool to control licences for OSS dependencies

.. seealso::
    * `Supported hooks <https://pre-commit.com/hooks.html>`_
