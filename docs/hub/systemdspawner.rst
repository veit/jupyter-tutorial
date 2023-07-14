systemdspawner
==============

The systemdspawner allows JupyterHub to create single user notebook servers with
`systemd <https://en.wikipedia.org/wiki/Systemd>`_. You get isolation and
security without having to use Docker, rkt or similar. In addition,
systemdspawner offers other features:

* the maximum allowed memory and CPU per person can be limited via cgroups and
  checked with ``systemd-cgtop``.
* all get their own `/tmp` directory to increase isolation
* notebook servers can be started as specific local users on the system
* the use of sudo in notebooks can be restricted
* the paths that can be read and written to can be restricted
* logs for each notebook can be managed

Requirements
------------

systemdspawner requires systemd ≥ v211; the security-related functions require
systemd ≥ v228. You can check which version of systemd is available on your
system with

.. code-block:: console

   $ systemctl --version | head -1
   systemd 249 (249.11-0ubuntu3.7)

To limit memory and CPU allocations, certain kernel options must also be
available. This can be checked with `check-kernel.bash
<https://github.com/jupyterhub/systemdspawner/blob/main/check-kernel.bash>`_.

If the default setting :samp:`c.SystemdSpawner.dynamic_users = False` is used,
the server is started with the local Unix user account. Therefore, this spawner
requires that all users, already have a local account on the machine. With
:samp:`c.SystemdSpawner.dynamic_users = True`, on the other hand, no local user
accounts are required; they are dynamically created by systemd as needed.

Installation and Configuration
------------------------------

You can install systemdspawner with

.. code-block:: console

   $ pipenv install jupyterhub-systemdspawner

Then you can activate it in :file:`jupyterhub_config.py` with

.. code-block:: python

   c.JupyterHub.spawner_class = 'systemdspawner.SystemdSpawner'

There are many other configuration options open to you, for example

:samp:`c.SystemdSpawner.mem_limit = '4G'`
    specifies the maximum amount of memory that can be used by each user. The
    ``None`` setting disables the memory limit.

    Although individual users should be able to use as much memory as possible,
    it is still useful to set a memory limit of 80–90% of the total physical
    memory. This prevents one user from accidentally crippling the machine
    single-handedly.

:samp:`c.SystemdSpawner.cpu_limit = 4.0`
    A floating point number that specifies the number of CPU cores that each
    user can use.
:samp:`c.SystemdSpawner.user_workingdir = '/home/{USERNAME}'`
    The directory where each user’s notebook server is started. This directory
    is also what users see when they open their notebook servers. Normally this
    is the user’s home directory.
:samp:`c.SystemdSpawner.username_template = 'jupyter-{USERNAME}'`
    Template for the Unix user name under which each user should be created.
:samp:`c.SystemdSpawner.default_shell = '/bin/bash'`
    The default shell used for the terminal in the notebook. Sets the
    environment variable ``SHELL`` to this value.
:samp:`c.SystemdSpawner.extra_paths = ['/home/{USERNAME}/conda/bin']`
    List of paths to prepend to the ``PATH`` environment variable for the
    spawned notebook server. This is easier than setting the ``env`` property
    because you want to add ``PATH`` and not replace it completely. This is very
    useful if you want to include a virtualenv or conda installation in the
    user’s ``PATH`` by default.
:samp:`c.SystemdSpawner.unit_name_template = 'jupyter-{USERNAME}-singleuser'`
    Systemd service unit name template for each user notebook server. This
    allows differentiation between multiple JupyterHubs with systemd spawners on
    the same machine. Should only contain ``[a-zA-Z0-9_-]``.
:samp:`c.SystemdSpawner.unit_extra_properties = {'LimitNOFILE': '16384'}`
    Dict of key-value pairs used to add arbitrary properties to spawned
    JupyerHub units – see also ``man systemd-run`` for details on properties.
:samp:`c.SystemdSpawner.isolate_tmp = True`
    Setting this to ``True`` will create a separate, private :file:`/tmp`
    directory for each user. This is very useful to protect against accidental
    leakage of otherwise private information.

    This requires systemd version > 227. If you enable this in earlier versions,
    spawning will fail.

:samp:`c.SystemdSpawner.isolate_devices = True`
    If you set this option to ``True``, a separate, private :file:`/dev`
    directory will be created for each user. This prevents users from accessing
    hardware devices directly, which could be a potential source of security
    problems. ``/dev/null``, ``/dev/zero``, ``/dev/random`` and the ``ttyp``
    pseudo devices are already mounted, so most users should not notice any
    change if this is enabled.

:samp:`c.SystemdSpawner.disable_user_sudo = True`
    Setting this option to ``True`` will prevent users from being able to use
    sudo or other means to become other users. This helps limit the damage done
    by compromising a user’s credentials if they also have sudo privileges on
    the machine – a web-based exploit can now only damage the user’s own data.

    This requires systemd version > 228. If you enable this in earlier versions,
    spawning will fail.

:samp:`c.SystemdSpawner.readonly_paths = ['/']`
    List of file system paths to be mounted read-only for the user’s notebook
    server. This overrides any existing file system permissions. Subpaths of
    paths that are mounted readonly can be marked as readwrite with
    ``readwrite_paths``. This is useful for marking ``/`` as read-only and
    listing only those paths to which notebook users are allowed to write. If
    the paths listed here do not exist, you will get an error message.

    This requires systemd version > 228. If you enable this feature in earlier
    versions, spawning will fail. Up to systemd version 231 it can also only
    contain directories and no files.

:samp:`c.SystemdSpawner.readwrite_paths = ['/home/{USERNAME}']`
    List of file system paths to be mounted read-only for the user’s notebook
    server. This only makes sense if ``readonly_paths`` is used to make some
    paths read-only. This does not override the file system permissions – the
    user must have the appropriate permissions to write to these paths.

    This requires systemd version > 228. If you enable this feature in earlier
    versions, spawning will fail. Up to systemd version 231, it can also only
    contain directories and not files.

.. seealso::
   * `systemdspawner <https://github.com/jupyterhub/systemdspawner>`_
