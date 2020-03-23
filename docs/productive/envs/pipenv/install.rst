Installation
============

Dieser Abschnitt behandelt die Grundlagen zur Installation von
:term:`Python-Paketen <Distribution Package>`.

Voraussetzungen für die Installation von Paketen
------------------------------------------------

Vor der Installation von Python-Paketen müssen einige Voraussetzungen erfüllt
sein. 

#. Stellt sicher, dass ihr die gewünschte Python-Version verwendet:

   .. code-block:: console

    $ python --version
    Python 3.6.3

   .. note::
        In iPython oder einem Jupyter Notebook könnt ihr die Version
        folgendermaßen herausbekommen:

        .. code-block:: ipython

            In [1]: import sys
                    !{sys.executable} --version
            Python 3.6.3

   .. note::
        Falls ihr das System-Python eurer Linux-Distribution verwendet, solltet
        ihr zunächst eine virtuelle Umgebung mit Python 3 und :term:`Pip <pip>`
        erstellen.

#. Stellt sicher, dass :term:`Pip <pip>` installiert ist:

   .. code-block:: console

    $ pip --version
    pip 10.0.1

   #. Falls Pip noch nicht installiert ist, könnt ihr es installieren (lassen)

      * für Python 2 mit:

        .. code-block:: console

            $ sudo apt install python-pip

      * für Python 3 mit:

        .. code-block:: console

            $ sudo apt install python3-venv python3-pip

Pipenv installieren
-------------------

:term:`pipenv` ist ein Abhängigkeitsmanager für Python-Projekte. Er nutzt
:term:`Pip` zum Installieren von Python-Paketen, er vereinfacht jedoch die
Verwaltung von Abhängigkeiten. Pip kann zum Installieren von Pipenv verwendet
werden, es sollte jedoch das ``--user``-Flag verwendet werden, damit es nur
für diesen Nutzer bereitsteht. Dadurch soll verhindert werden, dass
versehentlich systemweite Pakete überschrieben werden:

.. code-block:: console

    $ python3 -m pip install --user pipenv
      Downloading pipenv-2018.7.1-py3-none-any.whl (5.0MB): 5.0MB downloaded
    Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/lib/python3/dist-packages (from pipenv)
    Installing collected packages: pipenv, certifi, pip, setuptools, virtualenv-clone
    …
    Successfully installed pipenv certifi pip setuptools virtualenv-clone
    Cleaning up...

.. note::
    
   Wenn pipenv nach der Installation nicht in der Shell verfügbar ist, muss
   ggf. das ``USER_BASE/bin``-Verzeichnis in ``PATH`` angegeben werden. 

   * Unter Linux und MacOS lässt sich ``USER_BASE`` ermitteln mit::

        $ python3 -m site --user-base
        /Users/veit/.local

     Anschließend muss noch das ``bin``-Verzeichnis angehängt und zu ``PATH``
     hinzugefügt werden. Alternativ kann ``PATH`` dauerhaft gesetzt werden, indem
     ``~/.profile`` oder ``~/.bash_profile`` geändert werden, in meinem Fall also::

        export PATH=/Users/veit/.local/bin:$PATH

   * Unter Windows kann das Verzeichnis ermittelt werden mit
     ``py -m site --user-site`` und anschließend ``site-packages`` durch
     ``Scripts`` ersetzt werden. Dies ergibt dann z.B.:

     .. code-block:: console

        C:\Users\veit\AppData\Roaming\Python36\Scripts

     Um dauerhaft zur Verfügung zu stehen, kann dieser Pfad unter ``PATH``
     im Control Panel eingetragen werden.

Weitere Informationen zur nutzerspezifischen Installation findet ihr in `User
Installs <https://pip.readthedocs.io/en/latest/user_guide.html#user-installs>`_.

Virtuelle Umgebungen erstellen
------------------------------

:term:`Virtuelle Python-Umgebungen <Virtuelle Umgebung>` ermöglichen die
Installation von Python-Paketen an einem isolierten Ort für eine bestimmte
Anwendung, anstatt sie global zu installieren. Ihr habt also eure eigenen
Installationsverzeichnisse und teilt keine Bibliotheken mit anderen
virtuellen Umgebungen:

.. code-block:: console

    $ mkdir myproject
    $ cd !$
    cd myproject
    $ pipenv install requests
    Creating a virtualenv for this project..
    …
    Virtualenv location: /Users/veit/.local/share/virtualenvs/myproject-9TTuTZjx
    Creating a Pipfile for this project...
    Installing requests...
    …

