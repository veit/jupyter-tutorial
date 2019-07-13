``unittest2``
=============

`unittest2 <http://pypi.org/project/unittest2>`_ ist ein Backport von
:mod:`unittest`, mit verbesserter API und besseren *Assertions* als in früheren
Python-Versionen. 
 
Beispiel
--------

Möglicherweise wollt ihr das Modul unter dem Namen ``unittest`` importieren um
die Portierung von Code auf neuere Versionen des Moduls in Zukunft zu
vereinfachen:

.. code-block:: python

    import unittest2 as unittest

    class MyTest(unittest.TestCase):
        ...

Auf diese Weise könnt ihr, wenn ihr zu einer neueren Python-Version wechselt und
das Modul ``unittest2`` nicht mehr benötigt, einfach den Import in Ihrem
Testmodul ändern, ohne dass ihr weiteren Code ändern müsst.

Installation
------------

.. code-block:: console

    $ pipenv install unittest2

.. note::
   Falls ihr pipenv noch nicht installiert hab, findet ihr eine Anleitung hierzu
   unter :doc:`/first-steps/install`.

