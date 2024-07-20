================
Jupyter Tutorial
================

`Jupyter notebooks <https://jupyter-notebook.readthedocs.io/en/stable/>`_ are
growing in popularity with data scientists and have become the de facto standard
for rapid prototyping and exploratory analysis. They inspire experiments and
innovations enormously and as well they make the entire research process faster
and more reliable. In addition, many additional components are created that
expand the original limits of their use and enable new uses.

.. graphviz::

    digraph decide_jupyter {
        graph [fontname = "Calibri", fontsize="10", penwidth="1px",
               overlap=false];
        node [fontname = "Calibri", fontsize="10", style="bold",
              penwidth="1px", fontcolor="#640FFB"; color="#640FFB";];
        edge [fontname = "Calibri", fontsize="10", style="bold",
              penwidth="1px", fontcolor="#640FFB"; color="#640FFB";];
        tooltip="How do I decide which Jupyter packages I need?";
        // Top Level
        what [
            shape=diamond,
            label="What do you want to do?",
            tooltip="Jupyter offers you different ways how you can use the notebooks"]
        // Second Level
        singleuser [
             shape=plaintext,
             label=" ",
             tooltip="Single user"]
        team [
            shape=plaintext,
            label=" ",
            tooltip="Team"]
        nbconvert [
            label="nbconvert",
            tooltip="Install and\nuse nbconvert",
            target="_top",
            href="nbconvert.html"]
        nbviewer [
            label="nbviewer",
            tooltip="Install and\nuse nbviewer",
            target="_top",
            href="nbviewer.html"]
        kernels [
            label="Kernels",
            tooltip="Install, view and\nstart kernels",
            target="_top",
            href="kernels/install.html"]
        extensions [
            shape=plaintext,
            label=" ",
            tooltip="Install notebook extensions"]
        embed [
            shape=plaintext,
            label="",
            tooltip="Embed notebooks in other applications"]
        examples [
            label="Enterprise\napplications",
            tooltip="Application examples at\nNetflix, Bloomberg etc.",
            target="_top",
            href="use-cases.html"]
        // 3rd Level
        notebook [
             label="Jupyter-\nNotebook",
             tooltip="Install notebook locally",
             target="_top",
             href="notebook/index.html"]
         jupyterlab [
             label="JupyterLab",
             tooltip="Install JupyterLab locally",
             target="_top",
             href="jupyterlab/index.html"]
         hub [
             label="JupyterHub",
             tooltip="Install\nJupyterHub",
             target="_top",
             href="hub/index.html"]
         binder [
             label="Binder",
             tooltip="Binder tools",
             target="_top",
             href="binder.html"]
         nbviewer [
             label="nbviewer",
             tooltip="Install and use nbviewer",
             target="_top",
             href="nbviewer.html"]
        widgets [
            label="Widgets",
            tooltip="Install and\nuse ipywidgets",
            target="_top",
            href="ipywidgets/index.html"]
        extend [
            label="nbextensions",
            tooltip="Install and use various\nnotebook extensions",
            target="_top",
            href="nbextensions/index.html"]
        viz [
            label="Visualise\ndata",
            tooltip="Data visualisation libraries",
            target="_top",
            href="viz/index.html"]
        dash [
            label="Dashboards",
            tooltip="Install and\nuse Dashboards",
            target="_top",
            href="dashboards/index.html"]
        html [
            label="in HTML",
            tooltip="Embed notebooks in\nstatic HTML",
            target="_top",
            href="ipywidgets/embedding.html"]
        nbsphinx [
            label="nbsphinx",
            tooltip="Embed notebooks in the\nSphinx Document Generator",
            target="_top",
            href="sphinx/nbsphinx.html"]
        executablebooks [
            label="Executable Books",
            tooltip="Bücher aus Jupyter Notebooks und MyST",
            target="_top",
            href="sphinx/executablebooks.html"]
        // Edges
        what -> singleuser [label="Single\nuser"]
        what -> team [label="Teamwork"]
        what -> nbconvert [label="Convert"]
        nbconvert -> nbviewer [label="Conversion\nservice"]
        what -> kernels [label="Java, R,\nJulia etc."]
        what -> extensions [label="Extend\nnotebooks"]
        what -> embed [label="Embed\nnotebooks"]
        what -> examples [label="Examples"]
        singleuser -> {notebook jupyterlab}
        team -> {hub binder}
        extensions -> {widgets extend viz dash}
        embed -> {html nbsphinx executablebooks}
        // Arrangement
        rankdir="LR"
        {rank = same; what;}
        {rank = same; notebook; jupyterlab; hub; binder; widgets; extend; viz;
                dash; html}
        {rank = same; widgets; extend; viz; dash;}
    }

