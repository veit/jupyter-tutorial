==================
Embedding in Flask
==================

Examplarisch betten wir Bokeh-Plots in das `Flask
<http://flask.pocoo.org/>`_-Framework ein. 

#. Erstellen der virtuellen Umgebung:

   .. code-block:: sh

    $ mkdir embed
    $ cd !$
    $ pipenv install flask bokeh pandas

#. Einbinden von Bokeh-Plots in Flask:

   #. Dabei wird zunächst in der Datei ``flask_embed.py`` eine Methode für
      ein Bokeh-Dokument erstellt:

      .. code-block:: python

        from bokeh.layouts import column
        from bokeh.models import ColumnDataSource, Slider
        from bokeh.plotting import figure
        from bokeh.server.server import Server
        from bokeh.themes import Theme

        from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature

        def modify_doc(doc):
            df = sea_surface_temperature.copy()
            source = ColumnDataSource(data=df)

            plot = figure(x_axis_type='datetime', y_range=(0, 25), y_axis_label='Temperature (Celsius)',
                          title="Sea Surface Temperature at 43.18, -70.43")
            plot.line('time', 'temperature', source=source)

            def callback(attr, old, new):
                if new == 0:
                    data = df
                else:
                    data = df.rolling('{0}D'.format(new)).mean()
                source.data = ColumnDataSource(data=data).data

            slider = Slider(start=0, end=30, value=0, step=1, title="Smoothing by N Days")
            slider.on_change('value', callback)

            doc.add_root(column(slider, plot))

            doc.theme = Theme(filename="theme.yaml")

   #. Mit ``bokeh.sampledata.sea_surface_temperature`` werden Beispieldaten
       verwendet, die aufgrund ihrer Größe nicht im Bokeh-Paket enthalten sind. Nach
       der Installation von Bokeh können diese jedoch mit folgendem Befehl
       heruntergeladen werden:

       .. code-block:: sh

        $ pipenv run bokeh sampledata

   #. Anschließend erstellen wir folgende ``theme.yaml``-Datei für die
      Gestaltung von ``Figure`` und ``Grid``:

      .. code-block:: yaml

        attrs:
            Figure:
                background_fill_color: "gainsboro"
                outline_line_color: white
                toolbar_location: above
                height: 500
                width: 800
            Grid:
                grid_line_dash: [6, 4]
                grid_line_color: white

   #. Nun fügen wir in ``flask_embed.py`` eine Route von der Bokeh-App zum
      Flask-Server-Konfigurationsobjekt hinzu:

      .. code-block:: python

        from flask import render_template
          
        from bokeh.embed import server_document
        …
        @app.route('/', methods=['GET'])
        def bkapp_page():
            script = server_document('http://localhost:5006/bkapp')
            return render_template("embed.html", script=script, framework="Flask")

   #. ``script`` und ``framework`` werden anschließend in ein
      `Jinja2 <http://jinja.pocoo.org/>`_-Template ``templates/embed.html``
      eingebunden, das den Plot angezeigen soll:

      .. code-block:: html

        <!doctype html>
          
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <title>Embedding a Bokeh Server in {{framework}}</title>
        </head>

        <body>
          <div>
            This Bokeh app below served by a Bokeh server that has been embedded
            in the web app framework {{framework}}. For more information see the section
            <a  target="_blank" href="https://bokeh.pydata.org/en/latest/docs/user_guide/server.html#embedding-bokeh-server-as-a-library">Embedding Bokeh Server as a Library</a>
            in the User’s Guide.
          </div>
          {{script|safe}}
        </body>
        </html>

   #. Nun wird ein Bokeh-Worker in ``flask_embed.py`` definiert:

      .. code-block:: python

        from flask import Flask
        from tornado.ioloop import IOLoop
        …
        def bk_worker():
            server = Server({'/bkapp': modify_doc}, io_loop=IOLoop(), allow_websocket_origin=["localhost:8000"])
            server.start()
            server.io_loop.start()

        from threading import Thread
        Thread(target=bk_worker).start()

      .. note::
        In dieser Konfiguration kann nur ein Prozess gestartet werden.

        Sollen mehrere Prozesse gestartet werden, dann schaut Euch bitte
        `flask_gunicorn_embed.py
        <https://gitlab.cc-asp.fraunhofer.de/vschiele/jupyterhub-userdoc/blob/master/examples/bokeh/embed/flask_gunicorn_embed.py>`_
        an.

   #. Schließlich wird noch die Flask-App definiert:

      .. code-block:: python 

        app = Flask(__name__)
        …
        if __name__ == '__main__':
            print('Opening single process Flask app with embedded Bokeh application on http://localhost:8000/')
            print()
            print('Multiple connections may block the Bokeh app in this configuration!')
            print('See "flask_gunicorn_embed.py" for one way to run multi-process')
            app.run(port=8000)

#. Falls der Bokeh-Service noch nicht über WebSocket mit Flask
   kommunizieren kann, sollte dies explizit erlaubt werden mit:

   .. code-block:: sh

    $ export BOKEH_ALLOW_WS_ORIGIN=127.0.0.1:5000

#. Schließlich kann Flask gestartet werden mit:

   .. code-block:: sh

    $ export FLASK_APP=flask_embed.py
    $ pipenv run flask run

   oder, falls mehrere Bokeh-Worker gestartet werden sollen:

   .. code-block:: sh

    $ export FLASK_APP=flask_gunicorn_embed.py
    $ pipenv run flask run

.. seealso::

   * `User Guide/Embedding Plots and Apps/App Sessions
     <https://bokeh.pydata.org/en/latest/docs/user_guide/embed.html#app-sessions>`_ 
   * `Source Code
     <https://gitlab.cc-asp.fraunhofer.de/vschiele/jupyterhub-userdoc/blob/master/examples/bokeh/embed/>`_

