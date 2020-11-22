Serialisation formats
=====================

Data serialisation converts structured data to a format that allows sharing and
or storing of the data. Bevore serialising data you have to decide how the data
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

If the data to be serialised is in flat style, Python offers two methods to
serialise the data.

``repr``
~~~~~~~~

.. code-block:: python

    a =  { "id" : "veit", "first_name": "Veit", "last_name": "Schiele" }

    # Return a printable representation of the input
    print(repr(a))

    # Write contet to the file
    with open('data.py', 'w') as f:f.write(repr(a))

``ast.literal_eval``
~~~~~~~~~~~~~~~~~~~~

The ``literal_eval`` method parses and evaluates an expression for a Python
datatype. Supported data types are: strings, numbers, tuples, lists, dicts,
booleans, and None.

.. code-block:: python

    with open('data.py', 'r') as f: inp = ast.literal_eval(f.read())

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    csv
    json
    protobuf
    toml
    xml
    yaml
    others
