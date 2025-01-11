Installation
============

You can install Panel in the virtual environment of your Jupyter kernel with:

.. code-block:: console

    $ uv add panel

For some of the following examples additional packages are required such as
`Holoviews <https://holoviews.org/>`_ and `hvPlot
<https://hvplot.holoviz.org/>`_. They can be installed with:

.. code-block:: console

    $ uv add "holoviews[recommended hvplot

Examples
--------

#. Download

   .. code-block:: console

    $ uv run panel sampledata
    Creating /Users/veit/.bokeh/data directory
    Using data directory: /Users/veit/.bokeh/data
    Fetching 'CGM.csv'
    Downloading: CGM.csv (1589982 bytes)
     1589982   [100.00%%]
    …

#. View

   Then you can look at the examples, for example ``Introduction.ipynb`` with

   .. code-block:: console

    $ uv run panel serve panel-examples/getting_started/Introduction.ipynb
    2019-08-18 10:55:44,056 Starting Bokeh server version 1.3.4 (running on Tornado 6.0.3)
    2019-08-18 10:55:44,067 Bokeh app running at: http://localhost:5006/Introduction
    2019-08-18 10:55:44,067 Starting Bokeh server with process id: 86677
