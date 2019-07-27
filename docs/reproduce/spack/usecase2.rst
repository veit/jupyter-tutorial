Use Case 2: Python und andere interpretierte Sprachen
=====================================================

.. code-block:: console

    $ spack install python@2.7.10
    ==> Building python.
    ==> Successfully installed python.
      Fetch: 5.01s. Build: 97.16s. Total: 103.17s.
    [+] /srv/jupyterhub/spack/opt/spack/linux-x86_64/gcc-4.9.2/python-2.7.10-y2zr767
    $ spack extensions python@2.7.10
    ==> python@2.7.10%gcc@4.9.2=linux-x86_64-y2zr767
    ==> 49 extensions:
    geos            py-h5py         py-numpy        py-pypar            py-setuptools
    libxml2         py-ipython      py-pandas       py-pyparsing        py-shiboken
    py-basemap      py-libxml2      py-pexpect      py-pyqt             py-sip
    py-biopython    py-lockfile     py-pil          py-pyside           py-six
    py-cffi         py-mako         py-pmw          py-python-daemon    py-sphinx
    py-cython       py-matplotlib   py-pychecker    py-pytz             py-sympy
    py-dateutil     py-mock         py-pycparser    py-rpy2             py-virtualenv
    py-epydoc       py-mpi4py       py-pyelftools   py-scientificpython py-yapf
    py-genders      py-mx           py-pygments     py-scikit-learn     thrift
    py-gnuplot      py-nose         py-pylint       py-scipy
    ==> 3 installed:
    -- linux-x86_64 / gcc@4.9.2 ------------------------------------
    py-nose@1.3.6   py-numpy@1.9.2  py-setuptools@18.1
    ==> None currently activated.

.. code-block:: console

    $ spack activate py-numpy
    ==> Activated extension py-setuptools-18.1-gcc-4.9.2-ru7w3lx
    ==> Activated extension py-nose-1.3.6-gcc-4.9.2-vudjpwc
    ==> Activated extension py-numpy-1.9.2-gcc@4.9.2-45hjazt

.. code-block:: console

    $ spack deactivate -a py-numpy
    ==> Deactivated extension py-numpy-1.9.2-gcc@4.9.2-45hjazt
    ==> Deactivated extension py-nose-1.3.6-gcc-4.9.2-vudjpwc
    ==> Deactivated extension py-setuptools-18.1-gcc-4.9.2-ru7w3lx


