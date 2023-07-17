Appmode
=======

Jupyter extension that turns notebooks into web applications.

.. toctree::
    :titlesonly:
    :hidden:
    :maxdepth: 3

    app-example.ipynb

Example
-------

When you click on :menuselection:`Appmode` the notebook `app-example.ipynb
<app-example.ipynb>`_ becomes a clear web application for a calculator:

.. image:: appmode-app.png
   :scale: 53%
   :alt: Appmode app

Installation
------------

For the Jupyter service ``appmode`` must be installed with

.. code-block:: console

    $ pipenv install appmode
    Installing appmode…
    Collecting appmode
    …
    Installing collected packages: appmode
    Successfully installed appmode-0.6.0
    Adding appmode to Pipfile's [packages]…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    Updated Pipfile.lock (ea9a56)!
    Installing dependencies from Pipfile.lock (ea9a56)…
      🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 128/128 — 00:09:58
    …
    $ pipenv run jupyter nbextension enable --py --sys-prefix appmode
    Enabling notebook extension appmode/main...
          - Validating: OK
    $ pipenv run jupyter serverextension enable --py --sys-prefix appmode
    Enabling: appmode.server_extension
    - Writing config: /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/../etc/jupyter
        - Validating...
          appmode.server_extension  OK

Configuration
-------------

Server-side configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

The server can be configured with the following three options:

``Appmode.trusted_path``
    runs the app mode only for notebooks under this path; Default setting: *no
    restrictions*.

``Appmode.show_edit_button``
    displays :menuselection:`Edit App` button in app mode; Default setting:
    ``True``.

``Appmode.show_other_buttons``
    shows other buttons in app mode, for example
    :menuselection:`Logout`; Default setting: ``True``.

You can find more information about the server configuration in
:doc:`/notebook/config`.

Client-side configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

The UI elements can also be adapted on the client side in the `custom.js
<https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/JavaScript%20Notebook%20Extensions.html#custom.js>`_
file, for example with:

.. code-block:: Javascript

    // Hides the edit app button.
    $('#appmode-leave').hide();

    // Hides the kernel busy indicator.
    $('#appmode-busy').hide();

    // Adds a loading message.
    $('#appmode-loader').append('<h2>Loading...</h2>');

.. note::
    Hiding the :menuselection:`Edit App` button does not prevent users from
    exiting app mode by manually changing the URL.
