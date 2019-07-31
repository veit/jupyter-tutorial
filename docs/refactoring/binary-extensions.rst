Binary Extensions
=================

Eine der Funktionen des CPython-Interpreters besteht darin, dass neben der
Ausführung von Python-Code auch eine reichhaltige C-API für die Verwendung
durch andere Software verfügbar ist. Eine der häufigsten Anwendungen dieser
C-API besteht darin, importierbare C-Erweiterungen zu erstellen, die Dinge
ermöglichen, die im reinen Python-Code nur schwer zu erreichen sind.

Use Cases
---------

Die typischen Anwendungsfälle für Binary Extensions lassen sich in drei
Kategorien unterteilen:

Accelerator-Module
    Diese Module sind eigenständig und werden nur erstellt, um schneller zu
    laufen als der entsprechende reine Python-Code. Im Idealfall haben die
    Beschleunigermodule immer ein Python-Äquivalent, das als Fallback verwendet
    werden kann, wenn die beschleunigte Version auf einem bestimmten System
    nicht verfügbar ist.

    Die CPython-Standardbibliothek verwendet viele Beschleunigermodule.

Wrapper-Module
    Diese Module werden erstellt, um vorhandene C-Interfaces in Python verfügbar
    zu machen. Sie können entweder die zugrunde liegenden C-Interfaces direkt
    verfügbar oder eine *Pythonic*-API bereitgestellt werden, die
    Features von Python verwendet, um die API einfacher zu verwenden.

    Die CPython-Standardbibliothek verwendet umfangreiche Wrapper-Module.

Systemzugriffe auf niedriger Ebene
    Diese Module werden erstellt, um auf Funktionen der
    CPython-Laufzeitumgebung, des Betriebssystems oder der
    zugrundeliegenden Hardware zuzugreifen. Durch plattformspezifischen Code
    können mit solchen Erweiterungsmodulen Dinge erreicht werden, die mit reinem
    Python-Code nicht möglich wären.

    Eine Reihe von CPython-Standard-Bibliotheksmodulen sind in C geschrieben, um
    auf Interpreter-Interna zuzugreifen, die nicht auf der Sprachebene verfügbar
    sind.

    Eine besonders bemerkenswerte Eigenschaft von C-Erweiterungen ist, dass sie,
    den Global Interpreter Lock (GIL) von CPython bei lang andauernden
    Operationen freigeben können, unabhängig davon, ob diese Operationen CPU-
    oder IO-gebunden sind.

Nicht alle Erweiterungsmodule passen genau in die oben genannten Kategorien. So
umfassen z.B. die in `NumPy <http://www.numpy.org/>`_ enthaltenen
Erweiterungsmodule alle drei Anwendungsfälle: 

* Sie verschieben innere Schleifen aus Geschwindigkeitsgründen auf C,
* umschließen externe Bibliotheken in C, FORTRAN und anderen Sprachen und
* verwenden Systemschnittstellen auf niedriger Ebene für CPython und das
  zugrunde liegende Betriebssystem, um die gleichzeitige Ausführung von
  vektorisierten Operationen zu unterstützen und das Speicherlayout von
  erstellten Objekten genau zu steuern.

Nachteile
---------

Früher war Der Hauptnachteil bei der Verwendung von Binary Extensions, dass
dadurch die Distribution der Software erschwert wurde. Heute ist dieser Nachteil
durch :term:`wheel` kaum noch vorhanden. Einige Nachteile bleiben dennoch:

* Die Installation aus den Sourcen bleibt weiterhin kompiziert.
* Ggf. gibt es kein passendes :term:`wheel` für den verwendeten Build des
  CPython-Interpreters oder alternativen Interpretern wie `PyPy
  <https://pypy.org/>`_, `IronPython <http://ironpython.net/>`_ oder `Jython
  <http://www.jython.org/>`_.
* Die Wartung und Pflege der Pakete ist aufwändiger da die Maintainer nicht nur
  mit Python sondern auch mit einer anderen Sprache und der CPython C-API
  vertraut sein müssen. Zudem erhöht sich die Komplexität, wenn neben der
  Binary Extension auch eine Python-Fallback-Implementierung bereitgestellt
  wird.
