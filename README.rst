Schnelleinstieg
===============

|Contributors| |License| |Docs| |Pyup|

.. |Contributors| image:: https://img.shields.io/github/contributors/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/graphs/contributors
.. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE
.. |Docs| image:: https://readthedocs.org/projects/jupyter-tutorial/badge/?version=latest
   :target: https://jupyter-tutorial.readthedocs.io/de/latest/
.. |Pyup| image:: https://pyup.io/repos/github/veit/jupyter-tutorial/shield.svg
   :target: https://pyup.io/repos/github/veit/jupyter-tutorial/

.. first-steps::

Installation
------------

#. Herunterladen und Auspacken:

   .. code-block:: console

    $ curl -O https://codeload.github.com/veit/jupyter-tutorial/zip/master
    $ unzip master
    Archive:  master
    …
       creating: jupyter-tutorial-master/
    …

#. Pipenv installieren

   Siehe :doc:`Pipenv installieren </productive/envs/pipenv/install>`

#. Python-Pakete installieren:

   .. code-block:: console

    $ cd jupyter-tutorial
    $ pipenv install
    Creating a virtualenv for this project…
    …
    Installing dependencies from Pipfile.lock (fbb457)…
    …
    $ pipenv run jupyter nbextension enable highlighter/highlighter
        Enabling notebook extension highlighter/highlighter...
              - Validating: OK

#. Javascript- und CSS-Dateien der `Jupyter Notebook Extensions
   <https://jupyter-contrib-nbextensions.readthedocs.io/>`_ installieren

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

#. HTML-Dokumentation erstellen:

   .. code-block:: console

    $ python3 -m venv .
    $ bin/python -m pip install --upgrade pip
    $ bin/python -m pip install -r docs/constraints.txt
    $ bin/sphinx-build -ab html docs/ docs/_build/

#. PDF erstellen:

   Für die Erstellung von PDFs benötigt ihr weitere Pakete.

   Für Debian/Ubuntu erhaltet ihr diese mit:

   .. code-block:: console

    $ apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   oder für Mac OS X mit:

   .. code-block:: console

    $ brew cask install mactex
    …
    🍺  mactex was successfully installed!
    $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
    $ sudo texlua install-getnonfreefonts
    …
    mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
    mktexlsr: Done.

   Anschließend könnt ihr ein PDF generieren mit:

   .. code-block:: console

    $ cd docs/
    $ pipenv run make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   Das PDF findet ihr anschließend in ``docs/_build/latex/jupytertutorial.pdf``.

Folge uns
---------

* `GitHub <https://github.com/veit/jupyter-tutorial>`_
* `Twitter <https://twitter.com/JupyterTutorial>`_
* `Mastodon <https://mastodon.social/web/accounts/1089854>`_

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehle ich euch,
einen `Fork <https://github.com/veit/jupyter-tutorial/fork>`_ meines
`GitHub-Repository <https://github.com/veit/jupyter-tutorial/>`_ zu erstellen
und darin eure Änderungen vorzunehmen. Gerne dürft ihr auch einen *Pull Request*
stellen. Sofern die darin enthaltenen Änderungen klein und atomar sind, schaue ich
mir eure Vorschläge gerne an.

