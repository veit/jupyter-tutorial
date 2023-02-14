Template for Git repositories
=============================

``pre-commit init-templatedir`` can be used to set up a template for Git’s
`init.templateDir <https://git-scm.com/docs/git-init#_template_directory>`_
option, whereby any newly cloned repository will automatically receive the
pre-commit hooks without having to run ``pre-commit install`` , for example:

.. code-block:: console

    $ git config --global init.templateDir ~/.config/git/template
    $ pre-commit init-templatedir ~/.config/git/template
    pre-commit installed at /Users/veit/.config/git/template/hooks/pre-commit
