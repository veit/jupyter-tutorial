===========================
Git flow und seine Probleme
===========================

.. image:: git-flow.png

Git Flow war einer der ersten Vorschläge zur Verwendung von Git-Branches. Es
empfahl einen ``master``-Branch und einen separaten ``develop``-Branch sowie
diverse weitere Branches für Features, Releases und Hotfixes. Die verschiedenen
Entwicklungen sollten im ``develop``-Branch zusammengeführt werden, anschließend
in den ``release``-Branch überführt werden und schließlich im ``master``-Branch
landen. So ist Git Flow zwar ein wohldefinierter, aber komplexer Standard, der
praktisch die folgenden beiden Probleme hat:

* Die meisten Entwickler und Werkzeuge gehen von der Annahme aus, dass der
  ``master``-Branch der Hauptzweig ist von dem aus ``branch`` und ``merge``
  ausgeführt wird. Bei Git Flow entsteht nun zusätzlicher Aufwand da immer
  zunächst in den ``develop``-Branch gewechselt werden muss.
* Auch die ``hotfixes``- und ``release``-Branches bringen eine zusätzliche
  Komplexität, die nur in den seltensten Fällen Vorteile bringen dürfte.

Als Reaktion auf die Probleme von Git Flow entwickelten `GitHub
<https://guides.github.com/introduction/flow/>`_ und `Atlassian
<https://de.atlassian.com/git/tutorials/comparing-workflows>`_ einfachere
Alternativen, die sich meist auf sog. :doc:`feature-branches` beschränken.

.. seealso::
   `Vincent Driessen: A successful Git branching model
   <https://nvie.com/posts/a-successful-git-branching-model/>`_
