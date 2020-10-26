tox
===

`tox <https://tox.readthedocs.io/>`_ is a tool for automating ``virtualenv``
environment management and testing with multiple interpreter configurations.

With ``tox`` you can configure complex multi-parameter test matrices via a
simple configuration file in the ``INI`` style.

Example
-------

Creates a ``tox.ini`` file:

.. code-block:: ini

    [tox]
    envlist = py27,py36

    [testenv]
    deps = pytest
    commands =
        pytest

When you call ``pipenv run tox``, the following steps are performed:

#. Optionally create a Python package with

   .. code-block:: console

        $ pipenv run python setup.py sdist

#. Create the environments specified in ``envlist``

   In each of these environments, then

   #. the dependencies and packages are installed
   #. the commands specified in ``commands`` are executed

#. Create a report with the results from each of the environments, e.g.

   .. code-block:: text

        ____________________ summary ____________________
        py27: commands succeeded
        ERROR:   py36: commands failed

Installation
------------

.. code-block:: console

    $ pipenv install tox

.. note::
   If you haven't installed pipenv yet, you can find instructions on how to do
   this in unter :doc:`/first-steps/install`.

.. seealso::

   * `Examples <https://tox.readthedocs.io/en/latest/examples.html>`_
   * `Plugins <https://tox.readthedocs.io/en/latest/plugins.html>`_
