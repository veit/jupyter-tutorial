Mock
====

:mod:`unittest.mock` ist eine Python-Testbibliothek. Ab Python 3.3 ist sie in
der Python-Standardbibliothek verfügbar.

Beispiel
--------

Es ermöglicht euch, Teile eurer zu testenden Anwendung durch `Mock-Objekte
<https://de.wikipedia.org/wiki/Mock-Objekt>`_ zu testen und *Assertions*
darüber zu treffen, wie diese verwendet wurden.

Zum Beispiel könnt ihr einen Monkeypatch für eine Methode ausführen:

.. code-block:: python

    from mock import MagicMock
    thing = ProductionClass()
    thing.method = MagicMock(return_value=3)
    thing.method(3, 4, 5, key='value')

    thing.method.assert_called_with(3, 4, 5, key='value')

Um Mock-Klassen oder- Objekte in einem zu testenden Modul zu erzeugen, kann der
``patch``-Dekorator verwendet werden. Im folgenden Beispiel wird ein externes
Suchsystem durch eine Mock-Klasse ersetzt, die immer das gleiche Ergebnis
liefert:

.. code-block:: python

    def mock_search(self):
        class MockSearchQuerySet(SearchQuerySet):
            def __iter__(self):
                return iter(["foo", "bar", "baz"])
        return MockSearchQuerySet()

    @mock.patch('myapp.SearchForm.search', mock_search)
    def test_new_watchlist_activities(self):
        self.assertEqual(len(myapp.get_search_results(q="fish")), 3)

``SearchForm`` bezieht sich hier auf die importierte Klassenreferenz in
``myapp``, nicht auf die ``SearchForm``-Klasse selbst.

``get_search_results`` führt eine Suche durch und iteriert über das Ergebnis.

Installation
------------

Für ältere Python-Versionen kann sie installiert werden mit

.. code-block:: console

    $ pipenv install mock

.. note::
   Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
   unter :doc:`/first-steps/install`.
