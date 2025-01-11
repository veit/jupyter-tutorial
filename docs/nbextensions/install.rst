Installation
============

#. Installation with Pipenv:

   .. code-block:: console

      $ uv add jupyter_contrib_nbextensions

#. Installation of the associated Javascript and CSS files:

   .. code-block:: console

      $ uv run --with jupyter jupyter contrib nbextension install --user
      [I 20:57:19 InstallContribNbextensionsApp] jupyter contrib nbextension install --user
      [I 20:57:19 InstallContribNbextensionsApp] Installing jupyter_contrib_nbextensions nbextension files to jupyter data directory
      …
      [I 20:57:20 InstallContribNbextensionsApp] - Writing config: /Users/veit/.jupyter/jupyter_nbconvert_config.json
      [I 20:57:20 InstallContribNbextensionsApp] --  Writing updated config file /Users/veit/.jupyter/jupyter_nbconvert_config.json

#. Check the installation:

   .. code-block:: console

      $ uv run --with jupyter jupyter nbextension list
      Known nbextensions:
        config dir: /Users/veit/.jupyter/nbconfig
          notebook section
            nbextensions_configurator/config_menu/main  enabled
            - Validating: problems found:
              - require?  X nbextensions_configurator/config_menu/main
            contrib_nbextensions_help_item/main  enabled
            - Validating: OK
          tree section
            nbextensions_configurator/tree_tab/main  enabled
            - Validating: problems found:
              - require?  X nbextensions_configurator/tree_tab/main
        config dir: /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/../etc/jupyter/nbconfig
          notebook section
            jupyter-js-widgets/extension  enabled
            - Validating: OK

#. Latex environments

   .. code-block:: console

      $ uv run --with jupyter jupyter nbextension install --py latex_envs --user
      Installing /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/lib/python3.7/site-packages/latex_envs/static -> latex_envs
      …
      - Validating: OK
          To initialize this nbextension in the browser every time the notebook (or other app) loads:
                jupyter nbextension enable latex_envs --user --py
      …
      $ uv run --with jupyter jupyter nbextension enable --py latex_envs --user
      Enabling notebook extension latex_envs/latex_envs…
            - Validating: OK

#. `yapf <https://pypi.org/project/yapf/>`_ Code Prettyfier

   … for Python:

   .. code-block:: console

      $ uv add yapf

   … for Javascript:

   .. code-block:: console

      $ npm install js-beautify
      …
      + js-beautify@1.10.0
      added 29 packages from 21 contributors and audited 32 packages in 2.632s
      found 0 vulnerabilities

   … for R:

   .. code-block:: console

      $ Rscript -e 'install.packages(c("formatR", "jsonlite"), repos="http://cran.rstudio.com")'
      Installiere Pakete nach ‘/usr/local/lib/R/3.6/site-library’
      …

#. Highlighter

   .. code-block:: console

      $ uv run --with jupyter jupyter nbextension install https://rawgit.com/jfbercher/small_nbextensions/master/highlighter.zip  --user
      Downloading: https://rawgit.com/jfbercher/small_nbextensions/master/highlighter.zip -> /var/folders/_4/cs4t3m8d4ys8lcs67r3lghtw0000gn/T/tmpn9qrcrdz/highlighter.zip
      Extracting: /var/folders/_4/cs4t3m8d4ys8lcs67r3lghtw0000gn/T/tmpn9qrcrdz/highlighter.zip -> /Users/veit/Library/Jupyter/nbextensions
      $ uv run --with jupyter jupyter nbextension enable highlighter/highlighter
      Enabling notebook extension highlighter/highlighter…
            - Validating: OK

#. nbTranslate

   .. code-block:: console

      $ uv add jupyter_latex_envs --upgrade --user
      Installing jupyter_latex_envs…
      …
      $ uv run --with jupyter jupyter nbextension install --py latex_envs --user
      Installing /srv/jupyter/.local/share/virtualenvs/jupyterhub-aFv4x91W/lib/python3.5/site-packages/latex_envs/static -> latex_envs
      …
      $ uv run --with jupyter jupyter nbextension enable --py latex_envs