* Schließlich funktioniern häufig auch Importmechanismen, wie der direkte
  Import aus ZIP-Dateien, nicht für Extensions-Module.

Alternativen
------------



… zu Accelerator-Modulen
~~~~~~~~~~~~~~~~~~~~~~~~

Wenn Extensions-Module nur verwendet werden, um Code schneller auszuführen,
sollten auch eine Reihe anderer Alternativen in Betracht gezogen werden:

* Sucht nach vorhandenen optimierten Alternativen. Die CPython-Standardbibliothek
  enthält eine Reihe optimierter Datenstrukturen und Algorithmen, insbesondere in
  den builtins und den Modulen ``collections`` und ``itertools``.

  Gelegentlich bietet auch der :term:`Python Package Index (PyPI)` zusätzliche
  Alternativen. Manchmal kann ein Modul eines Drittanbieters die Notwendigkeit
  vermeiden, ein eigenes Accelerator-Modul zu erstellen.

* Für lange laufende Anwendungen kann der JIT-kompilierte `PyPy
  <https://pypi.python.org/>`_-Interpreter eine geeignete Alternative zum
  Standard-CPython sein. Die Hauptschwierigkeit bei der Übernahme von PyPy
  besteht typischerweise in der Abhängigkeit von anderen Binary
  Extensions-Modulen. Während PyPy die CPython C API emuliert, verursachen
  Module, die darauf angewiesen sind, Probleme für das PyPy JIT, und die
  Emulation legt oft Defekte in Extensions-Modulen offen, die CPython
  toleriert. (häufig bei Reference Counting Errors).

* `Cython <http://cython.org/>`_ ist ein ausgereifter statischer Compiler, der
  den meisten Python-Code zu C-Extensions-Modulen kompilieren kann. Die
  anfängliche Kompilierung bietet einige Geschwindigkeitssteigerungen (durch
  Umgehung der CPython-Interpreter-Ebene), und Cythons optionale statische
  Typisierungsfunktionen können zusätzliche Möglichkeiten für
  Geschwindigkeitssteigerungen bieten. Für Python-Programmierer bietet Cython
  eine niedrigere Eintrittshürde relativ zu anderen Sprachen wie C oder C ++).


  Die Verwendung von Cython hat jedoch den Nachteil, die Komplexität der
  Verteilung der resultierenden Anwendung zu erhöhen.

* `Numba <http://numba.pydata.org/>`_ ist ein neueres Tool, das die `LLVM
  Compiler-Infrastruktur <https://llvm.org/>`_ nutzt, um während der Laufzeit
  selektiv Teile einer Python-Anwendung auf nativen Maschinencode zu
  kompilieren. Es erfordert, dass LLVM auf dem System verfügbar ist, auf dem der
  Code ausgeführt wird. Es kann, insbesondere bei vektorisierbaren Vorgängen
  zu erheblichen Geschwindigkeitssteigerungen führen.

… zu Wrapper-Modulen
~~~~~~~~~~~~~~~~~~~~

Die C-ABI (`Application Binary Interface
<https://de.wikipedia.org/wiki/Bin%C3%A4rschnittstelle>`_) ist ein Standard für
die gemeinsame Nutzung von Funktionen zwischen mehreren Anwendungen. Eine der
Stärken der CPython C-API (`Application Programming Interface
<https://de.wikipedia.org/wiki/Programmierschnittstelle>`_) ist es, dass
Python-Benutzer diese Funktionalität nutzen können. Das manuelle Wrapping von
Modulen ist jedoch sehr mühsam, so dass eine Reihe anderer Alternativen in
Betracht gezogen werden sollten.

Die unten beschriebenen Ansätze vereinfachen nicht die Distribution, aber sie
können den Wartungsaufwand im Vergleich zu Wrapper-Modulen deutlich reduzieren.

* `Cython <http://cython.org/>`_ eignet sich nicht nur zum Erstellen von
  Accelerator-Modulen, sondern auch zum Erstellen von Wrapper-Modulen. Da das
  Wrapping der API immer noch von Hand erfolgen muss, ist es keine gute Wahl beim
  Wrapping großer APIs.

