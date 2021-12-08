Licensing
=========

In order for others to use your software, it should be given a license that
describes the terms of use. Otherwise, it should mostly be protected by
copyright. Authors are those who originally contributed to the software. If
software is to be relicensed, the consent of all authors is required.

.. note::
   This does not constitute legal advice. If in doubt, contact a lawyer or the
   legal department of your company.

.. seealso::
   * `The Whys and Hows of Licensing Scientific Code
     <https://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/>`_
   * `A Quick Guide to Software Licensing for the Scientist-Programmer
     <https://doi.org/10.1371/journal.pcbi.1002598>`_
   * Karl Fogel: `Producing Open Source Software <https://producingoss.com/>`_

Proprietary software licenses
-----------------------------

Proprietary software licenses are rarely standardised; they can be commercial,
shareware, or freeware.

Free and open source software licenses
--------------------------------------

They are defined by the `Free Software Foundation (FSF)
<https://www.fsf.org/de/?set_language=de>`_ and the `Open Source Initiative
(OSI) <https://opensource.org/>`_. A distinction can essentially be made between
copyleft, permissive and public domain licenses.

Copyleft licenses
~~~~~~~~~~~~~~~~~

Copyleft licenses oblige the licensees to place any processing of the software
under the license of the original work. This is to prevent usage restrictions of
the software. The best known copyleft license is the GNU General Public License
(GPL). The copyleft of the GPL is seen as very strong, while that of the Mozilla
Public License is seen as very weak.

Since the licensors are not bound by their own copyleft, they can also publish
new versions under a proprietary license or allow third parties to do so
(multiple licensing).

Copyleft licenses can quickly lead to incompatibilities with free licenses
without copyleft. For example, the 3 Clause BSD license is incompatible with the
GPL.

Permissive open source licenses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Permissive open source licenses allow broader reuse than copyleft licenses.
Derivatives and copies of the source code can be distributed under conditions
that have fundamentally different properties than those of the original license.
The best known examples of such licenses are the MIT license and the BSD
license.

Public domain licenses
~~~~~~~~~~~~~~~~~~~~~~

In the case of public domain licenses, copyrights are transferred to the general
public. The Creative Commons Zero license was created to identify the release of
the greatest possible usage rights.

Choosing a suitable license
---------------------------

Overviews of possible licenses can be found in the `SPDX License List
<https://spdx.org/licenses/>`_ or `OSI Open Source Licenses by Category
<https://opensource.org/licenses/category>`_. The websites
`Choose an open source license <https://choosealicense.com/>`_ and `Comparison
of free and open-source software licenses
<https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses>`_
supports you in choosing a suitable license.

If you want to achieve the widest possible distribution of your package, for
example, MIT or BSD versions are a good choice. The Apache licence protects you
better from from patent infringement, but it is not compatible with the GPL v2.
You should check what licences those packages have that you depend on and to
which you should be compatible. To analyse licences you can use `license
compatibility <https://en.wikipedia.org/wiki/License_compatibility>`_
and the `licensechecker
<https://boyter.org/2018/03/licensechecker-command-line-application-identifies-software-license/>`_, a command line tool that scans installation directories for licences. for licences.

Furthermore, it can also be useful to publish a package under several licences.
An example of this is `cryptography/LICENSE
<https://github.com/pyca/cryptography/blob/adf234e/LICENSE>`_.

GitHub
------

On `GitHub <https://github.com/>`_ you can have an open source license created in
your repository.

#. Go to the main page of your repository.
#. Click on *Create new file* and then enter ``LICENSE`` or ``LICENSE.md`` as
   the file name.
#. Then you can click on *Choose a license template*.
#. Now you can select the open source license that is suitable for your
   repository.
#. You will now be asked for additional information if the selected license
   requires this.
#. After you have given a commit message, for example ``Add license``, you can
   click on *Commit new file*.

If you’ve already added a ``/LICENSE`` file to your repository, GitHub uses
`licensee <https://github.com/licensee/licensee>`_ to compare the file with a
short `list of open source licenses  <https://choosealicense.com/appendix/>`_.
If GitHub can’t detect your repository’s license, it might contain multiple
licenses or be too complex. Then consider whether you can simplify the license,
for example by outsourcing complexity to the ``/README`` file.

Conversely, you can also search for repositories with specific licenses or
license families on GitHub. You can get an overview of the license keywords in
`Searching GitHub by license type
<https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#searching-github-by-license-type>`_.

Finally, you can have `Shields.io <https://shields.io/>`_ generate a license
badge for you, which you can include in your ``README`` file, for example

.. code-block:: rst

    |License|

    .. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
       :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE

|License|

.. |License| image:: https://img.shields.io/github/license/veit/jupyter-tutorial.svg
   :target: https://github.com/veit/jupyter-tutorial/blob/master/LICENSE

Standard format for licensing
-----------------------------

`SPDX <https://spdx.dev/>`_ stands for *Software Package Data Exchange* and
defines a standardised method for the exchange of copyright and licensing
information between projects and people. You can choose the appropriate SPDX
identifiers from the `SPDX License List <https://spdx.org/licenses/>`_ and then
add to the header of your licence files:

.. code-block::

    # SPDX-FileCopyrightText: [year] [copyright holder] <[email address]>
    #
    # SPDX-License-Identifier: [identifier]

Check conformity
----------------

`REUSE <https://reuse.software/>`_ was initiated by the Free Software Foundation
Europe (FSFE) to facilitate the licensing of free software projects. The `REUSE
tool <https://git.fsfe.org/reuse/tool>`_ checks licenses and supports you in
compliance with the license. With the `REUSE API
<https://reuse.software/dev/#api>`_ you can also generate a dynamic compliance
badge:

.. figure:: reuse-compliant.svg
   :alt: REUSE-compliant Badge

CIR workflow
~~~~~~~~~~~~

You can easily integrate REUSE into your continuous integration workflow, e.g.
for GitLab in the ``.gitlab-ci.yml`` file with:

.. code-block:: yaml

    reuse:
      image:
        name: fsfe/reuse:latest
        entrypoint: [""]
      script:
        - reuse lint

Alternatives
~~~~~~~~~~~~

`ClearlyDefined <https://clearlydefined.io/>`_
    It collects and displays information about the licensing and copyright
    situation of a software project
`OpenChain <https://www.openchainproject.org/>`_
    It recommends REUSE as a component to improve the clarity of the licensing
    and copyright situation, but has more stringent requirements to achieve full
    compliance.
`FOSSology <https://www.fossology.org/>`_
    Free software compliance toolkit that stores information in a database with
    license, copyright, and export scanners
