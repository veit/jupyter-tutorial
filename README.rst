Jupyter-Tutorial
================

* Dokumentation: https://jupyter-tutorial.readthedocs.io/de/latest/
* PDF: https://buildmedia.readthedocs.org/media/pdf/jupyter-tutorial/latest/jupyter-tutorial.pdf
* GitHub-Repo: https://github.com/veit/jupyter-tutorial/
* Lizenz: BSD license

Installation
------------

#. Herunterladen und Auspacken:

    $ curl -O https://github.com/veit/jupyter-tutorial/archive/master.zip
    $ unzip master.zip

#. Sphinx installieren:

    $ cd jupyter-tutorial
    $ pipenv install

#. HTML-Dokumentation erstellen:

    $ pipenv run sphinx-build -b html docs/ docs/_build/

#. PDF erstellen:

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

