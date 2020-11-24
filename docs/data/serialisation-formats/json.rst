JSON
====

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure support| +-    | JSON supports array and map or object structures and  |
|                       |       | many different data types including strings, numbers, |
|                       |       | boolean, null etc., but no date formats.              |
|                       |       |                                                       |
|                       |       | However, JSON does not support all data types of      |
|                       |       | JavaScript: ``NaN`` and ``Infinity`` become ``null``. |
|                       |       |                                                       |
|                       |       | Please note that the JSON syntax also don’t support   |
|                       |       | comments and you have to work arround e.g. with a     |
|                       |       | ``__comment__`` key/value pair.                       |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | \+    | JSON has a formal strongly typed `standard`_ (see     |
|                       |       | also `RFC 8259`_).                                    |
|                       |       | However, JSON data also contains some pitfalls due to |
|                       |       | the ambiguity of the JSON specifications:             |
|                       |       |                                                       |
|                       |       | *A JSON parser MUST accept all texts that conform to  |
|                       |       | the JSON grammar* (`RFC 7159`_)                       |
|                       |       |                                                       |
|                       |       | and                                                   |
|                       |       |                                                       |
|                       |       | *An implementation may set limits on the size of texts|
|                       |       | that it accepts. An implementation may set limits on  |
|                       |       | the maximum depth of nesting. An implementation may   |
|                       |       | set limits on the range and precision of numbers. An  |
|                       |       | implementation may set limits on the length and       |
|                       |       | character contents of strings* (`RFC 7158 #9`_).      |
|                       |       |                                                       |
|                       |       | Unfortunately there is neither a reference            |
|                       |       | implementation nor an official test suite that would  |
|                       |       | show the expected behaviour – at least `JSON_Checker`_|
|                       |       | gives some hints.                                     |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | +-    | Partly with `JSON Schema Proposal`_, `JSON Encoding   |
|                       |       | Rules (JER)`_, `Kwalify`_, `Rx`_, `JSON-LD`_ or       |
|                       |       | `JMESPath`_.                                          |
|                       |       |                                                       |
|                       |       | After all, there are many different `validators`_ are |
|                       |       | available.                                            |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | ++    | The JSON format is very well supported by almost every|
|                       |       | programming language.                                 |
|                       |       |                                                       |
|                       |       | The data structure of JSON closely represent objects  |
|                       |       | in many languages e.g. a Python ``dict`` can be       |
|                       |       | represented as JSON ``object``, and a Python ``list`` |
|                       |       | by a JSON ``array``.                                  |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | +-    | JSON is a human-readable serialisation format but it  |
|                       |       | does not support comments.                            |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | ++    | JSON is one of the fastest human-readable formats to  |
|                       |       | serialise and deserialise.                            |
+-----------------------+-------+-------------------------------------------------------+
| File size             | +-    | JSON is in the medium range similar to :doc:`yaml`    |
|                       |       | and :doc:`toml`.                                      |
+-----------------------+-------+-------------------------------------------------------+

Example
-------

Response of the :ref:`OSM-Nomination-API <Example-OSM-Nomination-API>`

.. code-block:: javascript

    [
        {
            'place_id': 234847916,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'relation',
            'osm_id': 131761,
            'boundingbox': ['52.5200695', '52.5232601', '13.4103097', '13.4160798'],
            'lat': '52.521670650000004',
            'lon': '13.413278026558228',
            'display_name': 'Alexanderplatz, Mitte, Berlin, 10178, Deutschland',
            'class': 'highway',
            'type': 'pedestrian',
            'importance': 0.6914982526373583
        },
        {
            'place_id': 53256307,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'node',
            'osm_id': 4389211800,
            'boundingbox': ['52.5231653', '52.5232653', '13.414475', '13.414575'],
            'lat': '52.5232153',
            'lon': '13.414525',
            'display_name': 'Alexanderplatz, Alexanderstraße, Mitte, Berlin, 10178, Deutschland',
            'class': 'highway',
            'type': 'bus_stop',
            'importance': 0.22100000000000003,
            'icon': 'https://nominatim.openstreetmap.org/images/mapicons/transport_bus_stop2.p.20.png'
        },
        {
            'place_id': 90037579,
            'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
            'osm_type': 'way',
            'osm_id': 23853138,
            'boundingbox': ['52.5214702', '52.5217276', '13.4037885', '13.4045026'],
            'lat': '52.5215991',
            'lon': '13.404112295159964',
            'display_name': 'Alexander Plaza, 1, Rosenstraße, Mitte, Berlin, 10178, Deutschland',
            'class': 'tourism',
            'type': 'hotel',
            'importance': 0.11100000000000002,
            'icon': 'https://nominatim.openstreetmap.org/images/mapicons/accommodation_hotel2.p.20.png'
        }
    ]

.. _`standard`: https://www.json.org/json-en.html
.. _`RFC 8259`: https://tools.ietf.org/html/rfc8259
.. _`RFC 7159`: https://tools.ietf.org/html/rfc7159
.. _`RFC 7158 #9`: https://www.ietf.org/rfc/rfc7158.html#section-9
.. _`JSON_Checker`: http://www.json.org/JSON_checker/
.. _`JSON Schema Proposal`: http://json-schema.org/
.. _`JSON Encoding Rules (JER)`: https://www.itu.int/rec/T-REC-X.697-201710-I/
.. _`Kwalify`: http://www.kuwata-lab.com/kwalify/
.. _`Rx`: http://rx.codesimply.com/
.. _`JSON-LD`: https://json-ld.org#
.. _`JMESPath`: https://jmespath.org/
.. _`validators`: https://json-schema.org/implementations.html#validators
