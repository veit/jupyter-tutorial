Quick start
===========

.. _badges:

Status
------

.. image:: https://img.shields.io/github/contributors/veit/jupyter-tutorial.svg
   :alt: Contributors
   :target: https://github.com/veit/jupyter-tutorial/graphs/contributors
.. image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :alt: License
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE
.. image:: https://results.pre-commit.ci/badge/github/veit/jupyter-tutorial/main.svg
   :alt: pre-commit.ci status
   :target: https://results.pre-commit.ci/latest/github/veit/jupyter-tutorial/main
.. image:: https://readthedocs.org/projects/jupyter-tutorial/badge/?version=latest
   :alt: Docs
   :target: https://jupyter-tutorial.readthedocs.io/en/latest/
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.10961038.svg
   :alt: DOI
   :target: https://doi.org/10.5281/zenodo.10961038
.. image:: https://img.shields.io/badge/dynamic/json?label=Mastodon&query=totalItems&url=https%3A%2F%2Fmastodon.social%2F@JupyterTutorial%2Ffollowers.json&logo=mastodon
   :alt: Mastodon
   :target: https://mastodon.social/@JupyterTutorial

.. _first-steps:

Installation
------------

#. Download and unpack:

   .. code-block:: console

    $ curl -O https://codeload.github.com/veit/jupyter-tutorial/zip/main
    $ unzip main
    Archive:  main
    …
       creating: jupyter-tutorial-main/
    …

#. Install Python packages:

   .. code-block:: console

      $ cd jupyter-tutorial-main
      $ python3 -m venv .venv
      $ . .venv/bin/activate
      $ python -m pip install --upgrade pip
      $ python -m pip install -e ".[dev]"

#. Install the `Jupyter Notebook Extensions
   <https://jupyter-contrib-nbextensions.readthedocs.io/>`_ Javascript and CSS
   files:

   .. code-block:: console

    $ jupyter contrib nbextension install --user
    jupyter contrib nbextension install --user
    Installing jupyter_contrib_nbextensions nbextension files to jupyter data directory
    …
    Successfully installed jupyter-contrib-core-0.3.3 jupyter-contrib-nbextensions-0.5.1
    jupyter-highlight-selected-word-0.2.0 jupyter-latex-envs-1.4.6
    jupyter-nbextensions-configurator-0.4.1
    …
    $ jupyter nbextension enable latex_envs --user --py
    Enabling notebook extension latex_envs/latex_envs...
          - Validating: OK

#. Create HTML documentation:

   Note that pandoc has to be installed. On Debian/Ubuntu you can just run

   .. code-block:: console

    $  sudo apt install pandoc

   To create the HTML documentation run these commands:

   .. code-block:: console

    $ cd docs/
    $ make html

#. Create a PDF:

   For the creation of a PDF file you need additional packages.

   For Debian/Ubuntu you get them with the following command:

   .. code-block:: console

    $ sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   or for macOS with:

   .. code-block:: console

    $ brew cask install mactex
    …
    🍺  mactex was successfully installed!
    $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
    $ sudo texlua install-getnonfreefonts
    …
    mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
    mktexlsr: Done.

   Then you can generate a PDF with:

   .. code-block:: console

    $ make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   You can find the PDF at ``docs/_build/latex/jupytertutorial.pdf``.

#. Run Vale to check spelling

   You can install download cusy-vale with:

   .. code-block:: console

      $ vale sync
      Syncing cusy-vale [1/1] ██████████████████████████████████████████████ 100% | 0s
       SUCCESS  Synced 1 package(s) to '/Users/veit/cusy/trn/jupyter-tutorial/styles'.

   .. seealso::
      * `Vale installation <https://docs.errata.ai/vale/install>`_
      * `Vale formats <https://docs.errata.ai/vale/scoping#formats>`_

   Now you can check the RestructuredText files with:

   .. code-block:: console

    $ vale .
    ✔ 0 errors, 0 warnings and 0 suggestions in 201 files.

.. _follow-us:

Follow us
---------

* `GitHub <https://github.com/veit/jupyter-tutorial>`_
* `Twitter <https://twitter.com/JupyterTutorial>`_
* `Mastodon <https://mastodon.social/@JupyterTutorial>`_

Pull-Requests
-------------

If you have suggestions for improvements and additions, I recommend that you
create a `Fork <https://github.com/veit/jupyter-tutorial/fork>`_ of my `GitHub
Repository <https://github.com/veit/jupyter-tutorial/>`_ and make your changes
there. . You are also welcome to make a *pull request*. If the changes
contained therein are small and atomic, I’ll be happy to look at your
suggestions.
