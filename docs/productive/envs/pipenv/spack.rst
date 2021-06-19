Pipenv and Spack
================

Pipenv has already been used to :doc:`install Jupyter notebooks
</first-steps/install>`. However, we need Pipenv for our :doc:`Spack
environments <../../envs/spack/envs>` to be able to generate binary-compatible
builds with Spack on the one hand and to be able to easily use Python packages
for data collection, visualization, etc. on the other.

To do this, first activate the appropriate Python version from the Spack
environment:

   .. code-block:: console

    $ spack env activate python-374
    $ spack env status
    ==> In environment python-374
    $ which python
    /Users/veit/jupyter-tutorial/spackenvs/python-374/.spack-env/view/bin/python

Then you can install the existing Pipenv environment with:

   .. code-block:: console

    $ cd ~/jupyter-tutorial/pipenvs/python-374/
    $ pipenv --python=/Users/veit/jupyter-tutorial/spackenvs/python-374/.spack-env/view/bin/python --site-packages
    $ pipenv install
    Creating a virtualenv for this project…
    Pipfile: /Users/veit/jupyter-tutorial/pipenvs/python-374/Pipfile
    Using /Users/veit/jupyter-tutorial/spackenvs/python-374/.spack-env/view/bin/python3.7 (3.7.4) to create virtualenv…
    …

This uses the environment installed with Spack and installs additional packages.

.. seealso::

    * `Pipenv and Other Python Distributions
      <https://pipenv.pypa.io/en/latest/advanced/#pipenv-and-other-python-distributions>`_
