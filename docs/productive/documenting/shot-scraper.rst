shot-scraper
============

`shot-scraper <https://simonwillison.net/2022/Mar/10/shot-scraper/>`_ is a tool
to automate the process of updating screenshots.

Installation
------------

.. code-block:: console

   $ pipenv install shot-scraper
   $ shot-scraper install

.. note::
   The second line installs the required browser.

Use
---

shot-scraper can be used in two ways

#. …for single screenshots on the command line:

   .. code-block:: console

        $  shot-scraper https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html -o ~/Downloads/clean-prep.png

   …or with additional options, e.g. for JavaScript and CSS selectors:

    .. code-block::

        $ pipenv run shot-scraper https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html -s '#overview' -o ~/Downloads/clean-prep.png

#. …for a set of screenshots configured in a YAML file:

   .. code-block:: yaml

        - url: https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html
          output: ~/Downloads/clean-prep.png
        - url: https://www.example.org/
          width: 736
          quality: 40
          output: example.jpg

   Afterwards ``shot-scraper multi`` can be used, for example:

   .. code-block:: console

        $ pipenv run shot-scraper multi shot.yaml
        Screenshot of 'https://jupyter-tutorial.readthedocs.io/de/latest/clean-prep/index.html' written to '~(Downloads/clean-prep.png'
        Screenshot of 'https://www.example.org/' written to 'example.jpg'

   .. seealso::
      * In the `README.md
        <https://github.com/simonw/shot-scraper/blob/main/README.md>`_ file you
        will find a complete overview of the possible options.
      * In the shot-scraper-demo repository you will find a much more
        comprehensive `shots.yaml
        <https://github.com/simonw/shot-scraper-demo/blob/main/.github/workflows/shots.yml>`_
        file.

GitHub Actions
--------------

shot-scraper can be easily integrated into GitHub Actions. The shot-scraper-demo
repository also contains an examplary `shots.yml
<https://github.com/simonw/shot-scraper-demo/blob/main/.github/workflows/shots.yml>`_. Once a day, two screenshots are created and transferred back to the
repository. Note, however, that saving image files that change frequently can
make the revision history very unreadable. Therefore, you should use
shot-scraper with caution together with GitHub Actions.