However, the Jupyter tutorial is only part of a series of tutorials on data
analysis and visualisation:

* :doc:`python-basics:index`
* :doc:`python4datascience:index`
* :doc:`PyViz Tutorial <pyviz:index>`
* `cusy Design-System: Datenvisualisierung
  <https://www.cusy.design/de/latest/viz/index.html>`_

All tutorials serve as seminar documents for our harmonised training courses:

+---------------+--------------------------------------------------------------+
| Duration      | Topic                                                        |
+===============+==============================================================+
| 3 days        | `Introduction to Python`_                                    |
+---------------+--------------------------------------------------------------+
| 2 days        | `Advanced Python`_                                           |
+---------------+--------------------------------------------------------------+
| 2 days        | `Design patterns in Python`_                                 |
+---------------+--------------------------------------------------------------+
| 2 days        | `Efficient testing with Python`_                             |
+---------------+--------------------------------------------------------------+
| 1 day         | `Software documentation with Sphinx`_                        |
+---------------+--------------------------------------------------------------+
| 2 days        | `Technical writing`_                                         |
+---------------+--------------------------------------------------------------+
| 3 days        | `Jupyter notebooks for efficient data science workflows`_    |
+---------------+--------------------------------------------------------------+
| 2 days        | `Numerical calculations with NumPy`_                         |
+---------------+--------------------------------------------------------------+
| 2 days        | `Analysing data with pandas`_                                |
+---------------+--------------------------------------------------------------+
| 3 days        | `Read, write and provide data with Python`_                  |
+---------------+--------------------------------------------------------------+
| 2 days        | `Cleanse and validate data with Python`_                     |
+---------------+--------------------------------------------------------------+
| 5 days        | `Visualising data with Python`_                              |
+---------------+--------------------------------------------------------------+
| 1 days        | `Designing data visualisations`_                             |
+---------------+--------------------------------------------------------------+
| 2 days        | `Create dashboards`_                                         |
+---------------+--------------------------------------------------------------+
| 3 days        | `Versioned and reproducible storage of code and data`_       |
+---------------+--------------------------------------------------------------+
| Subscription  | `News from Python for data science`_                         |
| of 2 hours    |                                                              |
| per quarter   |                                                              |
+---------------+--------------------------------------------------------------+

.. _`Introduction to Python`:
   https://cusy.io/en/our-training-courses/introduction-to-python
.. _`Advanced Python`:
   https://cusy.io/en/our-training-courses/advanced-python
.. _`Design patterns in Python`:
   https://cusy.io/en/our-training-courses/design-patterns-in-python
.. _`Efficient testing with Python`:
   https://cusy.io/en/our-training-courses/efficient-testing-with-python
.. _`Software documentation with Sphinx`:
   https://cusy.io/en/our-training-courses/software-documentation-with-sphinx
.. _`Technical writing`:
   https://cusy.io/en/our-training-courses/technical-writing
.. _`Jupyter notebooks for efficient data science workflows`:
   https://cusy.io/en/our-training-courses/jupyter-notebooks-for-efficient-data-science-workflows
.. _`Numerical calculations with NumPy`:
   https://cusy.io/en/our-training-courses/numerical-calculations-with-numpy
.. _`Analysing data with pandas`:
   https://cusy.io/en/our-training-courses/analysing-data-with-pandas
.. _`Read, write and provide data with Python`:
   https://cusy.io/en/our-training-courses/read-write-and-provide-data-with-python
.. _`Cleanse and validate data with Python`:
   https://cusy.io/en/our-training-courses/cleanse-and-validate-data-with-python
.. _`Visualising data with Python`:
   https://cusy.io/en/our-training-courses/visualising-data-with-python
.. _`Designing data visualisations`:
   https://cusy.io/en/our-training-courses/designing-data-visualisations
.. _`Create dashboards`:
   https://cusy.io/en/our-training-courses/create-dashboards
.. _`Versioned and reproducible storage of code and data`:
   https://cusy.io/en/our-training-courses/versioned-and-reproducible-storage-of-code-and-data
.. _`News from Python for data science`:
   https://cusy.io/en/our-training-courses/news-from-python-for-data-science

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    intro
    whatsnew
    notebook/index
    jupyterlab/index
    hub/index
    binder
    nbconvert
    nbviewer
    kernels/index
    ipywidgets/index
    nbextensions/index
    viz/index
    dashboards/index
    sphinx/index
    use-cases
    genindex

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
