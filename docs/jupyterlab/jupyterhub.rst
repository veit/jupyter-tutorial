JupyterLab on JupyterHub
========================

JupyterLab works by default with :doc:`../hub/index` ≥ 1.0 and can even run
alongside classic :doc:`notebooks  <../notebook/index>`.

When JupyterLab is used with JupyterHub, additional menu items are displayed in
the :menuselection:`File` menu to :menuselection:`Log Out` or to call up the
:menuselection:`Hub Control Panel`.

If JupyterLab is not yet the default, you can change the configuration in
:file:`jupyterhub_config.py`:

.. code-block:: python

   c.Spawner.default_url = "/lab"
