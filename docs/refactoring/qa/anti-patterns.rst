Code-Smells and Anti-Patterns
=============================

Functions that should be objects
--------------------------------

In addition to object-oriented programming, Python also supports procedural
programming using functions and inheritable classes. Both paradigms should,
however, be applied to the appropriate problems.

Typical symptoms of functional code that should be converted to classes are

* similar arguments across functions
* high number of distinct Halstead operands
* mix of mutable and immutable functions

For example, three functions with ambiguous usage can be reorganised so, that
``load_image()`` is replaced by ``.__init__()``, ``crop()`` becomes a class
method, and ``get_thumbnail()`` a property:

.. code-block:: python
    class Image(object):
        thumbnail_resolution = 128
        def __init__(self, path):
            …
        def crop(self, width, height):
            …
        @property
        def thumbnail(self):
            …
            return thumb

Objects that should be functions
--------------------------------

Sometimes, however, object-oriented code should also be better broken down into
functions, e.g. if a class contains only one other method apart from
``.__init__()`` or only static methods.

.. note::
   You do not have to search for such classes manually, but there is a pylint
   rule for it:

   .. code-block:: console

    $ pipenv run pylint --disable=all --enable=R0903 requests
    ************* Module requests.auth
    requests/auth.py:72:0: R0903: Too few public methods (1/2) (too-few-public-methods)
    requests/auth.py:100:0: R0903: Too few public methods (1/2) (too-few-public-methods)
    ************* Module requests.models
    requests/models.py:60:0: R0903: Too few public methods (1/2) (too-few-public-methods)

    -----------------------------------
    Your code has been rated at 9.99/10

   This shows us that two classes with only one public method have been defined in
   ``auth.py``, in lines 72ff. and 100ff. Also in ``models.py`` there is a class
   with only one public method from line 60.

Nested code
-----------

    *«Flat is better than nested.»*

– Tim Peters, `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`_

Nested code makes it difficult to read and understand. You need to understand
and remember the conditions as you go through the nestings. Objectively, the
cyclomatic complexity increases as the number of code branches increases.

You can reduce nested methods with multiple nested ``if`` statements by
replacing levels with methods that return ``False`` if necessary. Then you can
use ``.count()`` to check if the number of errors is ``> 0``.

Another possibility is to use list comprehensions. This way the code

.. code-block:: python

    results = []
    for item in iterable:
        if item == match:
            results.append(item)

can be replaced by

.. code-block:: python

    results = [item for item in iterable if item == match]

.. note::
   The `itertools <https://docs.python.org/3/library/itertools.html>`_ of the
   Python standard library are often also good for reducing the nesting depth by
   creating functions to create iterators from data structures. You can also
   filter with itertools, e.g. with `filterfalse
   <https://docs.python.org/3/library/itertools.html#itertools.filterfalse>`_.

Query tools for complex dicts
-----------------------------

`JMESPath <https://jmespath.org/>`_, `glom <https://github.com/mahmoud/glom>`_,
`asq <https://asq.readthedocs.io/en/latest/>`_ and `flupy
<https://flupy.readthedocs.io/en/latest/>`_ can significantly simplify the query
of dicts in Python.

Reduce code with ``dataclasses`` and ``attrs``
----------------------------------------------

`dataclasses <https://docs.python.org/3/library/dataclasses.html>`_ were
introduced in Python 3.7 and there is also a backport for Python 3.6. They are
meant to simplify the definition of classes that are mainly created to store
values and can then be accessed via attribute search. Some examples are
``collection.namedtuple``, ``Typing.NamedTuple``, Recipes to Records [#]_ and
Nested Dicts [#]_. Data classes save you from writing and managing these
methods.

.. seealso::
   * `PEP 557 – Data Classes <https://www.python.org/dev/peps/pep-0557/>`_

`attrs <https://www.attrs.org/en/stable/>`_  is a Python package that has been
around much longer than ``dataclasses``, is more comprehensive and can also be
used with older versions of Python.

----

.. [#] `Records (Python recipe) <https://code.activestate.com/recipes/576555-records/>`_
.. [#] `Dot-style nested lookups over dictionary based data structures (Python recipe)
       <http://code.activestate.com/recipes/576586-dot-style-nested-lookups-over-dictionary-based-dat/>`_
