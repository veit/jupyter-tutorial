Running Panel in the browser with WASM
======================================

Panel lets you write dashboards and other applications in Python that are
accessed through a web browser. Normally, the Python interpreter runs as a
separate Jupyter or Bokeh server process and communicates with the JavaScript
code running in the client browser. However, Python can also be run directly in
the browser using :abbr:`WASM (WebAssembly)`, without the need for a separate
server.

Panel uses `Pyodide <https://pyodide.org/en/stable/>`_ for this and `PyScript
<https://pyscript.net>`_ for rendering.

Converting panel applications
-----------------------------

Future versions of Panel can convert your Panel application from one or more
Python scripts or Notebook files, including :doc:`templates`, into an HTML file
using ``panel convert``. The only requirements are:

* they only import global modules and packages and no relative imports from
  other scripts or modules
* the libraries have been `compiled for Pyodide
  <https://github.com/pyodide/pyodide/tree/main/packages>`_ or are available as
  `Python wheels <Wheel>` on the :term:`Python Package Index` (:term:`PyPI`).

Example
-------

In the following example we will convert the :doc:`overview` notebook into a
standalone HTML page with

.. code-block:: console

    $ panel convert overview.ipynb --out pyodide
    Column
        [0] Column
            [0] FloatSlider(end=3.0, name='frequency', start=-1.0, value=1.0)
            [1] FloatSlider(end=3.0, name='amplitude', start=-1.0, value=1.0)
            [2] IntSlider(end=100, name='n', start=5, value=200)
        [1] Row
            [0] Matplotlib(Figure, name='interactive00114')
    Launching server at http://localhost:40405

Now you can open ``http://localhost:40405`` in your browser and try out the app:


.. figure:: pyodide-example.png
   :alt: Pyodide example

You can now add the :download:`pyodide/overview.html` file to your Github pages
or similar – no separate server is required.

.. seealso::
   * `Awesome Panel/Webassembly Apps
     <https://awesome-panel.github.io/examples/>`_

Options
-------

In the following I explain some of the options of ``panel convert``.

``--to``
    The format to convert to. There are three options, each with different
    advantages and disadvantages:

    ``pyodide`` (default)
         The application is run with pyodide in the main thread. This option is
         less performant than ``pyodide-worker``, but produces a fully
         self-contained HTML file that does not need to be hosted on a static
         file server, such as Github Pages.
    ``pyodide-worker``
        generates HTML and JS files, but includes a web worker that runs in a
        separate thread. This is the most powerful option, but the files must be
        hosted on a static file server.
    ``pyscript``
        creates an HTML file that uses `PyScript <https://pyscript.net>`_. This
        creates standalone HTML files with ``<py-env>`` and ``<py-script>`` tags
        containing the dependencies and application code. This output is the
        most readable and should have the same performance as the ``pyodide``
        option.
``-out``
    The directory to write the files to.
``--pwa``
    adds files that make the application a Progressive Web App.

    `Progressive Web Apps (PWAs)
    <https://en.wikipedia.org/wiki/Progressive_web_app>`_ provide a way for your
    web apps to behave almost like a native app, both on mobile devices and on
    the desktop. ``panel convert`` has a ``--pwa`` option that generates the
    files necessary to turn your panel and pyodide app into a PWA.

``--skip-embed``
    skips embedding pre-rendered content in the converted file.

    Panel embeds pre-rendered content in the HTML page and replaces it with live
    components once the page is loaded. However, this can take a long time. If
    you want to disable this behaviour and render a blank page first, use the
    ``--skip-embed`` option.

``--index``
    creates an index when you convert several applications at once, so you can
    easily navigate between them.
``--requirements``
    Explicit requirements to add to the converted file or to a
    ``requirements.txt`` file.

    By default, requirements are derived from code.

    If a library uses an optional import that cannot be derived from your
    application’s list of imports, you must specify an explicit list of
    dependencies.

    .. note::
       panel and its dependencies, including NumPy and Bokeh, are loaded
       automatically, which means that the explicit requirements for the above
       application would be as follows:

       .. code-block:: console

          $ panel convert overview.ipynb --out pyodide --requirements pandas matplotlib

       AAlternatively, you can provide a ``requirements.txt`` file:

       .. code-block:: console

          $ panel convert overview.ipynb --out pyodide --requirements requirements.txt

``--watch``
    Observe the source files.

You can get a complete overview with ``panel convert -u``.

.. tip::

    If the converted application does not work as expected, you can usually find
    the errors in the browser console, see `Finding Your Browser's Developer
    Console <https://balsamiq.com/support/faqs/browserconsole/>`_.

.. seealso::
    Answers to the most frequently asked questions about Python in the browser
    can be found in the

    * `Pyodide FAQ <https://pyodide.org/en/stable/usage/faq.html>`_
    * `PyScript FAQ <https://docs.pyscript.net/latest/reference/faq.html>`_
