Procedural programming languages
================================

With PostgreSQL, user-defined functions can be written in languages other than
SQL and C.

There are currently four procedural languages available in the standard
PostgreSQL distribution:

* `PL/pgSQL <https://www.postgresql.org/docs/current/plpgsql.html>`_
* `PL/Tcl <https://www.postgresql.org/docs/current/pltcl.html>`_
* `PL/Perl <https://www.postgresql.org/docs/current/plperl.html>`_
* `PL/Python <https://www.postgresql.org/docs/current/plpython.html>`_

Additional procedural programming languages are available but are not included
in the core distribution:

* `PL/Java <https://tada.github.io/pljava/>`_
* `PL/Lua <https://github.com/pllua/pllua>`_
* `PL/R  <http://www.joeconway.com/plr.html>`_
* `PL/sh <https://github.com/petere/plsh>`_
* `PL/v8 <https://github.com/plv8/plv8>`_

.. seealso::
   `External Procedural Languages
   <https://www.postgresql.org/docs/current/external-pl.html>`_

In addition, other languages can be defined, see also `Writing A Procedural
Language Handler <https://www.postgresql.org/docs/current/plhandler.html>`_.
