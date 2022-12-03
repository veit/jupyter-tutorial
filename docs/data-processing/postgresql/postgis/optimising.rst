Optimising PostgreSQL for GIS database objects
==============================================

In the standard installation, PostgreSQL is configured very cautiously so that
it can run on as many systems as possible. However, GIS database objects are
large compared to text data. Therefore, PostgreSQL should be configured to work
better with these objects. To do this, we configure the
``/etc/postgresql/14/main/postgresql.conf`` file as follows:

#. ``shared_buffer`` should be changed to approx. 75% of the total working
   memory, but never fall below 128 kB:

   .. code-block::

    shared_buffers = 768MB

#. ``work_mem`` should be increased to at least 16MB:

   .. code-block::

    work_mem = 16MB

#. ``maintenance_work_mem`` should be increased to 128MB:

   .. code-block::

    maintenance_work_mem = 128MB

#. Finally, ``random_page_cost`` should be set to ``2.0``.

   .. code-block::

    random_page_cost = 2.0

PostgreSQL should be restarted for the changes to take effect:

.. code-block:: console

    $ sudo service postgresql restart
