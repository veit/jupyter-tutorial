pre-commit
==========

`pre-commit <https://pre-commit.com/>`_ ist ein Framework zum Verwalten von
Pre-commit-Hooks.

Installation
------------

Die Installation kann mit :doc:`/productive/envs/spack/index` erfolgen, z.B.:

.. code-block:: console

    $ spack env activate python-374
    $ spack install py-pre-commit ^python@3.7.4

Konfiguration
-------------

Pre-commit wird konfiguriert in ``pre-commit-config.yaml``, z.B.:

.. code-block:: yaml

    repos:
      - repo: https://github.com/psf/black
        rev: 19.10b0
        hooks:
          - id: black
            language_version: python3.7
            # override until resolved: https://github.com/ambv/black/issues/402
        files: \.pyi?$
            types: []

      - repo: https://gitlab.com/pycqa/flake8
        rev: 3.7.9
        hooks:
          - id: flake8
            language_version: python3.7

      - repo: https://github.com/asottile/seed-isort-config
        rev: v1.9.4
        hooks:
          - id: seed-isort-config

      - repo: https://github.com/pre-commit/mirrors-isort
        rev: v4.3.21
        hooks:
          - id: isort
            additional_dependencies: [toml]
            language_version: python3.7

      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.4.0
        hooks:
          - id: trailing-whitespace
          - id: end-of-file-fixer
          - id: debug-statements
