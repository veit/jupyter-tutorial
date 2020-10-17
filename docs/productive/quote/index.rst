Zitieren
========

Heute ist Software ein integraler Bestandteil wissenschaftlicher Forschung. Mit
ihr werden Forschungsdaten erstellt, verarbeitet und analysiert sowie komplexe
Prozesse modelliert und simuliert. Trotz ihrer zunehmenden Bedeutung in der
Forschung ist kaum bekannt, wie sie in die wissenschaftlichen Anerkennungs-
und Reputationssysteme eingebettet werden können.
Eine wesentliche Möglichkeit in diesen Systemen sind Zitate, wobei jedoch nur
wenige Forscher*innen wissen, wie Software zitiert werden könnte. James Howison
und Julia Bullard führten in ihrem 2016 veröffentlichten Artikel `Software in
the scientific literature <https://doi.org/10.1002/asi.23538>`_ folgende
Beispiele in absteigender Reputation auf:

#. zitieren von Veröffentlichungen, die die jeweilige Software beschreiben
#. zitieren von Bedienungsanleitungen
#. zitieren der Software-Projekt-Website
#. Link auf eine Software-Projekt-Website
#. erwähnen des Software-Namens

Die Situation bleibt dennoch unbefriedigend für die Autor*innen von Software,
zumal wenn sie sich von den Autor*innen der Software-Beschreibung unterscheiden.
Umgekehrt ist Forschungssoftware leider auch nicht immer gut geeignet um zitiert
zu werden. So werden Kollegen Eure Software kaum direkt zitieren können, wenn Ihr
ihnen die Software als Anhang von E-Mails schickt. Auch ein Download-Link ist
hier noch nicht wirklich zielführend. Aber wie können Autor*innen ihre Software
zitierfähig bereitstellen?

Die `FORCE11 <https://www.force11.org/group/software-citation-working-group>`_
-Arbeitsgruppe hat ein Paper veröffentlicht, in denen Prinzipien des
wissenschaftlichen Software-zitierens dargelegt werden: Arfon Smith, Daniel
Katz, Kyle Niemeyer: `FORCE11 Software Citation Working Group
<https://doi.org/10.7717/peerj-cs.86>`_, 2016. Dabei kristallisieren sich
aktuell zwei Projekte für strukturierte Metadaten heraus:

`CodeMeta <https://codemeta.github.io/>`_
    Austauschschema für allgemeine Software-Metadaten und
    Referenzimplementierung für JSON for Linking Data (`JSON-LD
    <https://json-ld.org/>`_).

    Dabei wird eine ``codemeta.json``-Datei im Stammverzeichnis des
    Software-Repository erwartet. Die Datei kann z.B. so aussehen:

    .. code-block:: javascript

        {
            "@context": "https://doi.org/10.5063/schema/codemeta-2.0",
            "@type": "SoftwareSourceCode",
            "author": [{
                "@type": "Person",
                "givenName": "Stephan",
                "familyName": "Druskat",
                "@id": "http://orcid.org/0000-0003-4925-7248"
            }],
            "name": "My Research Tool",
            "softwareVersion": "2.0",
            "identifier": "https://doi.org/10.5281/zenodo.1234",
            "datePublished": "2017-12-18",
            "codeRepository": "https://github.com/research-software/my-research-tool"
        }

    .. seealso::
        * `CodeMeta generator <https://codemeta.github.io/codemeta-generator/>`_
        * `Codemeta Terms <https://codemeta.github.io/terms/>`_
        * `GitHub Repository
          <https://github.com/codemeta/codemeta-generator/>`_

`Citation File Format <https://citation-file-format.github.io/>`_
    Schema für Software-Citation-Metadaten in maschinenlesbarem `YAML
    <https://yaml.org/>`-Format

    Dabei sollte eine Datei ``CITATION.cff`` im Stammverzeichnis des
    Software-Repository abegelgt werden.

    Der Inhalt der Datei kann z.B. so aussehen:

    .. code-block::

        # YAML 1.2
        ---
        cff-version: 1.1.0
        message: If you use this software, please cite it as below.
        authors:
          - family-names: Druskat
            given-names: Stephan
            orcid: https://orcid.org/0000-0003-4925-7248
        title: "My Research Software"
        version: 2.0.4
        doi: 10.5281/zenodo.1234
        date-released: 2017-12-18

    Ihr könnt einfach das obige Beispiel anpassen um Eure eigene
    ``CITATION.cff``-Datei zu erzeugen oder die Website `cffinit
    <https://citation-file-format.github.io/cff-initializer-javascript/>`_
    verwenden.

    Es gibt auch einige Tools zum Verarbeiten von ``CITATION.cff``-Dateien:

    * `cff-converter-python
      <https://github.com/citation-file-format/cff-converter-python>`_
      konvertiert ``CITATION.cff``-Dateien in BibTeX, RIS, CodeMeta- und
      andere Dateiformate
    * `doi2cff <https://github.com/citation-file-format/doi2cff>`_ erstellt
      eine ``CITATION.cff``-Datei aus einem Zenodo DOI

Ihr solltet einen `Persistent Identifier (PID)
<https://de.wikipedia.org/wiki/Persistent_Identifier>`_ bereitstellen um die
langfristige Verfügbarkeit Eurer Software sicherzustellen. Sowohl das `Zenodo
<https://zenodo.org/>`_- als auch das `figshare
<https://figshare.com/>`_-Repository akzeptieren Quellcode einschließlich
Binärdateien und stellen DOIs hierfür breit. Und auch mit `CiteAs
<https://citeas.org/>`_ lassen sich Zitierinformationen für Software
abrufen.

.. seealso::
   * `Should I cite? <https://mr-c.github.io/shouldacite/index.html>`_
   * `How to cite software “correctly”
     <https://research-software.org/citation/researchers#how-to-cite-software-correctly>`_
   * Daniel S. Katz: `Compact identifiers for software: The last missing link in
     user-oriented software citation?
     <https://danielskatzblog.wordpress.com/2018/02/06/compact-identifiers-for-software-the-last-missing-link-in-user-oriented-software-citation/>`_
   * `Neil Chue Hong: How to cite software: current best practice
     <https://zenodo.org/record/2842910#.XspLsxMzbOQ>`_
   * Stephan Druskat, Radovan Bast, Neil Chue Hong, Alexander Konovalov, Andrew
     Rowley, Raniere Silva: `A standard format for CITATION files
     <https://www.software.ac.uk/index.php/blog/2017-12-12-standard-format-citation-files>`_
   * `Module-5-Open-Research-Software-and-Open-Source
     <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source/blob/master/content_development/README.md/>`_
   * Software Heritage: `Save and reference research software
     <https://www.softwareheritage.org/save-and-reference-research-software/>`_
   * `Mining software metadata for 80 M projects and even more
     <https://www.softwareheritage.org/2019/05/28/mining-software-metadata-for-80-m-projects-and-even-more/>`_
   * `Extensions to schema.org to support structured, semantic, and executable
     documents <https://github.com/stencila/schema>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    authorship
    journals