* `cffi <https://cffi.readthedocs.io/>`_ ist das Projekt einiger `PyPy
  <https://pypy.org/>`_-Entwickler, um Entwicklern, die sowohl Python als auch C
  bereits kennen, die Möglichkeit zu geben, ihre C-Module für Python-Anwendungen
  verfügbar zu machen. Es macht das Wrapping eines C-Moduls basierend auf seinen
  Header-Dateien relativ einfach, auch wenn man sich mit C selbst nicht auskennt.

  Einer der Hauptvorteile von cffi besteht darin, dass es mit dem PyPy-JIT
  kompatibel ist, sodass CFFI-Wrapper-Module vollständig von den
  PyPy-Tracing-JIT-Optimierungen partizipieren können.

* `SWIG <http://www.swig.org/>`_ ist ein Wrapper Interface Generator, der eine
  Vielzahl von Programmiersprachen, einschließlich Python, mit C- und C++-Code
  verbindet.

* Das ``ctypes``-Modul der Standardbibliothek ist zwar nützlich um Zugriff auf
  C-Schnittstellen zu erhalten, wenn die Header-Informationen jedoch nicht
  verfügbar sind, es leidet jedoch daran, dass es nur auf der C ABI-Ebene
  arbeitet und somit keine automatische Konsistenzprüfung zwischen der
  exportierten Schnittstelle und dem Python-Code macht. Im Gegensatz dazu
  können die obigen Alternativen alle auf der C-API arbeiten und
  C-Header-Dateien verwenden, um die Konsistenz zu gewährleisten.

… für den Systemzugriff auf niedriger Ebene
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Für Anwendungen, die Low Level System Access benötigen, ist eine Binary
Extension oft ist der beste Weg. Dies gilt insbesondere für den Low Level Access
auf die CPython-Runtime, da einige Operationen (wie das Freigeben des Global
Interpreter Lock (GIL) nicht zulässig sind, wenn der Interpreter den Code
selbst ausführt, gerade auch wenn Module wie ``ctypes`` oder ``cffi`` verwendet
werden, um Zugriff auf das relevanten C-API-Interfaces zu erhalten.

In Fällen, in denen das Erweiterungsmodul das zugrunde liegende Betriebssystem
oder die Hardware (statt der CPython-Runtime) manipuliert, ist es manchmal
besser, eine normale C-Bibliothek (oder eine Bibliothek in einer anderen
Programmiersprache wie C ++ oder Rust) zu schreiben, die eine C-kompatible ABI),
bereitstewllt und vnschließend eine der oben beschriebenen Wrapping-Techniken zu
erwenden um das Interface als importierbares Python-Modul verfügbar zu machen.

Implementierung
---------------

Der `CPython Extending and Embedding guide
<https://docs.python.org/3/extending/>`_ enthält eine Einführung in das
Schreiben eigener Extension-Module in C: `Extending Python with C or C++
<https://docs.python.org/3/extending/extending.html>`_. Beachtet jedoch bitte,
dass diese Einführung nur  die grundlegenden Tools zum Erstellen von
Erweiterungen beshreibt, die im Rahmen von CPython bereitgestellt werden.
Third-Party-Tools wie `Cython <http://cython.org/>`_, `cffi
<https://cffi.readthedocs.io/>`_, `SWIG <http://www.swig.org/>`_ und `Numba
<https://numba.pydata.org/>`_ bieten sowohl einfachere als auch ausgeklügeltere
Ansätze zum Erstellen von C- und C ++ - Erweiterungen für Python.

.. seealso::
    `Python Packaging User Guide: Binary Extensions
    <https://packaging.python.org/guides/packaging-binary-extensions/>`_
    behandelt nicht nur verschiedene verfügbare Tools, die die Erstellung von
    Binary Extensions vereinfachen, sondern erläutert auch die verschiedenen
    Gründe, warum das Erstellen eines Extension Module wünschenswert sein
    könnte.

Erstellen von Binary Extensions
-------------------------------

Binary Extensions für Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bevor ihr eine Binary Extension erstellen könnt, müsst ihr sicherstellen, dass
ihr einen geeigneten Compiler zur Verfügung habt. Unter Windows wird Visual C
zum Erstellen des offiziellen CPython-Interpreters verwendet und er sollte auch
zum Erstellen kompatibler Binary Extensions verwendet werden:

