Python2
=======

.. note::
    IPython 6.0 hat die Unterstützung für Python 2 eingestellt. Wenn ihr also
    IPython für Python 2 installieren wollt, verwendet eine ältere Version:

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
        $ pipenv run python2 -m ipykernel install --user
        Installed kernelspec python2 in /Users/veit/Library/Jupyter/kernels/python2

