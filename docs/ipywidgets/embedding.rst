Embed Jupyter widgets
=====================

Jupyter widgets can be serialised and then embedded in other contexts:

* static web pages
* Sphinx documentation
* HTML converted notebooks on Nbviewer


The npm package ``@jupyter-widgets/html-manager`` allows embedding in two
different ways:


* embedding the standard elements that can be used on any website
* embedding with `RequireJS <https://requirejs.org/>`_ also for custom widgets.

Embed widgets in HTML pages
---------------------------

The widgets menu provides several options for this:

*Save Notebook Widget State*
    A notebook file is saved with the current widget status as metadata. This
    allows to be rendered with the widgets in the browser.
*Clear Notebook Widget State*
    The widget status metadata is deleted from the notebook file.
*Embed widgets*
    The menu item offers a dialog box with an HTML page on which the current
    widgets are embedded. The RequireJS embedder is used to support custom
    widgets.

    .. note::
        The first script tag loads RequireJS from a CDN. However, RequireJS
        should be made available on the site itself and this script tag should
        be deleted.

    .. note::
        The second script tag loads the RequireJS widget embedder. This defines
        suitable modules and then sets up a function for rendering all widget
        views contained on the page.

        If you only embed standard widgets and don’t use RequireJS, you can
        replace the first two script tags with a script tag that loads the
        standard script.

*Download Widget State*
    The option downloads a JSON file that contains the serialized status of all
    widget models currently in use in the
    ``application/vnd.jupyter.widget-state+json`` format specified in the
    ``@jupyter-widgets/schema``  npm package.

Sphinx integration
------------------

Jupyter Sphinx
~~~~~~~~~~~~~~

`jupyter_sphinx <https://github.com/jupyter/jupyter-sphinx>`_ enables
jupyter-specific functions in Sphinx. It can be installed with  ``pip``.

Configuration
:::::::::::::

Adds ``jupyter_sphinx.embed_widgets`` to the list of extensions in the
:file:`conf.py` file.

Then you can use the following directives in reStructuredText:

``ipywidgets-setup``
    .. code-block:: python

       from ipywidgets import Button, IntSlider, VBox, jsdlink

``ipywidgets-display``
    .. code-block:: python

       s1, s2 = IntSlider(max=200, value=100), IntSlider(value=40)
       b = Button(icon="legal")
       jsdlink((s1, "value"), (s2, "max"))
       VBox([s1, s2, b])


Example
:::::::

.. code-block:: rest

   .. ipywidgets-setup::

      from ipywidgets import VBox, jsdlink, IntSlider, Button

   .. ipywidgets-display::
      :hide-code:

      s1, s2 = IntSlider(max=200, value=100), IntSlider(value=40)
      b = Button(icon="legal")
      jsdlink((s1, "value"), (s2, "max"))
      VBox([s1, s2, b])

Options
:::::::

The ``ipywidgets-setup`` and ``ipywidgets-display`` directives have the
following options:

``ipywidgets-setup``
    with the option ``:show:`` to display the setup code as a code block
``ipywidgets-display``
    with the following options:
``:hide-code:``
    doesn’t show the code, only the widget

Widget

``:code-below:``
    shows the code after the widget
``:alt:``
    Alternate text if the widget cannot be rendered

.. seealso::
   `Options <https://jupyter-sphinx.readthedocs.io/en/latest/#configuration-options>`_
