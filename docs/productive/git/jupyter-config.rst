Configuring Git for Jupyter Notebooks
=====================================

The results of the calculations can also be saved in the notebook file format
:ref:`nbformat <whats-an-ipynb-file>`. These can also be Base-64-coded blobs
for images and other binary data that should not normally be included in a
version management. These can be removed manually with :menuselection:`Cell -->
All Output --> Clear`, but you have to carry out these steps before every ``git
add``, and it also does not solve a second cause of the noise in ``git diff``,
namely some in the `metadata
<https://nbformat.readthedocs.io/en/latest/format_description.html#metadata>`_.

In order to get systematically comparable versions of notebooks in the version
management, we can use `jq <https://stedolan.github.io/jq/>`_, a lightweight
JSON processor. It takes some time to set up ``jq`` because it has its own
query/filter language, but the default settings are usually well chosen.

Installation
------------

``jq`` can be installed with:

.. tab:: Debian/Ubuntu

   .. code-block:: console

      $ sudo apt install jq

.. tab:: macOS

   .. code-block:: console

      $ brew install jq

Example
-------

A typical call is:

.. code-block:: console

    jq --indent 1  \
      '(.cells [] | select (has ("output")) | .outputs) = []
      | (.cells [] | select (has ("execution_count")) | .execution_count) = null
      | .metadata = {"language_info": {"name": "python", "pygments_lexer": "ipython3"}}
      | .Cells []. metadata = {}
      '  example.ipynb

Each line within the single quotation marks defines a filter – the first selects
all entries from the cells list and deletes the output. The next entry resets all
outputs. The third step deletes the notebook’s metadata and replaces it with a
minimum of necessary information so that the notebook can still be run without
complaints. The fourth filter line ``.cells []. metadata = {}``, deletes all meta
information. If you want to keep certain meta information, you can indicate this
here.

Set up
------

#. To make your work easier, you can create an alias in the ``~/.bashrc`` file:

   .. code-block:: bash

    alias nbstrip_jq="jq --indent 1 \
        '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
        | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
        | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
        | .cells[].metadata = {} \
        '"

#. Then you can conveniently enter the following in the terminal:

   .. code-block:: console

    $ nbstrip_jq example.ipynb > stripped.ipynb

#. If you start with an existing notebook, you should first add a ``filter``
   commit by simply reading in the newly filtered version of your notebook
   without the unwanted metadata. After you have added the notebook with ``git
   add``, you can see whether the filter has really worked with ``git diff
   --cached``  before you do ``git commit -m 'filter'``.

#. If you want to use this filter for all Git repositories, you can also
   configure your Git globally:

   #. First you add the following to your ``~/.gitconfig`` file:

      .. code-block:: ini

        [core]
        attributesfile = ~/.gitattributes

        [filter "nbstrip_jq"]
        clean = "jq --indent 1 \
                '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
                | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
                | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
                | .cells[].metadata = {} \
                '"
        smudge = cat
        required = true

      ``clean``
          is applied when adding changes to the stage area.
      ``smudge``
          is used when resetting the workspace by changes from the stage area.

   #. Then you have to specify the following in the ``~/.gitattributes`` file:

      .. code-block:: ini

         *.ipynb filter=nbstrip_jq

#. If you then use ``git add`` to add your notebok to the stage area, the
   ``nbstrip_jq`` filter will be applied.

    .. note::
       However, ``git diff`` will not show you any changes between the working
       and stage areas. Only with ``git diff --staged`` you can see that only the
       filtered changes have been applied.

    .. warning::
       ``clean`` and ``smudge`` filters often do not play well with ``git
       rebase`` across such filtered commits. Then you should disable these
       filters before rebasing.

#. And there is another problem: If such a notebook is run again, ``git diff``
   will not show any changes, but ``git status`` will. Therefore, the following
   should be entered in the ``~/.bashrc`` file to be able to quickly clean the
   respective working directory:

   .. code-block:: bash

      function nbstrip_all_cwd {
          for nbfile in *.ipynb; do
              echo "$( nbstrip_jq $nbfile )" > $nbfile
          done
          unset nbfile
      }
