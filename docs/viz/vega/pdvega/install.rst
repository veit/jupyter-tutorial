PdVega-Installation
===================

PdVega kann installiert werden mit

.. code-block:: console

    $ pipenv install pdvega
    Installing pdvega…
    Adding pdvega to Pipfile's [packages]…
    ✔ Installation Succeeded
    …
    $ pipenv run jupyter nbextension install --sys-prefix --py vega3
    Installing /srv/jupyter/.local/share/virtualenvs/python-374-c_ntaqVM/lib/python3.7/site-packages/vega3/static -> jupyter-vega3
    …
    - Validating: OK

        To initialize this nbextension in the browser every time the notebook (or other app) loads:
        
              jupyter nbextension enable vega3 --py --sys-prefix

.. seealso::
   * `Installing and Using pdvega
     <https://altair-viz.github.io/pdvega/installation.html#installation>`_

Abhängigkeiten
--------------

Um Plots als PNG oder SVG speichern zu können, müssen die
Kommandoheilenwerkzeuge ``vl2png`` und ``vl2svg`` aus dem `vega-lite
<https://github.com/vega/vega-lite>`_-npm-Paket vorhanden sein.

