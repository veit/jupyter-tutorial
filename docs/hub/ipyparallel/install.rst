Installation
============

#. Installation

   .. code-block:: console

    $ pipenv install "ipython[all]"

#. Activate notebook server extension:

   .. code-block:: console

    $ pipenv run jupyter serverextension enable --py ipyparallel
    Enabling: ipyparallel.nbextension
    - Writing config: /Users/veit/.jupyter
        - Validating...
          ipyparallel.nbextension  OK

#. Install notebook extension:

   .. code-block:: console

    $ pipenv run jupyter nbextension install --py ipyparallel
    …
    - Validating: OK

        To initialize this nbextension in the browser every time the notebook (or other app) loads:

              jupyter nbextension enable ipyparallel --py

#. Activate notebook extension:

   .. code-block:: console

    $ pipenv run jupyter nbextension enable --py ipyparallel
    Enabling tree extension ipyparallel/main...
          - Validating: OK
