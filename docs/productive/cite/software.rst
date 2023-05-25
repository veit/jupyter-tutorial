Cite software
=============

James Howison and Julia Bullard listed the following examples in descending
reputations in their 2016 article `Software in the scientific literature
<https://doi.org/10.1002/asi.23538>`_:

#. citing publications that describe the respective software
#. citing operating instructions
#. citing the software project website
#. link to a software project website
#. mention the software name

The situation remains unsatisfactory for the authors of software, especially if
they differ from the authors of the software description. Conversely, research
software is unfortunately not always well suited to being cited. For example,
others will hardly be able to cite your software directly if you send it to
them as an email attachment. Even a download link is not really useful here. It
is better to provide a `persistent identifier (PID)
<https://en.wikipedia.org/wiki/Persistent_identifier>`_ to ensure the long-term
availability of your software. Both `Zenodo <https://zenodo.org/>`__ and
`figshare <https://figshare.com/>`_ repositories accept source code including
binaries and provide `Digital Object Identifiers (DOI)
<https://en.wikipedia.org/wiki/Digital_object_identifier>`_ for them. The same
applies to `CiteAs <https://citeas.org/>`_, which can be used to retrieve
citation information for software.

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
   * `Guide to Citation File Format schema
     <https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md>`_
   * `schema.json
     <https://github.com/citation-file-format/citation-file-format/blob/main/schema.json>`_

.. _zenodo:

Create a DOI with Zenodo
------------------------

`Zenodo <https://zenodo.org/>`__ enables software to be archived and a DOI to be
provided for it. In the following I will show which steps are required on the
example of the Jupyter tutorial:

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

