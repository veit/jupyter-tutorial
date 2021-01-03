pgMonitor
=========

`pgMonitor <https://access.crunchydata.com/documentation/pgmonitor/latest/>`_ is
an environment to visualise the healtch and performance of a PostgreSQL cluster.
It combines a suite of tools to faciliate the collection of important metrics,
including:

* number of connections
* Database size
* Replication lag
* Transaction wraparround
* Extra space taken up by your tables and indexes
* CPU, memory, I/O and uptime

It combines multiple open-source software packages to create a robust PostgreSQL
monitoring environment, including:

`PostgreSQL Exporter <https://github.com/wrouesnel/postgres_exporter>`_
    an open-source data export to Prometheus that supports collecting metrics
    from any PostgreSQL ≥ 9.1 server.
`Prometheus <https://prometheus.io/>`_
    an open-source metrics collector that is highly customizable.
`Grafana <https://grafana.com/>`_
    an open-source data visualiser that allows you to generate many different
    kinds of charts and graphs.

Installation and configuration
------------------------------

Installation and configuration instructions for each package are provided:

#. `PostgreSQL Exporter
   <https://access.crunchydata.com/documentation/pgmonitor/latest/exporter>`_
#. `Prometheus
   <https://access.crunchydata.com/documentation/pgmonitor/latest/prometheus>`_
#. `Grafana
   <https://access.crunchydata.com/documentation/pgmonitor/latest/grafana>`_
