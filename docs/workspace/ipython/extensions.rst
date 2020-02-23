IPython-Erweiterungen
=====================

IPython-Erweterungen sind Python-Module, die das Verhalten der Shell ändern. Sie
werden mit einem importierbaren Modulnamen bezeichnet und befinden sich
üblicherweise in ``.ipython/extensions/``.

Einige wichtige Erweiterungen sind bereits in IPython enthalten:
:label:`extensions_autoreload` und :label:`extensions_storemagic`. Andere
Erweiterungen findet ihr im  `Extensions Index
<https://github.com/ipython/ipython/wiki/Extensions-Index>`_ oder auf PyPI unter
dem `IPython tag <https://pypi.python.org/pypi?:action=browse&c=586>`_.

.. seealso::
    * `IPython extensions docs
      <https://ipython.readthedocs.io/en/stable/config/extensions/index.html>`_

Erweiterungen verwenden
-----------------------

Die ``%load_ext``-Magie kann verwendet werden um Erweiterungen zu laden während
IPython ausgeführt wird. 

.. code-block:: ipython

    %load_ext myextension

Alternativ kann eine Erweiterung auch bei jedem Start von IPython geladen
werden, indem sie in der IPython-Konfigurationsdate aufgelistet wird:

.. code-block:: Python

    c.InteractiveShellApp.extensions = [
        'myextension'
    ]

Falls ihr noch keine IPython-Konfigurationsdatei erstellt habt, könnt ihr dies
mit:

.. code-block:: console

    $ ipython profile create [profilename]

Falls kein Profilname angegeben wird, wird ``default`` verwendet. Üblicherweise
wird die Datei dann in ``~/.ipython/profile_default/`` erstellt und je nach
Verwendungszweck benannt: ``ipython_config.py`` wird für alle IPython-Befehle
verwendet, während ``ipython_notebook_config.py`` nur für Befehle in
IPython-Notebooks Verwendung findet.

IPython-Erweiterungen schreiben
-------------------------------

Eine IPython-Erweiterung ist ein importierbares Python-Modul, das über spezielle
Funktionen zum Laden und Entladen verfügt:

.. code-block:: python

    def load_ipython_extension(ipython):
        # The `ipython` argument is the currently active `InteractiveShell`
        # instance, which can be used in any way. This allows you to register
        # new magics or aliases, for example.

    def unload_ipython_extension(ipython):
        # If you want your extension to be unloadable, put that logic here.

.. seealso::
    * :label:`defining_magics`

