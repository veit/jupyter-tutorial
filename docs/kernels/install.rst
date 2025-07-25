Install, view and start the kernel
==================================

Install a kernel
----------------

Kernels are searched for in the following directories, for example:

* :file:`/srv/jupyter/.local/share/jupyter/kernels`
* :file:`/usr/local/share/jupyter/kernels`
* :file:`/usr/share/jupyter/kernels`
* :file:`/srv/jupyter/.ipython/kernels`

To make your new environment available as a Jupyter kernel in one of the
directories, you should install ipykernel:

.. code-block:: console

   $ uv add --dev ipykernel

You can then register your kernel, for example with

.. code-block:: console

   $ uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --prefix /srv/jupyter/.ipython/kernels --name python311 --display-name 'Python 3.11 Kernel'

:samp:`--user`
    installs the kernel for the current user and not system-wide.
:samp:`--env {ENV} {VALUE}`
    sets environment variables for the kernel.
:samp:`--prefix {/PATH/TO/KERNEL}`
    specifies the path where the Jupyter kernel is to be installed.
:samp:`name {NAME}`
    gives a name for the ``kernelspec``. This is required in order to be able to
    use several IPython kernels at the same time.
:samp:`display-name {DISPLAY_NAME}`
    specifies the display name for the kernelspec.

``ipython kernel install`` creates a ``kernelspec`` file in JSON format for the
current Python environment, for example:

.. code-block:: json

    {
     "argv": [
      "/srv/jupyter/.ipython/kernels/python311/.venv/bin/python",
      "-Xfrozen_modules=off",
      "-m",
      "ipykernel_launcher",
      "-f",
      "{connection_file}"
     ],
     "display_name": "project",
     "language": "python",
     "metadata": {
      "debugger": true
     },
     "env": {
      "VIRTUAL_ENV": "/srv/jupyter/.ipython/kernels/python311/.venv"
     }
    }

:samp:`argv`
    A list of command line arguments used to start the kernel.
    ``{connection_file}`` refers to a file that contains the IP address, ports,
    and authentication key required for the connection. Usually this JSON file
    is saved in a safe place of the current profile:
:samp:`display_name`
    The name of the kernel as it should be displayed in the browser. In contrast
    to the kernel name used in the API, it can contain any Unicode characters.
:samp:`language`
    The name of the language of the kernel. If no suitable ``kernelspec`` key is
    found when loading notebooks, a kernel with a suitable language is used. In
    this way, a notebook written for a Python or Julia kernel can be linked to
    the user’s Python or Julia kernel, even if it does not have the same name as
    the author’s.

    :samp:`{connection_file}` refers to a file containing the IP address, ports
    and authentication key needed for the connection. Typically, this JSON file
    is stored in a secure location of the current profile:

    .. code-block:: javascript

        {
          "shell_port": 61656,
          "iopub_port": 61657,
          "stdin_port": 61658,
          "control_port": 61659,
          "hb_port": 61660,
          "ip": "127.0.0.1",
          "key": "a0436f6c-1916-498b-8eb9-e81ab9368e84"
          "transport": "tcp",
          "signature_scheme": "hmac-sha256",
          "kernel_name": ""
        }

:samp:`interrupt_mode`
    can be either ``signal`` or ``message`` and specifies how a client should
    interrupt the execution of a cell on this kernel.

    ``signal``
        sends an interrupt, e.g. ``SIGINT`` on *POSIX* systems
    ``message``
        sends an ``interrupt_request``, see also `Kernel Interrupt
        <https://jupyter-client.readthedocs.io/en/latest/messaging.html#kernel-interrupt>`_.

:samp:`env`
    ``dict`` with environment variables to be set for the kernel. These are
    added to the current environment variables before the kernel starts.
:samp:`metadata`
    ``dict`` with additional attributes for this kernel. Used by clients to
    support the kernel selection. Metadata added here should have a namespace
    for the tool to read and write that metadata.

You can edit this ``kernelspec`` file at a later time.

Show available kernels
----------------------

.. code-block:: console

   $ uv run jupyter kernelspec list
   Available kernels:
     mykernel   /Users/veit/Library/Jupyter/kernels/mykernel
     python311  /Users/veit/Library/Jupyter/kernels/python311
     python313  /Users/veit/Library/Jupyter/kernels/python313

Start kernel
------------

.. code-block:: console

    $ uv run jupyter console --kernel mykernel
    Jupyter console 6.0.0
    Python 2.7.15 (default, Oct 22 2018, 19:33:46)
    ...

    In [1]:

With :kbd:`ctrl-d` you can exit the kernel again.

Delete kernel
-------------

.. code-block:: console

   $ uv run jupyter kernelspec uninstall mykernel

Uninstall the Standard kernel
-----------------------------

If not already done, a configuration file can be created, for example with

.. code-block:: console

   $ uv run jupyter lab --generate-config

Then you can add the following line to this configuration file:

.. code-block:: python

   c.KernelSpecManager.ensure_native_kernel = False