#. Finally, you can include a badge in the readme of your software, for example:

   Markdown:
    .. code-block:: md

        [![DOI](https://zenodo.org/badge/199994535.svg)](https://zenodo.org/badge/latestdoi/199994535)

   reStructedText:
    .. code-block:: rst

        .. image:: https://zenodo.org/badge/199994535.svg
           :target: https://zenodo.org/badge/latestdoi/199994535

Metadata formats
----------------

The `FORCE11 <https://www.force11.org/group/software-citation-working-group>`_
working group has published a paper in which the principles of scientific
software citation are presented: `FORCE11 Software Citation Working Group
<https://doi.org/10.7717/peerj-cs.86>`_ by Arfon Smith, Daniel Katz and Kyle
Niemeyer 2016. Two projects are currently emerging for structured metadata:

.. _codemeta:

CodeMeta
~~~~~~~~

`CodeMeta <https://codemeta.github.io/>`__ is an exchange scheme for general
software metadata and reference implementation for JSON for Linking Data
(`JSON-LD <https://json-ld.org/>`_).

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

.. _cff:

Citation File Format
~~~~~~~~~~~~~~~~~~~~

`Citation File Format <https://citation-file-format.github.io/>`_ is a scheme
for software citation metadata in machine-readable
:doc:`/data-processing/serialisation-formats/yaml/index` format

A file ``CITATION.cff`` should be stored in the root directory of the software
repository.

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

You can easily adapt the example above to create your own ``CITATION.cff`` file
or use the `cffinit
<https://citation-file-format.github.io/cff-initializer-javascript/>`_ website.

With `cff-validator <https://github.com/marketplace/actions/cff-validator>`_ you
have a GitHub action that checks ``CITATION.cff`` files with the R package
``V8``.

There are also some tools for the workflow of ``CITATION.cff`` files:

* `cff-converter-python
  <https://github.com/citation-file-format/cff-converter-python>`_ converts
  ``CITATION.cff`` files to BibTeX, RIS, :ref:`codemeta` and other
  file formats
* `doi2cff <https://github.com/citation-file-format/doi2cff>`_ creates a
  ``CITATION.cff`` file from a Zenodo DOI

GitHub also offers a service to copy the information from ``CITATION.cff`` files
in APA and BibTex format.

.. figure:: github-cite.png
   :alt: Popup on the landing page of a GitHub repository with the
         possibility to export ADA and BibTex formats.

.. seealso::
   * `GitHub Docs: About CITATION files
     <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files>`_

When registering a DOI via Zenodo the ``CITATION.cff`` file in the GitHub
repository is also be used.  Also `Zotero <https://www.zotero.org/>`_ interprets
the :ref:`cff` file in GitHub repositories; however, Zotero can take
meta-information of the repository, such as company, programming language
:abbr:`etc. (et cetera)`, even without a :ref:`cff` file.

Git2PROV
~~~~~~~~

`Git2PROV <https://github.com/IDLabResearch/Git2PROV>`_ generates PROV data from
the information in a Git repository.

On the command line, the conversion can be easily executed with:

.. code-block:: console

    $ git2prov git_url [serialization]

For example:

.. code-block:: console

    $ git2prov git@github.com:veit/jupyter-tutorial.git PROV-JSON

In total, the following serialisation formats are available:

* ``PROV-N``
* ``PROV-JSON``
* ``PROV-O``
* ``PROV-XML``

Alternatively, Git2PROV also provides a web server with:

.. code-block:: console

    $ git2prov-server [port]

.. seealso::
   * `Git2PROV: Exposing Version Control System Content as W3C PROV
     <http://ceur-ws.org/Vol-1035/iswc2013_demo_32.pdf>`_
   * `GitHub-Repository <https://github.com/IDLabResearch/Git2PROV>`_

HERMES
------

`HERMES <https://project.software-metadata.pub>`_ simplifies the publication of
research software by continuously retrieving existing metadata in :ref:`cff`,
:ref:`codemeta` and :doc:Git <../git/index>`. Subsequently, the metadata is also
compiled appropriately for `InvenioRDM
<https://invenio-software.org/products/rdm/>`_ and `Dataverse
<https://dataverse.org/>`_. Finally, :ref:`CITATION.cff <cff>` and
:ref:`codemeta.json <codemeta>` are also updated for the publication
repositories.

#. Add ``.hermes/`` to the :ref:`.gitignore <gitignore>` file
#. Provide :ref:`CITATION.cff <cff>` file with additional metadata

   .. important::
      Make sure  ``license`` is defined in the :ref:`CITATION.cff <cff>` file;
      otherwise, your release will not be accepted as open access by the
      :ref:`Zenodo <zenodo>` sandbox.

#. Configure HERMES workflow

   The HERMES workflow is configured in the file
   :doc:`/data-processing/serialisation-formats/toml/index`, where each step
   gets its own section.

   If you want to configure HERMES to use the metadata from :doc:`Git
   <../git/index>` and :ref:`CITATION.cff <cff>`, and to file in the Zenodo sandbox built on InvenioRDM, the :file:`hermes.toml` file looks like this:

   .. literalinclude:: hermes.toml
      :caption: hermes.toml
      :name: hermes.toml

#. Access token for Zenodo Sandbox

   In order for GitHub Actions to publish your repository in the `Zenodo Sandbox
   <https://sandbox.zenodo.org/>`_, you need a personal access token. To do
   this, you need to log in to Zenodo Sandbox and then create a `personal access
   token
   <https://sandbox.zenodo.org/account/settings/applications/tokens/new/>`_ in
   your user profile with the name :samp:`HERMES workflow` and the scopes
   :guilabel:`deposit:actions` und :guilabel:`deposit:write`:

   .. image:: zenodo-personal-access-token.png
      :alt: Zenodo: Neues persönliches Zugangstoken

#. Copy the newly created token to a new `GitHub secret
   <https://docs.github.com/de/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository>`_
   named :samp:`ZENODO_SANDBOX` in your repository: `Settings --> Secrets and
   Variables --> Actions --> New repository secret`:

   .. image:: github-new-action-secret.png
      :alt: GitHub: Neues Action-Secret

#. Configure the GitHub action

   The HERMES project provides templates for continuous integration in a special
   repository: `hermes-hmc/ci-templates
   <https://github.com/hermes-hmc/ci-templates>`_. Copy the template file
   `TEMPLATE_hermes_github_to_zenodo.yml
   <https://github.com/hermes-hmc/ci-templates/blob/main/TEMPLATE_hermes_github_to_zenodo.yml>`_
   into the :file:`.github/workflows/` directory of your repository and rename
   it, for example to :file:`hermes_github_to_zenodo.yml`.

   Then you should go through the file and look for comments marked :samp:`#
   ADAPT`. Modify the file to suit your needs.

   Finally, add the workflow file to version control and push it to the GitHub
   server:

   .. code-block:: console

      $ git add .github/workflows/hermes_github_to_zenodo.yml
      $ git commit -m ":construction_worker: GitHub action for automatic publication with HERMES"
      $ git push

#. GitHub actions should be allowed to create pull requests in your repository

   The HERMES workflow will not publish metadata without your approval. Instead,
   it will create a pull request so that you can approve or change the metadata
   that is stored. To enable this, go to :menuselection:`Settings --> Actions
   --> General` in your repository and in the :guilabel:`Workflow permissions`
   section, enable :guilabel:`Allow GitHub Actions to create and approve pull
   requests`.
