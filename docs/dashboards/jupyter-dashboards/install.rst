Installation of Jupyter dashboards
==================================

.. code-block:: console

    $ uv add jupyter_dashboards
    $ uv run jupyter dashboards quick-setup --sys-prefix
    …
    Enabling notebook extension jupyter_dashboards/notebook/main...
          - Validating: OK
    $ uv run jupyter nbextension enable jupyter_dashboards --py --sys-prefix
    Enabling notebook extension jupyter_dashboards/notebook/main...
          - Validating: OK
