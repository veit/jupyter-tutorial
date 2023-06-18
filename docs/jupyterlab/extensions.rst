JupyterLab extensions
=====================

JupyterLab is designed as an extensible environment. In doing so, JupyterLab
extensions can customise any part of JupyterLab. They can provide new themes,
file viewers and editors, or renderers for rich outputs in
:doc:`../notebook/index`.

.. seealso::
   `JupyterLab Extensions by Examples
   <https://github.com/jupyterlab/extension-examples>`_

Installing extensions
---------------------

A JupyterLab extension contains JavaScript that is installed in JupyterLab and
executed in the browser. Most JupyterLab extensions can be installed with
:term:`pip`. These packages can also contain server-side components that are
required for the extension to function.

Since JupyterLab ≥ 4, the default extension manager uses :term:`PyPI` as a
source for the available extensions and :term:`pip` to install them. An
extension is listed if the Python package has the :term:`trove classifier
<trove-classifiers>` ``Framework :: Jupyter :: JupyterLab :: Extensions ::
Prebuilt``.

.. warning::
   It does not check if the extension is compatible with the current JupyterLab
   version.

.. danger::
   Installing an extension allows arbitrary code to be executed on the server,
   kernel and browser. Therefore, avoid installing extensions that you do not
   trust.

Configuring the Extension Manager
---------------------------------

By default, there are two extension managers provided by JupyterLab:

``pypi``
    Default setting that allows the installation from :term:`pypi.org`.
``readonly``
    shows the installed extensions with the possibility to disable or enable
    them.

You can specify the manager with the command line option
``--LabApp.extension_manager``, for example :samp:`jupyter lab
--LabApp.extension_manager={readonly}`.

When searching for extensions in the extension manager, JupyterLab usually shows
all search results and any source extension can be installed. However, to
increase security, JupyterLab can be configured so that extensions can only be
activated using the block or allow lists.

You can define the loading of the lists with ``blocked_extensions_uris`` or
``allowed_extensions_uris``, which contain a list of comma-separated URIs, for
example
:samp:`--LabServerApp.blocked_extensions_uris=http://example.com/blocklist.json`
with the following :file:`blocklist.json` file:

.. code-block:: json

    {
      "blocked_extensions": [
        {
          "name": "@jupyterlab-examples/launcher",
          "type": "jupyterlab",
          "reason": "@jupyterlab-examples/launcher is blocklisted for test purpose - Do NOT take this for granted!!!",
          "creation_date": "2020-03-11T03:28:56.782Z",
          "last_update_date":  "2020-03-11T03:28:56.782Z"
        }
      ]
    }

Another example shows an :file:`allowlist.json` file that allows all extensions
of the `JupyterLab organisation <https://www.npmjs.com/org/jupyterlab>`_:

.. code-block:: json

    {
      "allowed_extensions": [
        {
          "name": "@jupyterlab/*",
          "type": "jupyterlab",
          "reason": "All @jupyterlab org extensions are allowed, of course…",
          "creation_date": "2020-03-11T03:28:56.782Z",
          "last_update_date":  "2020-03-11T03:28:56.782Z"
        }
      ]
    }
