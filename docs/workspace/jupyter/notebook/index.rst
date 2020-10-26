Notebook
========

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    ../../../first-steps/install
    ../../../first-steps/create-notebook
    shortcuts
    config

Introduction
------------

Jupyter Notebooks extend the console-based approach to interactive computing
with a web-based application, with which the entire process can be recorded:
from developing and executing the code to documenting and presenting the
results. Jupyter notebooks combine three different components:

Interactive Computing Protocol:
    Open network protocol based on JSON data via `ZMQ
    <http://zeromq.org/>`_ and `WebSockets
    <https://en.wikipedia.org/wiki/WebSocket>`_.
Notebook Document Format:
    Open JSON-based document format with full records of the user’s sessions and
    the code contained therein.
Kernel:
    Processes that execute interactive code in a particular programming language
    and return output to the user.
