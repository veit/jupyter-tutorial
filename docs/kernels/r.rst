R-Kernel
========

#. ZMQ

   Für Ubuntu & Debian:

   .. code-block:: console

        $ sudo apt install libzmq3-dev libcurl4-openssl-dev libssl-dev jupyter-core jupyter-client

#. R-Pakete

   .. code-block:: console

        $ R
        > install.packages(c('crayon', 'pbdZMQ', 'devtools'))
        ...
        --- Please select a CRAN mirror for use in this session ---
        ...
        33: Germany (Münster) [https]
        ...
        Selection: 33
        > devtools::install_github(paste0('IRkernel/', c('repr', 'IRdisplay', 'IRkernel')))
        Downloading GitHub repo IRkernel/repr@master
        from URL https://api.github.com/repos/IRkernel/repr/zipball/master
        ...

#. Kernel bereitstellen

   .. code-block:: console

        > IRkernel::installspec()
        ...
        [InstallKernelSpec] Installed kernelspec ir in /Users/veit/Library/Jupyter/kernels/ir3.3.3/share/jupyter/kernels/ir

   Ihr könnt den Kernel auch systemweit bereitstellen:

   .. code-block:: console

        > IRkernel::installspec(user = FALSE)

.. seealso::
    * `IRkernel Installation <https://irkernel.github.io/installation/>`_

