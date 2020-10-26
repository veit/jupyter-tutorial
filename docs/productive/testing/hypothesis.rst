Hypothesis
==========

`Hypothesis <https://hypothesis.readthedocs.io/>`_ is a library that allows you
to write tests that are parameterised from a source of examples. Then simple and
comprehensible examples are generated, which can be used to fail your tests and
to find errors with little effort.

Example
-------

To test lists with floating point numbers, many examples are tried, but only a
simple example is given in the report for each bug (unique exception type and
position):

.. code-block:: python

    from hypothesis import given
    from hypothesis.strategies import lists, floats

    @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
    def test_mean(ls):
        mean = sum(ls) / len(ls)
        assert min(ls) <= mean <= max(ls)

.. code-block:: console

    $ pipenv run pytest
    ============================= test session starts ==============================
    platform linux -- Python 3.6.8, pytest-4.6.2, py-1.8.0, pluggy-0.12.0
    …
    collected 1 item
    test_mean.py F                                                     [100%]
    =================================== FAILURES ===================================
    __________________________________ test_mean ___________________________________
        @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
    >   def test_mean(ls):
    test_mean.py:5:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    ls = [8.988465674311579e+307, 8.98846567431158e+307]

        @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
        def test_mean(ls):
            mean = sum(ls) / len(ls)
    >       assert min(ls) <= mean <= max(ls)
    E       assert inf <= 8.98846567431158e+307
    E        +  where 8.98846567431158e+307 = max([8.988465674311579e+307, 8.98846567431158e+307])

    test_mean.py:7: AssertionError
    ---------------------------------- Hypothesis ----------------------------------
    Falsifying example: test_mean(ls=[8.988465674311579e+307, 8.98846567431158e+307])
    =========================== 1 failed in 0.11 seconds ===========================

In our example we let  :doc:`pytest <pytest:index>` find the test and run it.
However, we could also have :defined class:`python:unittest.TestCase`
explicitly:

.. code-block:: python

    from hypothesis import given
    from hypothesis.strategies import lists, floats
    import unittest

    class TestMean(unittest.TestCase):
        @given(lists(floats(allow_nan=False, allow_infinity=False), min_size=1))
        def test_mean(ls):
            mean = sum(ls) / len(ls)
            assert min(ls) <= mean <= max(ls)

    if __name__ == '__main__':
        unittest.main()

Installation
------------

.. code-block:: console

    $ pipenv install hypothesis

Alternatively, Hypothesis can also be installed with `extras
<https://hypothesis.readthedocs.io/en/latest/extras.html>`_, e.g.

.. code-block:: console

    $ pipenv install hypothesis[numpy,pandas]

.. note::
   If you haven’t installed pipenv yet, you can find instructions on how to do
   this in :doc:`/first-steps/install`.

.. seealso::
   `Hypothesis for the Scientific Stack
   <https://hypothesis.readthedocs.io/en/latest/numpy.html>`_
