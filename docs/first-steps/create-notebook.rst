Notebook erstellen
==================

Nachdem der Notebook-Server gestartet wurde, können wir unser erstes Notebook
erstellen.

Erstellen eines Notebooks
-------------------------

In eurem Standard-Browser solltet ihr das Notebook-Dashboard mit dem Menü *New*
auf der rechten Seite sehen. In diesem Menü werden alle Notebook-Kernel
aufgeführt, initial jedoch vermutlich nur *Python 3*.



Nachdem ihr :menuselection:`New --> Python 3` ausgewählt habt, wird ein neues
Notebook ``Untitled.ipynb`` erstellt und in einem neuen Reiter angezeigt:

.. image:: initial-notebook.png

Umbenennen des Notebooks
------------------------

Als nächstes solltet Ihr dieses Notebook umbenennen indem ihr auf den Titel
*Untitled* klickt:

.. image:: rename-notebook.png

Die Notebook-Oberfläche
-----------------------

Es gibt zwei wichtige Begriffe um Jupyter Notebooks zu beschreiben: *Cells* und
*Kernel*:

*Kernel*
    *Rechenmaschine*, die den in einem Notebook enthaltenen Code ausführt.
*Cell*
    Container für Text, der in einem Notebook angezeigt werden soll oder für
    Code, der vom Kernel des Notebooks ausgeführt werden soll.

    *Code*
        enthält Code, der im Kernel ausgeführt werden soll und dessen Ausgabe
        unterhalb angezeigt wird.
    *Markdown*
        enthält mit `Markdown
        <https://daringfireball.net/projects/markdown/syntax>`_ formatierten
        Text, der interpretiert wird sobald :menuselection:`Run` gedrückt wird.

Was ist eine ``ipynb``-Datei?
------------------------------

Diese Datei beschreibt ein Notebook im `JSON
<https://de.wikipedia.org/wiki/JavaScript_Object_Notation>`_-Format. Jede Zelle
und ihr Inhalt einschließlich Bildern werden dort zusammen mit einigen Metadaten
aufgelistet. Ihr könnt euch diese anschauen wenn ihr im Dashboard das Notebook
auswählt und dann auf :menuselection:`edit` klickt. So sieht z.B. die JSON-Datei
für `my-first-notebook.ipynb <my-first-notebook.ipynb>`_ folgendermaßen aus:

.. code-block:: json

    {
     "cells": [
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "# My first notebook"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": 1,
       "metadata": {},
       "outputs": [
        {
         "name": "stdout",
         "output_type": "stream",
         "text": [
          "Hello World!\n"
         ]
        }
       ],
       "source": [
        "print('Hello World!')"
       ]
      }
     ],
     "metadata": {
      "kernelspec": {
       "display_name": "Python 3",
       "language": "python",
       "name": "python3"
      },
      "language_info": {
       "codemirror_mode": {
        "name": "ipython",
        "version": 3
       },
       "file_extension": ".py",
       "mimetype": "text/x-python",
       "name": "python",
       "nbconvert_exporter": "python",
       "pygments_lexer": "ipython3",
       "version": "3.7.0"
      }
     },
     "nbformat": 4,
     "nbformat_minor": 2
    }

