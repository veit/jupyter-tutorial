Introduction
============

.. include:: ../README.rst
   :start-after: badges
   :end-before: first-steps

Target group
------------

The users of Jupyter notebooks are diverse, from data scientists to data
engineers and analysts to system engineers. Their skills and workflows are very
different. However, one of the great strengths of Jupyter notebooks is that they
allow these different experts to work closely together in cross-functional
teams.

* **Data scientists** explore data with different parameters and summarise the
  results.
* **Data engineers** check the quality of the code and make it more robust,
  efficient and scalable.
* **Data analysts** use the code provided by data engineers to systematically
  analyse the data.
* **System engineers** provide the research platform based on the
  :doc:`workspace/jupyter/hub/index` on which the other roles can perform their
  work.

In this tutorial, we primarily address system engineers who want to build and
operate a platform based on Jupyter notebooks. Then, we explain how this
platform can be used effectively by data scientists, data engineers, and
analysts.

Structure of the Jupyter tutorial
---------------------------------

From Chapter 3, the Jupyter tutorial follows the prototype of a research
project:

3. **Set up the workspace** with the installation and configuration of
   :doc:`workspace/ipython/index`,
   :doc:`workspace/jupyter/index` with
   :doc:`workspace/jupyter/nbextensions/index` and
   :doc:`workspace/jupyter/ipywidgets/index`.
4. **Collect data,** either through a :doc:`REST API
   <data-processing/requests/index>` or directly from an :doc:`HTML page
   <data-processing/serialisation-formats/xml-html/beautifulsoup>`.
5. **Cleaning up data** is a recurring task that includes Remove or modify
   redundant, inconsistent, or incorrectly formatted data.
6. **Analyse data** through exploratory analysis and :doc:`visualising data
   <viz/index>`.
7. **Refactoring** includes parameterisation, validation and performance
   optimisation, including through :doc:`concurrency
   <performance/concurrency>`.
8. **Creating a product**
   includes :doc:`productive/testing`, :doc:`productive/logging/index` and
   :doc:`productive/documenting/index` the methods and functions as well
   as :doc:`creating packages  <productive/packaging/index>`.
9. **Web applications**
   can either generate dashboards from Jupyter notebooks or require more
   comprehensive application logic, such as demonstrated in
   :doc:`pyviz:bokeh/embedding-export/flask`, or provide data via a `RESTful API
   <https://en.wikipedia.org/wiki/Representational_state_transfer>`_.

Why Jupyter?
------------

How can these diverse tasks be simplified? You will hardly find a tool that
covers all of these tasks, and several tools are often required even for
individual tasks. Therefore, on a more abstract level, we are looking for more
general patterns for tools and languages with which data can be analysed and
visualised and a project can be documented and presented. This is exactly what
we are aiming for with `Project Jupyter <https://jupyter.org/>`_.

The Jupyter project started in 2014 with the aim of creating a consistent set of
open source tools for scientific research, reproducible workflows,
`computational narratives
<https://blog.jupyter.org/project-jupyter-computational-narratives-as-the-engine-of-collaborative-data-science-2b5fb94c3c58>`_
and data analysis. In 2017, Jupyter received the `ACM Software Systems Award
<https://blog.jupyter.org/jupyter-receives-the-acm-software-system-award-d433b0dfe3a2>`_
– a prestigious award which, among other things, shares with Unix and the web.

To understand why Jupyter notebooks are so successful, let’s take a closer look
at the core functions:

`Jupyter Notebook Format <https://nbformat.readthedocs.io/>`_
    Jupyter Notebooks are an open, JSON-based document format with full records
    of the user’s sessions and the code they contain.
Interactive Computing Protocol
    The notebook communicates with the computing kernel via the *Interactive
    Computing Protocol*, an open network protocol based on JSON data via `ZMQ
    <https://zeromq.org/>`_ and `WebSockets
    <https://en.wikipedia.org/wiki/WebSocket>`_.
:doc:`workspace/jupyter/kernels/index`
    Kernels are processes that execute interactive code in a specific
    programming language and return the output to the user.

.. seealso::
   * `Jupyter celebrates 20 years
     <https://data.berkeley.edu/news/project-jupyter-celebrates-20-years-fernando-perez-reflects-how-it-started-open-sciences>`_

Jupyter infrastructure
----------------------

A platform for the above-mentioned use cases requires an extensive
infrastructure that not only allows the provision of the kernel and the
parameterisation, time control and parallelisation of notebooks, but also the
uniform provision of resources.

This tutorial provides a platform that enables fast, flexible and comprehensive
data analysis beyond Jupyter notebooks. At the moment, however, we are not yet
going into how it can be expanded to include streaming pipelines and
domain-driven data stores.

However, you can also create and run the examples in the Jupyter tutorial
locally.
