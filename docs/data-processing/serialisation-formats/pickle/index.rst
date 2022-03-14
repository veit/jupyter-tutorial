Pickle
======

Overview
--------

+-----------------------+-------+-------------------------------------------------------+
| Data structure        | +\-   | Pickle is used to store Python object structures like |
| support               |       | ``list`` or ``dict`` in a byte stream. In contrast to |
|                       |       | ``marshal``, already serialised objects are tracked   |
|                       |       | so that later references are not serialised again.    |
|                       |       | Recursive objects are also possible.                  |
+-----------------------+-------+-------------------------------------------------------+
| Standardisation       | ++    | Pickle is defined in the Python Enhancement Proposals |
|                       |       | Proposals `307`_, `3154`_ and `574`_.                 |
+-----------------------+-------+-------------------------------------------------------+
| Schema IDL            | -\-   | No                                                    |
+-----------------------+-------+-------------------------------------------------------+
| Language support      | -\-   | Python-specific                                       |
+-----------------------+-------+-------------------------------------------------------+
| Human readability     | +\-   | Pickle is a binary serialisation format, but it can   |
|                       |       | be easily read with Python.                           |
+-----------------------+-------+-------------------------------------------------------+
| Speed                 | +\-   | The pickle format can usually be serialised and       |
|                       |       | deserialised quickly by Python; see also              |
|                       |       | `Don’t pickle your data`_.                            |
+-----------------------+-------+-------------------------------------------------------+
| File size             | ++    | Compact binary format, which can, however, be         |
|                       |       | compressed even further, see also `Data Compression   |
|                       |       | and Archiving                                         |
|                       |       | <https://docs.python.org/3/library/archiving.html>`_. |
+-----------------------+-------+-------------------------------------------------------+

.. seealso::

    `pickle – Python object serialization <https://docs.python.org/3/library/pickle.html>`_
        Documentation of the ``pickle`` module
    `shelve – Python object persistence <https://docs.python.org/3/library/shelve.html#module-shelve>`_
        Indexed databases of ``pickle`` objects
    `Uwe Korn: The implications of pickling ML models <https://uwekorn.com/2021/04/26/implications-of-pickling-ml-models.html>`_
        Alternatives to ``pickle`` for ML models
    `Ned Batchelder: Pickle’s nine flaws <https://nedbatchelder.com/blog/202006/pickles_nine_flaws.html>`_
        Disadvantages of ``pickle`` and alternatives

.. _`307`: https://www.python.org/dev/peps/pep-0307
.. _`3154`: https://www.python.org/dev/peps/pep-3154
.. _`574`: https://www.python.org/dev/peps/pep-0574
.. _`Don’t pickle your data`:
   https://www.benfrederickson.com/dont-pickle-your-data/

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    pickle-examples
