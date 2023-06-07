Jupyter Dashboards
==================

The `Jupyter Dashboards Layout Extension
<https://jupyter-dashboards-layout.readthedocs.io/>`_ is an add-on for Jupyter
notebooks, with which outputs (text, plots, widgets, etc.) can be arranged in a
design grid or in report form. It saves the information on the layout directly
in the notebook so that other users of this extension can also see the notebook
in the same layout. For examples of dashboards, see `Jupyter Dashboards Demos
<https://github.com/jupyter/dashboards/tree/master/etc/notebooks>`_.

Use case
--------

The Jupyter dashboards should solve the following problem:

#. Alice creates a Jupyter notebook with plots and interactive widgets.
#. Alice arranges the notebook cells in a grid or report format.
#. Alice provides the dashboard on a dashboard server.
#. Bob calls up the dashboard on the `Jupyter Dashboards Server
   <https://github.com/jupyter-attic/dashboards_server>`_ and interacts with
   Alice Dashboard application.
#. Alice updates her Jupyter notebook and then makes the dashboard available
   again on the dashboard server.

.. note::
    For steps 3–5, `Jupyter Dashboards Bundler
    <https://github.com/jupyter-attic/dashboards_bundlers>`_ and `Jupyter
    Dashboards Server <https://github.com/jupyter-attic/dashboards_server>`_
    are also required; however, both are now retired and should not be used any
    longer.

    The roadmap for the :ref:`Voila-Gridstack-Template <voila-gridstack>` is to
    support the entire specification for the Jupyter dashboards. Currently,
    however, the Voilà gridstack template is still in an early stage of
    development, see also `And voilà!
    <https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93>`_.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    use
    matplotlib-example.ipynb
