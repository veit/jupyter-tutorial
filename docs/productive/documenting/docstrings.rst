Docstrings
==========

Mit der Sphinx-Erweiterung `sphinx.ext.autodoc
<http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ lassen
sich auch Docstrings in die Dokumentation übernehmen. Dabei lassen sich die
folgenden drei Direktiven angeben:

.. rst:directive::  automodule
                    autoclass
                    autoexception

   Diese dokumentieren ein Modul, eine Klasse oder eine Exception anhand des
   Docstrings des jeweiligen Objekts.

Installation
------------

Üblicherweise ist ``sphinx.ext.autodoc`` bereits in der
Sphinx-Konfigurationsdatei ``docs/conf.py`` angegeben::

    extensions = [
        'sphinx.ext.autodoc',
        …
    ]

Wenn euer Paket und die zugehörige Dokumentation Teil des gleichen Repository
sind, haben sie immer die gleiche relative Position im Dateisystem. In diesem
Fall könnt ihr die Sphinx-Konfiguration einfach so bearbeiten, dass ``sys.path``
den relativen Pfad zum Paket angibt, also::

    sys.path.insert(0, os.path.abspath('..'))
    import requests

Wen ihr eure Sphinx-Dokumentation in einer virtuellen Umgebung installiert
habt, könnt ihr dort auch euer Paket installieren mit::

    $ pipenv install my.package

bzw., wenn ihr auch das Paket weiterentwickeln wollt mit::

    $ pipenv install -e https://github.com/veit/my.package.git

Beispiele
---------

Hier einige Beispiele aus der API-Dokumentation des `requests
<http://docs.python-requests.org/en/master/>`_-Modul:

.. code-block:: rest

    Developer Interface
    ===================

    .. module:: requests
    …
    Main Interface
    --------------
    …
    .. autofunction:: head
    …
    Exceptions
    ----------

    .. autoexception:: requests.RequestException
    …
    Request Sessions
    ----------------
    …
    .. autoclass:: Session
       :inherited-members:

Dies führt zu :doc:`docstrings-example`, generiert aus den folgenden Docstrings:

* `requests.head <http://docs.python-requests.org/en/master/_modules/requests/api/#head>`_
* `requests.RequestException <http://docs.python-requests.org/en/master/_modules/requests/exceptions/#RequestException>`_
* `requests.Session <http://docs.python-requests.org/en/master/_modules/requests/sessions/#Session>`_

.. autoclass:: Session
   :inherited-members:

.. note::
   Ihr solltet euch beim Schreiben von  Docstrings an die folgenden
   Anleitungen halten:

   * `Python Style Guide: comments
     <https://www.python.org/dev/peps/pep-0008/#comments>`_
   * `The Docstring Conventions Guide
     <https://www.python.org/dev/peps/pep-0257/#specification>`_

``sphinx-autodoc-typehints``
----------------------------

Mit `PEP 484 <https://www.python.org/dev/peps/pep-0484/>`_ wurde eine
Standardmethode zum Ausdrücken von Typen in Python-Code eingeführt. Damit lassen
sich auch Typen in Docstrings anders ausdrücken. Dabei bietet die Variante mit
Typen gemäß PEP 484 den Vorteil, dass Typenprüfer und IDEs zur statischen
Codeanalyse genutzt werden können.

Python 3 type annotations
    ::

        def func(arg1: int, arg2: str) -> bool:
            """Summary line.

            Extended description of function.

            Args:
                arg1: Description of arg1
                arg2: Description of arg2

            Returns:
                Description of return value

            """
            return True

Types in Docstrings
    ::

        def func(arg1, arg2):
            """Summary line.

            Extended description of function.

            Args:
                arg1 (int): Description of arg1
                arg2 (str): Description of arg2

            Returns:
                bool: Description of return value

            """
            return True

.. note::
   `Python2/3-kompatible Anmerkungen
   <https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code>`_
   werden aktuell nicht von Sphinx unterstützt und erscheinen nicht in der
   generierten Dokumentation.

``sphinx.ext.napoleon``
-----------------------

Die Sphinx-Erweiterung `sphinx.ext.napoleon
<https://sphinxcontrib-napoleon.readthedocs.io/>`_ erlaubt euch, verschiedene
Abschnitte in Docstrings zu definieren, u.a.:

* ``Attributes``
* ``Example``
* ``Keyword Arguments``
* ``Methods``
* ``Parameters``
* ``Warning``
* ``Yield``

Dabei unterscheidet ``sphinx.ext.napoleon`` zwei Stilen von Docstrings:

* `Google <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_
* `NumPy <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html>`_

Die wesentlichen Unterschiede sind, dass Google Einrückungen verwendet und NumPy
Unterstriche:

Google
    ::

        def func(arg1, arg2):
            """Summary line.

            Extended description of function.

            Args:
                arg1 (int): Description of arg1
                arg2 (str): Description of arg2

            Returns:
                bool: Description of return value

            """
            return True

NumPy
    ::

        def func(arg1, arg2):
            """Summary line.

            Extended description of function.

            Parameters
            ----------
            arg1 : int
                Description of arg1
            arg2 : str
                Description of arg2

            Returns
            -------
            bool
                Description of return value

            """
            return True

Die detailierten Konfigurationsoptionen findet ihr in `sphinxcontrib.napoleon.Config
<https://sphinxcontrib-napoleon.readthedocs.io/en/latest/sphinxcontrib.napoleon.html#sphinxcontrib.napoleon.Config>`_.
