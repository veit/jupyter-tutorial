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

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    serialisation.ipynb
    csv/index
    json/index
    excel.ipynb
    xml-html/index
    yaml/index
    toml
    pickle/index
    protobuf
    others
