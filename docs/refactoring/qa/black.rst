Black
=====

`Black <https://github.com/psf/black>`_ formats your code in a nice and
deterministic format.

.. seealso::
    Was lesbaren Code auszeichnet, ist gut beschrieben im Trey Hunners Blog-Post
    `Craft Your Python Like Poetry
    <https://treyhunner.com/2017/07/craft-your-python-like-poetry/>`_.

Installation
------------

.. code-block:: console

    $ pipenv install black

Check
-----

Then you can check the installation with

.. code-block:: console

    $ pipenv run black /path/to/your/source/file

Integration
-----------

With `jupyter-black <https://github.com/drillan/jupyter-black>`_ you can already
use Black in your Jupyter notebooks.

.. seealso::
    Integration into other editors such as PyCharm, Wing IDE or Vim is also
    possible, see `Editor integration
    <https://black.readthedocs.io/en/stable/integrations/editors.html>`_

Configuration
-------------

In contrast to Black’s standard 88-character formatting, however, I prefer a
line length of 79 characters.

For this you can enter the following in ``pyproject.toml``:

.. code-block:: toml

    [tool.black]
    line-length = 79

.. seealso::
    You can get more information about the configuration of Black in the Toml
    file in `pyproject.toml
    <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file>`_.
