Prozedurale Programmiersprachen
===============================

Mit PostgreSQL können benutzerdefinierte Funktionen außer in SQL und C auch in
anderen Sprachen geschrieben werden.

In der Standarddistribution von PostgreSQL stehen derzeit vier prozedurale
Sprachen zur Verfügung:

* `PL/pgSQL <https://www.postgresql.org/docs/current/plpgsql.html>`_
* `PL/Tcl <https://www.postgresql.org/docs/current/pltcl.html>`_
* `PL/Perl <https://www.postgresql.org/docs/current/plperl.html>`_
* `PL/Python <https://www.postgresql.org/docs/current/plpython.html>`_

Es sind zusätzliche prozedurale Programmiersprachen verfügbar, die jedoch nicht
in der Kerndistribution enthalten sind:

* `PL/Java <https://tada.github.io/pljava/>`_
* `PL/Lua <https://github.com/pllua/pllua>`_
* `PL/R  <http://www.joeconway.com/plr.html>`_
* `PL/sh <https://github.com/petere/plsh>`_
* `PL/v8 <https://github.com/plv8/plv8>`_

.. seealso::
   `External Procedural Languages
   <https://www.postgresql.org/docs/current/external-pl.html>`_

Zusätzlich können andere Sprachen definiert werden, s. `Writing A Procedural
Language Handler <https://www.postgresql.org/docs/current/plhandler.html>`_.
