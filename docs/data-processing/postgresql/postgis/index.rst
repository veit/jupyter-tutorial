PostGIS
=======

`PostGIS <https://postgis.net/>`_ is an extension for PostgreSQL that includes
geographic objects and functions. The extension implements i.a. the `Simple
Feature Access <https://www.ogc.org/standards/sfa>`_ specification of the `Open
Geospatial Consortium <https://www.ogc.org/>`_. Although PostgreSQL already
supports geometry types, these are insufficient for geographic tasks. Therefore,
PostGIS creates its own data types that are better suited for geographic tasks.
The following geometry types are supported:

* OpenGIS with well-known text and well-known binary
* Extended Well-Known Text and Extended Well-Known Binary also with height
  information and/or measured values
* SQL/MM with Circularstring, Compoundcurve, Curvepolygon, Multicurve and
  Multisurface

`GEOS <https://trac.osgeo.org/geos/>`_, on the other hand, contains the numerous
spatial functions and operators for geographic data.

Finally, `pgRouting <https://pgrouting.org/>`_ contains routing functions based
on PostGIS.

In the  `OpenStreetMap <https://www.openstreetmap.org>`_ project, PostGIS is
used to render maps with `Mapnik <https://mapnik.org/>`_.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    optimising
    load
