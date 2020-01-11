Hypothesis
==========

`Hypothesis <https://hypothesis.readthedocs.io/>`_ ist eine Bibliothek, mit der
ihr Tests schreiben könnt, die anhand einer Quelle von Beispielen
parametrisiert werden. Anschließend werden einfache und nachvollziehbare
Beispiele generiert, anhand derer eure Tests fehlschlagen und ihr mit geringen
Aufwänden Fehler finden könnt.

Beispiel
--------

Zum Testen von Listen mit Fließkommazahlen werden viele Beispiele ausprobiert,
jedoch im Report nur ein einfaches Beispiel für jeden Bug (eindeutiger
*exception type* und Position) angegeben:

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

In unserem Beispiel haben wir :doc:`pytest <pytest:index>` den Test finden und
ausführen lassen. Wir hätten jedoch auch explizit einen
:class:`python:unittest.TestCase` definieren können:

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

Alternativ kann Hypothesis auch mit `Erweiterungen
<https://hypothesis.readthedocs.io/en/latest/extras.html>`_ installiert werden,
z.B.:

.. code-block:: console

    $ pipenv install hypothesis[numpy,pandas]

.. note::
   Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
   unter :doc:`/first-steps/install`.

.. seealso::
   `Hypothesis for the Scientific Stack
   <https://hypothesis.readthedocs.io/en/latest/numpy.html>`_

