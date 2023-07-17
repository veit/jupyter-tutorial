Templating
==========

.. _voila-gridstack:

Voilà gridstack
---------------

`gridstack.js <https://gridstackjs.com/>`_ is a jQuery plugin for widget layouts.
This enables multi-column drag and drop grids and customizable layouts suitable
for `Bootstrap v3 <https://getbootstrap.com/docs/3.4/>`_. It also works with
`knockout.js <https://knockoutjs.com/>`_ and touch devices.

The Gridstack Voilà template uses the metadata of the notebook cells to design
the notebook’s layout. It is supposed to support the entire specification for
the outdated :doc:`../jupyter-dashboards/index`.

.. image:: voila-gridstack.png
   :scale: 53%
   :alt: Example for Voilà gridstack

voila-vuetify
-------------

`voila-vuetify <https://github.com/voila-dashboards/voila-vuetify>`_ is a
template for using Voilà with the `Material Design Component Framework
<https://m3.material.io>`_ `Vuetify.js <https://vuetifyjs.com/>`_.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install bqplot ipyvuetify voila-vuetify

Usage
~~~~~

To use ``voila-vuetify`` in a notebook, you first have to import ``ipyvuetify``:

.. code-block:: python

    import ipyvuetify as v

Then you can create a layout, for example with:

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

You can use :doc:`bqplot_vuetify_example` with:

.. code-block:: console

    $ pipenv run voila --template vuetify-default bqplot_vuetify_example.ipynb

Then your standard browser will open the URL ``http://localhost:8866/`` and show
you the plots in Responsive Material Design.

Example for Voilà-vuetify with the monitor resolution of a laptop MDPI screen:

.. image:: voila-vuetify-laptop.png
   :scale: 53%

Example for Voilà-vuetify with the monitor resolution of an iPhone X:

.. image:: voila-vuetify-iphone.png
   :scale: 53%

voila-debug
-----------

`voila-debug <https://github.com/voila-dashboards/voila-debug>`_ is a template
for displaying debug information when working on Voilà applications.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install voila-debug

Usage
~~~~~

You can use the template :doc:`debug` with:

.. code-block:: console

    $ pipenv run voila --template=debug --VoilaExporter.template_file=debug.tpl

This will open your default browser with the URL ``localhost:8866``.

Then you can take a closer look at how it works at
``http://localhost:8866/voila/render/docs/jupyter/dashboards/voila/debug.ipynb``.

.. image:: voila-debug.png
   :scale: 53%
   :alt: Example of voila-debug

In addition to an example widget, it contains a code cell for exiting the
kernel:

.. code-block:: python

    import os

    def kill_kernel(change):
        os._exit(0)

    button = widgets.Button(description="Kill Kernel")
    button.on_click(kill_kernel)
    button

voila-reveal
------------

`voila-reveal <https://github.com/voila-dashboards/voila-reveal>`_ is a template
for slideshows based on `RevealJS <https://revealjs.com/>`_.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pipenv install voila-reveal

Usage
~~~~~

You can use the template with:

.. code-block:: console

    $ pipenv run voila --template=reveal reveal.ipynb

Additional options can be used to override the default settings, for example to
change the default value for transition ``Fade`` to ``Zoom`` with:

.. code-block:: console

    $ pipenv run voila --template=reveal --VoilaConfiguration.resources="{'reveal': {'transition': 'zoom'}}" reveal.ipynb

If configuration options are to be saved permanently, a  ``conf.json`` file can
be created in ``share/jupyter/voila/templates/reveal/``:

.. code-block:: javascript

    {
      "traitlet_configuration": {
        "resources": {
          "reveal": {
            "scroll": false,
            "theme": "simple",
            "transition": "zoom"
          }
        }
      }
    }

You can then turn your notebook into a slideshow in :menuselection:`View -->
Cell Toolbar --> Slideshow`. In a cell toolbar you can choose between

Slide
    left to right
Sub-Slide
    top to bottom
Fragment
    stops inside a slide
Notes
    Speaker notes opened in a new window when the presenter press the ``t`` key

If you want to publish your slideshow on `binder <https://mybinder.org/>`_, you
must write the following tag in the metadata of the notebook in
:menuselection:`Edit --> Edit Notebook Metadata`:

.. code-block:: javascript

    "rise": {
        "autolaunch": true
    }

You can also use the `chalkboard reveal plugin
<https://github.com/rajgoel/reveal.js-plugins/tree/master/chalkboard>`_ in the
metadata of the notebook:

.. code-block:: javascript

    "rise": {
      "enable_chalkboard": true
    }

Create your own templates
-------------------------

A Voilà template is a folder that is located in the virtual environment at
``share/jupyter/voila/templates`` and for example, contains the following:

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
    Configuration file that for example refers to the basic template:

    .. code-block:: json

        {"base_template": "default"}

``nbconvert_templates``
    Custom templates for :doc:`/nbconvert`.
``static``
    Directory for static files.
``templates``
    Custom tornado templates.
