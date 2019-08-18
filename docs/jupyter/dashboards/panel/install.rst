Installation
============

Ihr könnt Panel in der virtuellen Umgebung eurer Jupyter-Kernels installieren
mit:

.. code-block:: console

    veit$ pipenv install panel
    Installing panel…
    Collecting panel
    …
    Installing collected packages: param, pyviz-comms, pyct, markdown, bokeh, panel
    Successfully installed bokeh-1.3.4 markdown-3.1.1 panel-0.6.2 param-1.9.1 pyct-0.4.6 pyviz-comms-0.7.2
    …

Für einige der unten genannten Beispiele werden zusätzliche Pakete benötigt wie
z.B. `Holoviews <http://holoviews.org/>`_ und `hvPlot
<https://hvplot.pyviz.org/>`_. Sie können installiert werden mit:

.. code-block:: console

    $ pipenv install "holoviews[recommended]"
    Installing holoviews[recommended]…
    …
    Installing collected packages: param, pyviz-comms, kiwisolver, cycler, pyparsing, matplotlib, pyct, markdown, packaging, bokeh, panel, holoviews
    Successfully installed bokeh-1.3.4 cycler-0.10.0 holoviews-1.12.5 kiwisolver-1.1.0 markdown-3.1.1 matplotlib-3.1.1 packaging-19.1 panel-0.6.2 param-1.9.1 pyct-0.4.6 pyparsing-2.4.2 pyviz-comms-0.7.2
    …
    $ pipenv install hvplot
    Installing hvplot…
    Collecting hvplot
    …
    Installing collected packages: hvplot
    Successfully installed hvplot-0.4.0
    …

Beispiele herunterladen
-----------------------

.. code-block:: console

    $ pipenv run panel examples
    Copied examples to /Users/veit/jupyter-tutorial/panel-examples

