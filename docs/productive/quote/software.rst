Citing software
===============

James Howison and Julia Bullard listed the following examples in descending
reputations in their 2016 article `Software in the scientific literature
<https://doi.org/10.1002/asi.23538>`_:

#. citing publications that describe the respective software
#. citing operating instructions
#. citing the software project website
#. link to a software project website
#. mention the software name

Nevertheless, the situation remains unsatisfactory for software authors,
especially if they differ from the authors of the software description.
Conversely, research software is unfortunately not always well suited to be
cited. Colleagues will hardly be able to cite your software directly if you send
them the software as an attachment to an email. Even a download link is not
really useful here. But how can authors make their software citable?

`Digital object identifier (DOI)
<https://en.wikipedia.org/wiki/Digital_object_identifier>`_ are commonly used in
science for citations. `Zenodo <https://zenodo.org/>`_ enables software to be
archived and a DOI to be provided for it. In the following I will show which
steps are required on the example of the Jupyter tutorial:

#. If you haven’t already, `create an account on Zenodo
   <https://zenodo.org/signup/>`_, preferably with GitHub.

#. Now select the repository that you want to archive:

   .. figure:: zenodo-github.png
      :alt: Enable repositories for Zenodo

#. Check whether Zenodo has created a webhook in your repository for the
   *Releases* event:

   .. figure:: zenodo-webhook.png
      :alt: Zenodo webhook

#. Create a new release:

   .. figure:: github-release.png
      :alt: Github releases

#. Check that the :abbr:`DOI (Digital object identifier)` was created correctly:

   .. figure:: zenodo-release.png
      :alt: Zenodo release

#. Finally, you can include a badge in the readme of your software, e.g.:

   Markdown:
    .. code-block:: md

        [![DOI](https://zenodo.org/badge/199994535.svg)](https://zenodo.org/badge/latestdoi/199994535)

   reStructedText:
    .. code-block:: rst

        .. image:: https://zenodo.org/badge/199994535.svg
           :target: https://zenodo.org/badge/latestdoi/199994535

The `FORCE11 <https://www.force11.org/group/software-citation-working-group>`_
working group has published a paper in which the principles of scientific
software citation are presented: `FORCE11 Software Citation Working Group
<https://doi.org/10.7717/peerj-cs.86>`_ by Arfon Smith, Daniel Katz and Kyle
Niemeyer 2016. Two projects are currently emerging for structured metadata:

`CodeMeta <https://codemeta.github.io/>`_
    Exchange scheme for general software metadata and reference implementation
    for JSON for Linking Data (`JSON-LD <https://json-ld.org/>`_).

    A ``codemeta.json`` file is expected in the root directory of the software
    repository. The file can look like this:

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
    Scheme for software citation metadata in machine-readable `YAML
    <https://yaml.org/>`_ format

    A file ``CITATION.cff`` should be stored in the root directory of the
    software repository.

    The content of the file can look like this:

    .. code-block::

        cff-version: "1.1.0"
        message: "If you use this tutorial, please cite it as below."
        authors:
          -
            family-names: Schiele
            given-names: Veit
            orcid: "https://orcid.org/https://orcid.org/0000-0002-2448-8958"
        identifiers:
          -
            type: doi
            value: "10.5281/zenodo.4147287"
        keywords:
          - "data-science"
          - jupyter
          - "jupyter-notebooks"
          - "jupyter-kernels"
          - ipython
          - pandas
          - spack
          - pipenv
          - ipywidgets
          - "ipython-widget"
          - dvc
        title: "Jupyter tutorial"
        version: "0.8.0"
        date-released: 2020-10-08
        license: "BSD-3-Clause"
        repository-code: "https://github.com/veit/jupyter-tutorial"

    You can easily adapt the example above to create your own ``CITATION.cff``
    file or use the `cffinit
    <https://citation-file-format.github.io/cff-initializer-javascript/>`_
    website.

    There are also some tools for processing ``CITATION.cff`` files:

    * `cff-converter-python
      <https://github.com/citation-file-format/cff-converter-python>`_
      converts ``CITATION.cff`` files to BibTeX, RIS, CodeMeta and other file
      formats
    * `doi2cff <https://github.com/citation-file-format/doi2cff>`_ creates a
      ``CITATION.cff`` file from a Zenodo DOI

    GitHub also offers a service to copy the information from ``CITATION.cff``
    files in APA and BibTex format.

    .. figure:: github-cite.png
       :alt: Popup on the landing page of a GitHub repository with the
             possibility to export ADA and BibTex formats.

    .. seealso::
       * `GitHub Docs: About CITATION files
         <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files>`_

You should provide a `Persistent Identifier (PID)
<https://en.wikipedia.org/wiki/Persistent_identifier>`_ to ensure the long-term
availability of your software. Both the `Zenodo <https://zenodo.org/>`_ and
`figshare <https://figshare.com/>`_ repositories accept source code including
binary files and provide DOIs for this. And citation information for software
can also be called up with `CiteAs <https://citeas.org/>`_.

.. seealso::
   * `Should I cite? <https://mr-c.github.io/shouldacite/index.html>`_
   * `How to cite software “correctly”
     <https://cite.research-software.org/>`_
   * Daniel S. Katz: `Compact identifiers for software: The last missing link in
     user-oriented software citation?
     <https://danielskatzblog.wordpress.com/2018/02/06/compact-identifiers-for-software-the-last-missing-link-in-user-oriented-software-citation/>`_
   * `Neil Chue Hong: How to cite software: current best practice
     <https://zenodo.org/record/2842910>`_
   * `Recognizing the value of software: a software citation guide
     <https://f1000research.com/articles/9-1257/v2>`_
   * Stephan Druskat, Radovan Bast, Neil Chue Hong, Alexander Konovalov, Andrew
     Rowley, Raniere Silva: `A standard format for CITATION files
     <https://www.software.ac.uk/blog/2017-12-12-standard-format-citation-files>`_
   * `Module-5-Open-Research-Software-and-Open-Source
     <https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source/blob/master/content_development/README.md/>`_
   * Software Heritage: `Save and reference research software
     <https://www.softwareheritage.org/save-and-reference-research-software/>`_
   * `Mining software metadata for 80 M projects and even more
     <https://www.softwareheritage.org/2019/05/28/mining-software-metadata-for-80-m-projects-and-even-more/>`_
   * `Extensions to schema.org to support structured, semantic, and executable
     documents <https://github.com/stencila/schema>`_
