FastAPI integration
===================

Panel usually runs on a :doc:`pyviz:bokeh/bokeh-server`, which in turn runs on
`Tornado <https://www.tornadoweb.org/en/stable/>`_. However, it is also often
useful to embed a Panel app into a large web application, such as a FastAPI web
server. Integration with FastAPI is easier compared to others such as
:doc:`Flask <pyviz:bokeh/embedding-export/flask>`, as it is a more lightweight
framework. Using Panel with FastAPI requires only a little more effort than
notebooks and Bokeh servers.

Configuration
-------------

Before we start adding a Bokeh application to our FastApi server, we need to set
up some of the basic configuration in :download:`fastAPI/main.py`:

#. First, we import all the necessary elements:

   .. literalinclude:: fastAPI/main.py
      :caption: fastAPI/main.py
      :name: fastAPI/main.py
      :linenos:
      :lines: 1-3, 5-7

#. Next, we define ``app`` as an instance of ``FastAPI`` and define the path to
   the template directory:

   .. literalinclude:: fastAPI/main.py
      :lineno-start: 10
      :lines: 10-11

#. Now we create our first routine via an asynchronous function and refer it to
   our BokehServer:

   .. literalinclude:: fastAPI/main.py
      :lineno-start: 14
      :lines: 14-19

#. As you can see from the code, a `Jinja2
   <https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates>`_
   template :download:`fastAPI/templates/base.html` is expected. This can have
   the following content, for example:

   .. literalinclude:: fastAPI/templates/base.html
      :caption: fastAPI/templates/base.html
      :name: fastAPI/templates/base.html
      :language: html
      :linenos:
      :lines: 1-

#. Let’s now return to our :download:`fastAPI/main.py` file to start our bokeh
   server with ``pn.serve()``:

   .. literalinclude:: fastAPI/main.py
      :lineno-start: 22
      :lines: 22-

   ``createApp``
       calls up our panel app in this example, but this is not covered until the
       next section.
   ``address``, ``port``
       Address and port at which the server listens for requests; in our case
       ``http://127.0.0.1:5000``.
   ``show=False``
       ensures that the Bokeh server is started but is not immediately displayed
       in the browser.
   ``allow_websocket_origin``
       lists the hosts that can connect to the websocket. In our example, this
       should be ``fastApi``, so we use ``127.0.0.1:8000``.

#. Now we define the ``sliders`` app based on a standard template for FastAPI
   apps, which shows how Panel and FastAPI can be integrated:

   :download:`fastAPI/sliders/sinewave.py`
       a parameterised object that represents your existing code:

       .. literalinclude:: fastAPI/sliders/sinewave.py
          :caption: fastAPI/sliders/sinewave.py
          :name: fastAPI/sliders/sinewave.py
          :linenos:
          :lines: 1-

   :download:`fastAPI/sliders/pn_app.py`
       creates an app function from the ``SineWave`` class:

       .. literalinclude:: fastAPI/sliders/pn_app.py
          :caption: fastAPI/sliders/pn_app.py
          :name: fastAPI/sliders/pn_app.py
          :linenos:
          :lines: 1-

#. Finally, we return to our :download:`fastAPI/main.py` and import the
   ``createApp`` function:

   .. literalinclude:: fastAPI/main.py
      :caption: fastAPI/main.py
      :name: fastAPI/main.py
      :lineno-start: 4
      :lines: 4

The file structure should now look like this:

.. code-block:: console

    fastAPI
    ├── main.py
    ├── sliders
    │   ├── pn_app.py
    │   └── sinewave.py
    └── templates
        └── base.html

You can now start the server with:

.. code-block:: console

    $ bin/uvicorn main:app --reload
    INFO:     Will watch for changes in these directories: ['/srv/jupyter/jupyter-tutorial/docs/web/dashboards/panel/fastAPI']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [218214] using StatReload
    Launching server at http://127.0.0.1:5000
    INFO:     Started server process [218216]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.

You should then see the following in your web browser under the URL
``http://127.0.0.1:8000``:

.. figure:: panel-fastapi.png
   :alt: Widgets and sine curve in bokeh plot
