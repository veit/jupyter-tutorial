Serialisation formats
=====================

Data serialisation converts structured data to a format that allows sharing and
or storing of the data. Before serialising data you have to decide how the data
should be structured – flat or nested. The differences in the two styles are
shown in the examples below:

Flat JSON style:
    .. code-block:: javascript

        {
          "id"          :  "veit",
          "first_name"  :  "Veit",
          "last_name"   :  "Schiele",
        }

Nested JSON style:
    .. code-block:: javascript

      {
        "veit" : {
          "first_name"  :  "Veit",
          "last_name"   :  "Schiele",
        },
      }


Serialising data
----------------

If the data is to be serialised flat, Python offers two functions:

``repr``
~~~~~~~~

:func:`python:repr` outputs a printable representation of the input, for
example:

.. code-block:: python

   >>> a = { "id" : "veit", "first_name": "Veit", "last_name": "Schiele" }
   >>> print(repr(a))
   {'id': 'veit', 'first_name': 'Veit', 'last_name': 'Schiele'}
   >>> with open('data.py', 'w') as f:
   ...     f.write(repr(a))
   ...
   60

``ast.literal_eval``
~~~~~~~~~~~~~~~~~~~~


the :func:`python:ast.literal_eval` function parses and analyses the Python data
type of an expression. Supported data types are
:doc:`python-basics:types/strings`, :doc:`python-basics:types/numbers`,
:doc:`python-basics:types/tuples`, :doc:`python-basics:types/lists`,
:doc:`python-basics:types/dicts` and :doc:`python-basics:types/none`.

.. code-block:: python

   >>> import ast
   >>> with open('data.py', 'r') as f:
   ...     inp = ast.literal_eval(f.read())

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    csv/index
    json/index
    excel.ipynb
    pickle/index
    protobuf
    toml
    xml-html/index
    yaml
    others
