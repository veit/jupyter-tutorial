Mock
====

:mod:`unittest.mock` is a Python test library. As of Python 3.3, it is available
in the Python standard library.

Example
-------

It allows you to test parts of your application with `mock objects
<https://en.wikipedia.org/wiki/Mock_object>`_ and make assertions about how they
have been used.

For example, you can do a monkey patch for a method:

.. code-block:: python

    from mock import MagicMock
    thing = ProductionClass()
    thing.method = MagicMock(return_value=3)
    thing.method(3, 4, 5, key='value')

    thing.method.assert_called_with(3, 4, 5, key='value')

The ``patch`` decorator can be used to create mock classes or objects in a
module under test. In the following example, an external search system is
replaced by a mock class that always delivers the same result:

.. code-block:: python

    def mock_search(self):
        class MockSearchQuerySet(SearchQuerySet):
            def __iter__(self):
                return iter(["foo", "bar", "baz"])
        return MockSearchQuerySet()

    @mock.patch('myapp.SearchForm.search', mock_search)
    def test_new_watchlist_activities(self):
        self.assertEqual(len(myapp.get_search_results(q="fish")), 3)

``SearchForm`` refers here to the imported class reference in ``myapp``, not to
the ``SearchForm`` class itself.

``get_search_results`` performs a search and iterates over the result.

Installation
------------

For older Python versions it can be installed with

.. code-block:: console

    $ pipenv install mock

.. note::
   If you haven’t installed pipenv yet, you can find instructions on how to do
   this in :doc:`/first-steps/install`.

.. seealso::
   With `responses <https://github.com/getsentry/responses>`_ you can create
   mock objects for the :doc:`/data/requests/index` library.
