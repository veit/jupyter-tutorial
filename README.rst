Quick start
===========

.. badges::

Status
------

.. image:: https://img.shields.io/github/contributors/veit/jupyter-tutorial.svg
   :alt: Contributors
   :target: https://github.com/veit/jupyter-tutorial/graphs/contributors
.. image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :alt: License
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE
.. image:: https://readthedocs.org/projects/jupyter-tutorial/badge/?version=latest
   :alt: Docs
   :target: https://jupyter-tutorial.readthedocs.io/en/latest/
.. image:: https://pyup.io/repos/github/veit/jupyter-tutorial/shield.svg
   :alt: Pyup
   :target: https://pyup.io/repos/github/veit/jupyter-tutorial/
.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.4147287.svg
   :alt: DOI
   :target: https://zenodo.org/badge/latestdoi/199994535

.. first-steps::

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

#. Edit the ``Pipfile`` in the unpacked archive and enter your current Python version in this section:

  .. code-block:: console

    [requires]
    python_version = ""

#. Install Pipenv

   Refer to :doc:`Install Pipenv </productive/envs/pipenv/install>`

#. Install Python packages:

   .. code-block:: console

    $ cd jupyter-tutorial-main
    $ pipenv install
    Creating a virtualenv for this project…
    …
    Installing dependencies from Pipfile.lock (fbb457)…
    …
    $ pipenv run jupyter nbextension enable highlighter/highlighter
        Enabling notebook extension highlighter/highlighter...
              - Validating: OK

#. Install the `Jupyter Notebook Extensions
   <https://jupyter-contrib-nbextensions.readthedocs.io/>`_ Javascript and CSS
   files:

   .. code-block:: console

    $ pipenv run jupyter contrib nbextension install --user
    jupyter contrib nbextension install --user
    Installing jupyter_contrib_nbextensions nbextension files to jupyter data directory
    …
    Successfully installed jupyter-contrib-core-0.3.3 jupyter-contrib-nbextensions-0.5.1
    jupyter-highlight-selected-word-0.2.0 jupyter-latex-envs-1.4.6
    jupyter-nbextensions-configurator-0.4.1
    …
    $ pipenv run jupyter nbextension enable latex_envs --user --py
    Enabling notebook extension latex_envs/latex_envs...
          - Validating: OK

#. Create HTML documentation:

   Note that pandoc has to be installed. On Debian/Ubuntu you can just run

   .. code-block:: console

    $  sudo apt-get install pandoc

    To create the HTML documentation run these commands:

   .. code-block:: console

    $ python3 -m venv .
    $ bin/python -m pip install --upgrade pip
    $ bin/python -m pip install -r docs/constraints.txt
    $ bin/sphinx-build -ab html docs/ docs/_build/

#. Create a PDF:

   For the creation of a PDF file you need additional packages.

   For Debian/Ubuntu you get them with the following command:

   .. code-block:: console

    $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

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

    $ cd docs/
    $ pipenv run make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   You can find the PDF at ``docs/_build/latex/jupytertutorial.pdf``.

#. Install vnd run ale to check spelling

   You can install Vale with:

   .. code-block:: console

    $ brew install vale

   You can install the parser for Restructuredtext with:

   .. code-block:: console

    $ brew install docutils

   .. seealso::
      * `Vale installation <https://docs.errata.ai/vale/install>`_
      * `Vale formats <https://docs.errata.ai/vale/scoping#formats>`_

   Now you can check the RestructuredText files with:

   .. code-block:: console

    $ cd jupyter-tutorial
    $ vale docs/
    ✔ 0 errors, 0 warnings and 0 suggestions in 1 file.

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