für Python 2.7
    #. installiert `Microsoft Visual C++ Compiler for Python 2.7
       <https://www.microsoft.com/en-gb/download/details.aspx?id=44266>`_
    #. aktualisiert :term:`pip` und :term:`setuptools`
für Python 3.4
    #. installiert `Microsoft Windows SDK for Windows 7 and .NET Framework 4
       <https://www.microsoft.com/en-gb/download/details.aspx?id=8279>`_
    #. arbeitet mit dem SDK-Command-Prompt (mit den Umgebungsvariablen und dem
       SDK in ``PATH``).
    #. setzt ``DISTUTILS_USE_SDK=1``.
für Python 3.5+
    #. installiert `Visual Studio Code <https://code.visualstudio.com/>`_ mit
       `Python Extension
       <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_

    .. note::
        Visual Studio arbeitet ab Python 3.5 abwärtskompatibel, d.h., dass jede
        zukünftige Version von Visual Studio Python-Erweiterungen für alle
        Python-Versionen ab Version 3.5 erstellen kann.

Das Erstellen mit dem empfohlenen Compiler unter Windows stellt sicher, dass
eine kompatible C-Bibliothek im gesamten Python-Prozess verwendet wird.

Binary Extensions für Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux-Binaries müssen eine ausreichend alte glibc verwenden, um mit älteren
Distributionen kompatibel zu sein. `Distrowatch <https://distrowatch.com/>`_
bereitet in tabellarischer Form auf, welche Versionen der Distributionen welche
Bibliothek liefern:

* `Red Hat Enterprise Linux <https://distrowatch.com/table.php?distribution=redhat>`_
* `Debian <https://distrowatch.com/table.php?distribution=debian>`_
* `Ubuntu <https://distrowatch.com/table.php?distribution=ubuntu>`_
* …

Das `PYPA/Manylinux <https://github.com/pypa/manylinux>`_-Projekt erleichtert
die Distribution von Binarxy Extensions als :term:`Wheels <wheel>` für die
meisten Linux-Plattformen. Hieraus ging auch `PEP 513
<https://www.python.org/dev/peps/pep-0513/>`_ hervor, das die
``manylinux1_x86_64``- und ``manylinux1_i686``-Plattform-Tags definiert.

Binary Extensions für Mac
~~~~~~~~~~~~~~~~~~~~~~~~~

Die Binärkompatibilität auf macOS wird durch das Zielsystem für die minimale
Implementierung bestimmt, z. B. *10.9* , das in der Umgebungsvariable
``MACOSX_DEPLOYMENT_TARGET`` definiert wird. Beim Erstellen mit
setuptools/distutils wird das Deployment-Ziel mit dem Flag ``--plat-name``
angegeben, z.B. ``macosx-10.9-x86_64``. Weitere Informationen zu
Deployment-Zielen für Mac OS Python-Distributionen findet ihr im `MacPython
Spinning Wheels-Wiki <https://github.com/MacPython/wiki/wiki/Spinning-wheels>`_.

Deployment von Binary Extensions
--------------------------------

Im Folgenden soll das Deployment auf dem :term:`Python Package Index (PyPI)`
oder einem anderen Index beschrieben werden.

.. note::
   Bei Deployments auf Linux-Distributionen sollte beachtet werden, dass diese
   Anforderungen an das spezifische Build-System stellen. Daher sollten neben
   :term:`Wheels <wheel>` immar auch :term:`Source Distributions (sdist)
   <Source Distribution (sdist)>` bereitgestellt werden.

.. todo::
   `enscons <https://pypi.python.org/pypi/enscons/>`_ als Alternative zu
   ``distutils`` oder ``setuptools`` evaluieren. 

   Ein Vorteil scheint zu sein, dass ihr mit `Scons <http://scons.org/>`_ ein
   vollwertiges Build-System erhaltet, das euch Arbeit abnimmt beim Ermitteln
   der möglichen Build-Varianten.

.. seealso::
   * `Deploying Python applications
     <https://packaging.python.org/discussions/deploying-python-applications/>`_
   * `Supporting Windows using Appveyor
     <https://packaging.python.org/guides/supporting-windows-using-appveyor/>`_

