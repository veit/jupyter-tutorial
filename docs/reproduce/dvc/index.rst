``DVC``
=======

`DVC <https://dvc.org/>`_ unterscheidet sich von anderen Werkzeugen zur
Versionskontrolle großer Daten wie z.B. `Git LFS <https://git-lfs.github.com/>`_
insbesondere durch die Unterstützung von Datenpipelines und
Abhängigkeitsgraphen.

.. seealso::
   * `Tutorial <https://dvc.org/doc/tutorial>`_
   * `Documentation <https://dvc.org/doc>`_
   * `Git Repository <https://github.com/iterative/dvc>`_

Installation
------------

DVC lässt sich mit Pipenv installieren. Beachtet dabei jedoch bitte, dass ihr
hierbei die Extras explizit angeben müsst. Dies können ``[ssh]``, ``[s3]``,
``[gs]``, ``[azure]``, und ``[oss]`` oder ``[all]`` sein. Für ``ssh`` sieht das
Kommando dann so aus:

.. code-block:: console

    $ pipenv install dvc[ssh]

Alternativ kann DVC auch über das Paketmanagement von Ubuntu/Debian installiert
werden mit:

.. code-block:: console

    $ sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list
    $ sudo apt update
    $ sudo apt install dvc

Für Mac OS X lässt sich DVC installieren mit:

.. code-block:: console

    $ brew install iterative/homebrew-dvc/dvc

.. toctree::
    :hidden:

    init
    integration
    pipeline
    reproduce
    metrics

