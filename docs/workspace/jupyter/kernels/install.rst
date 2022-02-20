Install, view and start the kernel
==================================

Install a kernel
----------------

``pipenv run python -m ipykernel install`` can be called with the following
options:

``--user``
    installs the kernel for the current user and not system-wide
``name <NAME>``
    gives a name for the ``kernelspec``. This is required in order to be able to
    use several IPython kernels at the same time, e.g.:

    .. code-block:: console

        $ cd /path/to/your/jupyter/
        $ pipenv run python -m ipykernel install --user --name mykernel --display-name "My Kernel"
        Installed kernelspec mykernel in /Users/veit/Library/Jupyter/kernels/mykernel

``ipykernel install`` creates a ``kernelspec`` file in JSON format for the
current Python environment, e.g.:

.. code-block:: json

    {
     "display_name": "My Kernel",
     "language": "python"
     "argv": [
      "/Users/veit/.local/share/virtualenvs/mykernel-7y9G693U/bin/python",
      "-m",
      "ipykernel_launcher",
      "-f",
      "{connection_file}"
     ],
    }

``display_name``
    The name of the kernel as it should be displayed in the browser. In contrast
    to the kernel name used in the API, it can contain any Unicode characters.
``language``
    The name of the language of the kernel. If no suitable ``kernelspec`` key is
    found when loading notebooks, a kernel with a suitable language is used. In
    this way, a notebook written for a Python or Julia kernel can be linked to
    the user's Python or Julia kernel, even if it does not have the same name as
    the author’s.
``argv``
    A list of command line arguments used to start the kernel.
    ``{connection_file}`` refers to a file that contains the IP address, ports,
    and authentication key required for the connection. Usually this JSON file
    is saved in a safe place of the current profile:

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

``interrupt_mode``
    can be either ``signal`` or ``message`` and specifies how a client should
    interrupt the execution of a cell on this kernel.

    ``signal``
        sends an interrupt, e.g. ``SIGINT`` on *POSIX* systems
    ``message``
        sends an ``interrupt_request``, see also `Kernel Interrupt
        <https://jupyter-client.readthedocs.io/en/latest/messaging.html#kernel-interrupt>`_.

``env``
    ``dict`` with environment variables to be set for the kernel. These are
    added to the current environment variables before the kernel starts.
``metadata``
    ``dict`` with additional attributes for this kernel. Used by clients to
    support the kernel selection. Metadata added here should have a namespace
    for the tool to read and write that metadata.

You can edit this ``kernelspec`` file at a later time.

Show available kernels
----------------------

.. code-block:: console

    $ pipenv run jupyter kernelspec list
    Available kernels:
      mykernel    /Users/veit/Library/Jupyter/kernels/mykernel
      python2    /Users/veit/Library/Jupyter/kernels/python2
      python3    /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/../share/jupyter/kernels/python3

Start kernel
------------

.. code-block:: console

    $ pipenv run jupyter console --kernel mykernel
    Jupyter console 6.0.0
    Python 2.7.15 (default, Oct 22 2018, 19:33:46)
    ...

    In [1]:

With ``ctrl`` + ``d`` you can exit the kernel again.
