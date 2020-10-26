Spack mirrors
=============

Some machines may not have internet access to get packages. Then you will need a
local repository of tarballs from which to retrieve your files. Spack supports
this with :doc:`mirrors`. A mirror is a URL that points to a directory on the
local file system or on a server and contains tarballs for all Spack packages.

Here is an example of the directory structure of a mirror:

.. code-block:: console

    $ tree /path/to/mirror/
    /path/to/mirror/
    ├── autoconf
    │   └── autoconf-2.69.tar.gz
    ├── automake
    │   └── automake-1.16.1.tar.gz
    ├── bzip2
    │   └── bzip2-1.0.8.tar.gz
    ├── diffutils
    │   └── diffutils-3.7.tar.xz
    ├── expat
    │   └── expat-2.2.5.tar.bz2
    ├── gcc
    │   └── gcc-9.1.0.tar.xz
    …

``spack mirror create``
-----------------------

You can create a mirror with the command ``spack mirror create``, provided you
are on a machine that can access the Internet. The command iterates through all
of Spack’s packages and downloads the ones you want.

``spack mirror add``
--------------------

Once you’ve created a mirror, you need to let Spack know about it. It’s
relatively easy. First find out the URL of your mirror. If it’s a directory, you
can use a file url like this:

.. code-block:: console

    $ spack mirror add local_filesystem file://$HOME/spack-mirror

Order of mirrors
----------------

``spack mirror ad`` adds a line in ``~/.spack/mirrors.yaml``:

.. code-block:: yaml

    mirrors:
      local_filesystem: file:///home/veit/spack-mirror
      remote_server: https://spack-mirror.cusy.io

If you want to change the order in which mirrors are searched for packages, you
can edit this file and rearrange the sections: Spack searches them from top to
bottom until a suitable entry is found.

Local default cache
-------------------

Spack creates a cache for resources that are downloaded as part of
installations. This cache is a valid Spack mirror: it uses the same directory
structure and naming scheme as other Spack mirrors. The mirror is managed
locally in the Spack installation directory at ``~/spack/var/spack/cache/``.
