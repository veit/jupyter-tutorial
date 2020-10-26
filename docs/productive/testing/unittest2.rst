``unittest2``
=============

`unittest2 <http://pypi.org/project/unittest2>`_ is a backport of
:mod:`unittest`, with improved API and better assertions than in previous Python
versions.

Example
-------

You may want to import the module under the name ``unittest`` to simplify the
porting of code to newer versions of the module in the future:

.. code-block:: python

    import unittest2 as unittest

    class MyTest(unittest.TestCase):
        ...

In this way, if you switch to a newer Python version and no longer need the
module ``unittest2``, you can simply change the import in your test module
without having to change any further code.

Installation
------------

.. code-block:: console

    $ pipenv install unittest2

.. note::
   If you haven’t installed pipenv yet, you can find instructions on how to do
   this in :doc:`/first-steps/install`.
