Python2
=======

.. note::
    IPython 6.0 has ended support for Python 2. So if you want to install
    IPython for Python 2, use an older version:

    .. code-block:: console

        $ mkdir -p kernels/python2
        $ cd !$
        cd kernels/python2
        $ pipenv --two
        Creating a virtualenv for this project…
        ...
        $ pipenv install "ipykernel<=6"
        Installing ipykernel<=6…
        ...
        $ pipenv run python2 -m ipykernel install --user --name python2 --display-name "Python 2"
        Installed kernelspec python2 in /Users/veit/Library/Jupyter/kernels/python2
