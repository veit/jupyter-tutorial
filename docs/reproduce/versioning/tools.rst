Git-Tools für Notebooks
=======================

``nbdime``
----------

`nbdime <https://nbdime.readthedocs.io/>`_ ist ein GUI für `nbformat
<https://nbformat.readthedocs.io/>`_-Diffs und ersetzt `nbdiff
<https://github.com/tarmstrong/nbdiff>`_. Es versucht *Content-Aware*-Diffing
sowie das Merging von Notebooks, beschränkt sich nicht nur auf die Darstellung
von Diffs, sondern verhindert auch, dass unnötige Änderungen eingecheckt werden.

.. _nbstripout_label:

``nbstripout``
--------------

`nbstripout <https://github.com/kynan/nbstripout>`_ automatisiert *Clear all
outputs*. Es nutzt `nbformat <https://nbformat.readthedocs.io/>`_ und ein paar
Automagien um ``git config`` einzurichten. Meines Erachtens hat es jedoch zwei
Nachteile: es beschränkt sich auf den problematischen Metadaten-Abschnitt und
es ist langsam.

