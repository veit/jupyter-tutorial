Kernel installieren
===================

Python 2 und 3
--------------

.. note::
    IPython 6.0 hat die Unterstützung für Python 2 eingestellt. Wenn ihr also
    IPython für Python 2 installieren wollt, verwendet eine ältere Version.

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

``ipykernel install`` kann u.a. mit folgenden Optionen aufgerufen werden:

``--user``
    installiert den Kernel für den aktuellen Nutzer und nicht systemweit
``name <NAME>``
    gibt einen Namen für die ``kernelspec`` an. Dieser wird benötigt, um
    mehrere IPython-Kernel gleichzeitig verwenden zu können, z.B.:

    .. code-block:: console

        $ pipenv run python -m ipykernel install --user --name myenv --display-name "MyPython"
        Installed kernelspec myenv in /Users/veit/Library/Jupyter/kernels/myenv

Mit ``ipykernel install`` wird eine ``kernelspec``-Datei im JSON-Format für die
aktuelle Python-Umgebung erstellt, z.B.:

.. code-block:: json

    {
     "display_name": "Python 2",
     "language": "python",
     "argv": [
      "/Users/veit/.local/share/virtualenvs/python2-EcWzFUEK/bin/python2",
      "-m",
      "ipykernel_launcher",
      "-f",
      "{connection_file}"
     ]
    }

``display_name``
    Der Name des Kernels, wie er im Browser angezeigt werden soll. Im Gegensatz
    zum in der API verwendeten Kernelnamen kann dieser beliebige Unicode-Zeichen
    enthalten.
``language``
    Der Name der Sprache des Kernels. Wenn beim Laden von Notebooks kein
    passender ``kernelspec``-Schlüssel gefunden wird, wird ein Kernel mit einer
    passenden Sprache verwendet. Auf diese Weise kann ein für ein Python- oder
    Julia-Kernel geschriebenes Notebook mit dem Python- oder Julia-Kernel des
    Benutzers verknüpft werden, auch wenn dieser nicht demselben Namen wie der
    des Autors hat.
``argv``
    Eine Liste von Befehlszeilenargumenten, die zum Starten des Kernels
    verwendet werden.

    ``{connection_file}`` verweist auf eine Datei, die die die IP-Adresse, die
    Ports und den Authentifizierungsschlüssel enthält, die für die Verbindung
    benötigt werden. Üblicherweise wird diese JSON-Datei an einem sicheren Ort
    des aktuellen Profile gespeichert:

    .. code-block:: json

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
    Kann entweder ``signal`` oder ``message`` sein und gibt an, wie ein Client
    die Ausführung einer Zelle auf diesem Kernel unterbrechen soll.

    ``signal``
        sendet ein Interrupt, z.B. ``SIGINT`` auf *POSIX*-Systemen
    ``message``
        sendet einen ``interrupt_request``, s.a. `Kernel Interrupt
        <https://jupyter-client.readthedocs.io/en/latest/messaging.html#kernel-interrupt>`_.

``env``
    ``dict`` mit Umgebungsvariablen, die für den Kernel festgelegt werden
    sollen. Diese werden zu den aktuellen Umgebungsvariablen hinzugefügt, bevor
    der Kernel gestartet wird.
``metadata``
    ``dict`` mit zusätzlichen Attributen zu diesem Kernel. Wird von Clients zur
    Unterstützung der Kernelauswahl verwendet. Hier hinzugefügte Metadaten
    sollten einen Namensraum für das Tool zum Lesen und Schreiben dieser
    Metadaten haben.

Ihr könnt diese ``kernelspec``-Datei zu einem späteren Zeitpunkt editieren, z.B.
um 

Verfügbare Kernel anzeigen
--------------------------

.. code-block:: console

    $ pipenv run jupyter kernelspec list
    Available kernels:
      python2    /Users/veit/Library/Jupyter/kernels/python2
      python3    /Users/veit/.local/share/virtualenvs/jupyter-tutorial--q5BvmfG/bin/../share/jupyter/kernels/python3

Kernel starten
--------------

.. code-block:: console

    $ pipenv run jupyter console --kernel python2
    Jupyter console 6.0.0
    Python 2.7.15 (default, Oct 22 2018, 19:33:46) 
    ...

    In [1]:

Mit ``ctrl`` + ``d`` könnt ihr den Kernel wieder beenden.

