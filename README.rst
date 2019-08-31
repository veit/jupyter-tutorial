|Contributors| |License| |Docs|

.. |Contributors| image:: https://img.shields.io/github/contributors/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/graphs/contributors
.. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE
.. |Docs| image:: https://readthedocs.org/projects/jupyter-tutorial/badge/?version=latest
   :target: https://jupyter-tutorial.readthedocs.io/de/latest/

Installation
------------

#. Herunterladen und Auspacken:

   .. code-block:: console

    $ curl -O https://github.com/veit/jupyter-tutorial/archive/master.zip
    $ unzip master.zip

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

#. ``nbextension`` installieren und aktivieren:

   .. code-block:: console

    $ pipenv run jupyter nbextension install --py latex_envs --user
    …
    $ pipenv run jupyter nbextension enable latex_envs --user --py
    Enabling notebook extension latex_envs/latex_envs...
          - Validating: OK

#. HTML-Dokumentation erstellen:

   .. code-block:: console

    $ pipenv run sphinx-build -b html docs/ docs/_build/

#. PDF erstellen:

   .. code-block:: console

    $ cd docs/
    $ pipenv run make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   Das PDF findet ihr anschließend in ``docs/_build/latex/jupytertutorial.pdf``.

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehle ich euch,
mit einen *Fork* eure eigene Version zu erstellen. Ich akzeptiere auch
Pull-Requests, wenn diese klein und atomar sind sowie meine eigene Erfahrung
verbessern.

