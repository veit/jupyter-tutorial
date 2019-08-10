:HTML: `jupyter-tutorial.readthedocs.io <https://jupyter-tutorial.readthedocs.io/>`_
:PDF: `jupyter-tutorial.pdf <https://buildmedia.readthedocs.org/media/pdf/jupyter-tutorial/latest/jupyter-tutorial.pdf>`_
:Quellcode: `github.com/veit/jupyter-tutorial <https://github.com/veit/jupyter-tutorial/>`_
:Lizenz: `BSD 3-Clause <https://github.com/veit/jupyter-tutorial/blob/master/LICENSE>`_

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

    $ pipenv shell
    Launching subshell in virtual environment…
    $ bash-3.2$  . /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/activate
    $ (jupyter-tutorial) bash-3.2$ cd docs/
    $ (jupyter-tutorial) bash-3.2$ make latexpdf

   Das PDF findet ihr anschließend in ``docs/_build/latex/jupytertutorial.pdf``.

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehle ich euch,
mit einen *Fork* eure eigene Version zu erstellen. Ich akzeptiere auch
Pull-Requests, wenn diese klein und atomar sind sowie meine eigene Erfahrung
verbessern.

