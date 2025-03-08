Installation
============

You can install Panel in the virtual environment of your Jupyter kernel with:

.. code-block:: console

    $ uv add panel

.. tip::
   `watchfiles
   <https://watchfiles.helpmanual.io>`_ supports the autoreload functions of
   Panel if the ``--dev`` mode is activated:

   .. code-block:: console

      $ uv add --dev watchfiles

.. tip::
   For syntax highlighting, `pygments <https://pygments.org/>`_ should also be
   installed:

   .. code-block:: console

      $ uv add pygments

.. seealso::
   If you want to use Panel for example in VSCode or Google Colab, have a look
   at `Develop in other notebook environments
   <https://panel.holoviz.org/how_to/notebook/other_nb.html>`_.
