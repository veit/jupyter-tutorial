Templating
==========

.. _voila-gridstack:

Voila-Gridstack
---------------

`gridstack.js <http://gridstackjs.com/>`_ ist ein jQuery-Plugin für
Widget-Layouts. Dies ermöglicht mehrspaltige Drag & Drop-Raster und anpassbare,
für `Bootstrap v3 <https://getbootstrap.com/docs/3.4/>`_ geeignete Layouts.
Zudem funktioniert es  mit `knockout.js <https://knockoutjs.com/>`_ und
Touch-Geräten.

Das Gridstack-Voilà-Template verwendet die Metadaten der Notebook-Zellen, um das
Layout des Notebooks zu gestalten. Es soll die gesamte Spezifikation für die
veralteten :doc:`../jupyter-dashboards/index`
unterstützen.

.. image:: voila-gridstack.png
   :scale: 53%
   :alt: Beispiel für Voilà-Gridstack

voila-vuetify
-------------

`voila-vuetify <https://github.com/QuantStack/voila-vuetify>`_ ist ein Template
zur Verwendung von Voilà mit dem `Material Design Component Framework
<https://material.io/>`_ `Vuetify.js <https://vuetifyjs.com/>`_.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install bqplot ipyvuetify voila-vuetify==voila-vuetify 0.0.1a8

Verwendung
~~~~~~~~~~

Um ``voila-vuetify`` in einem Notebook zu verwenden, müsst ihr zunächst
``ipyvuetify`` importieren:

.. code-block:: python

    import ipyvuetify as v

Anschließend könnt ihr ein Layout erstellen z.B mit:

.. code-block:: python

    v.Tabs(_metadata={'mount_id': 'content-main'}, children=[
        v.Tab(children=['Tab1']),
        v.Tab(children=['Tab2']),
        v.TabItem(children=[
            v.Layout(row=True, wrap=True, align_center=True, children=[
                v.Flex(xs12=True, lg6=True, xl4=True, children=[
                    fig, slider
                ]),
                v.Flex(xs12=True, lg6=True, xl4=True, children=[
                    figHist2, sliderHist2
                ]),
                v.Flex(xs12=True, xl4=True, children=[
                    fig2
                ]),
            ])
        ]),
        v.TabItem(children=[
            v.Container(children=['Lorum ipsum'])
        ])
    ])

:doc:`bqplot_vuetify_example`. könnt ihr nutzen mit:

.. code-block:: console

    $ pipenv run voila --template vuetify-default bqplot_vuetify_example.ipynb

Anschließend öffnet sich euer Standardbrowser mit der URL
``http://localhost:8866/`` und zeigt euch die Plots im Responsive Material
Design.

Beispiel für Voilà-vuetify mit der Monitorauflösung eines Laptop MDPI-Screen:

.. image:: voila-vuetify-laptop.png
   :scale: 53%

Beispiel für Voilà-vuetify mit der Monitorauflösung eine iPhone X:

.. image:: voila-vuetify-iphone.png
   :scale: 53%

voila-debug
-----------

`voila-debug <https://github.com/QuantStack/voila-debug>`_ ist ein Template zum
Anzeigen von Debug-Informationen bei der Arbeit an Voilà-Anwendungen.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install voila-debug

Verwendung
~~~~~~~~~~

Ihr könnt das Template :doc:`debug.ipynb` nutzen mit:

.. code-block:: console

    $ pipenv run voila --template=debug --VoilaExporter.template_file=debug.tpl

Dies öffnet euren Standardbrowser mit der URL ``localhost:8866``.

In
``http://localhost:8866/voila/render/docs/jupyter/dashboards/voila/debug.ipynb``
könnt ihr euch dann die Funktionsweise genauer anschauen.

.. image:: voila-debug.png
   :scale: 53%
   :alt: Beispiel für Voilà-Debug

Es enthält neben einem Beispiel-Widget eine Code-Zelle zum Beenden des Kernels:

.. code-block:: python

    import os

    def kill_kernel(change):
        os._exit(0)

    button = widgets.Button(description="Kill Kernel")
    button.on_click(kill_kernel)
    button

Eigene Templates erstellen
--------------------------

Ein Voilà-Template ist ein Ordner, der sich im Virtual-environment unter
``share/jupyter/voila/templates`` befindet und z.B. Folgendes enthält:

.. code-block:: console

    /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/share/jupyter/voila/templates/mytheme
    ├── conf.json
    ├── nbconvert_templates
    │   └── voila.tpl
    ├── static
    │   ├── mytheme.js
    │   └── mytheme.css
    └── templates
        ├── 404.html
        ├── browser-open.html
        ├── error.html
        ├── page.html
        └── tree.html

``conf.json``
    Konfigurationsdatei, die z.B. auf das Basis-Template verweist:

    .. code-block:: json

        {"base_template": "default"}

``nbconvert_templates``
    Benutzerdefinierte Templates für :doc:`/workspace/jupyter/nbconvert`.
``static``
    Verzeichnis für statische Dateien.
``templates``
    Benutzerdefinierte Tornado-Templates.
