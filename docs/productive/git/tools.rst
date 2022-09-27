Git tools for notebooks
=======================

There are several issues to manage Jupyter Notebooks with Git:

* Jupyter Notebooks cell metadata changes even when no content changes have been
  made to the cells. This makes Git diffs unnecessarily complicated.
* The lines that Git writes to the ``*.ipynb`` files in case of :ref:`merge
  conflicts <merge-conflicts>` cause the notebooks to no longer be valid JSON
  and therefore cannot be opened by Jupyter: you will then get the *Error
  loading notebook* message when opening them.

  Conflicts are especially common in notebooks because Jupyter changes the
  following each time a notebook is run:

  * Each cell contains a number that indicates the order in which it was
    executed. If team members execute the cells in different order, every single
    cell has a conflict! To fix this manually would take a very long time.
  * For each image, such as a plot, Jupyter records not only the image itself in
    the notebook, but also a simple text description containing the ID of the
    object, for example :samp:`{<matplotlib.axes._subplots.AxesSubplot at
    0x7fbc113dbe90>}`. This will change every time you run a notebook, and
    therefore will conflict every time two people run that cell.
  * Some output can be non-deterministic, such as a notebook that uses random
    numbers or interacts with a service that provides different output over
    time.
  * Jupyter adds metadata to the notebook that describes the environment in
    which it was last run, such as the name of the kernel. This often varies
    between different installations, and so two people saving a notebook (even
    without other changes) will often have a conflict in the metadata.

``nbdev2``
----------

`nbdev2 <https://nbdev.fast.ai>`_ has a set of git hooks that provide clean git
diffs that automatically resolve most git conflicts and ensure that any
remaining conflicts can be fully resolved within the standard Jupyter notebook
environment:

* A new ``git merge`` driver provides notebook-native conflict markers that
  result in notebooks opening directly in Jupyter, even if there are Git
  conflicts. Local and remote changes are each shown as separate cells in the
  notebook, so you can simply delete the version you don’t want to keep or
  combine the two cells as needed.

  .. seealso::
     `nbdev.merge docs <https://nbdev.fast.ai/api/merge.html>`_

* Resolving git merges locally is extremely helpful, but we also need to resolve
  them remotely. For example, if a :doc:`merge request <gitlab/merge-requests.>`
  is submitted and then someone else submits the same notebook before the merge
  request is merged, it could cause a conflict:

  .. code-block:: javascript

        "outputs": [
         {
     <<<<<< HEAD
          "execution_count": 8,
     ======
          "execution_count": 5,
     >>>>>> 83e94d58314ea43ccd136e6d53b8989ccf9aab1b
          "metadata": {},

  The *save hook* of nbdev2 automatically removes all unnecessary metadata
  (including :samp:`execution_count`) and non-deterministic cell output; this
  means that there are no pointless conflicts like the one above, since this
  information is not stored in the commits in the first place.

To get started, follow the instructions in `Git-Friendly Jupyter
<https://nbdev.fast.ai/tutorials/git_friendly_jupyter.html>`_.

Other Git tools for notebooks
-----------------------------

ReviewNB
~~~~~~~~

`ReviewNB <https://www.reviewnb.com>`_ solves the problem of doing
:doc:`gitlab/merge-requests` with notebooks. GitLab’s code review GUI only works
with line-based file formats, such as Python scripts. Most of the time, however,
I prefer to check the source code notebooks because:

* I want to check the documentation and the tests, not just the implementation
* I want to see the changes to the cell output, like charts and tables, not just
  the code.

For this purpose ReviewNB is perfect.

``nbdime``
~~~~~~~~~~

`nbdime <https://nbdime.readthedocs.io/>`_ is a GUI for diffs of `nbformat
<https://nbformat.readthedocs.io/>`_ and replaces `nbdiff
<https://github.com/tarmstrong/nbdiff>`_. It tries content-aware diffing as well
as the merging of notebooks, is not limited to the display of diffs, but also
prevents unnecessary changes from being checked in.

.. _nbstripout_label:

``nbstripout``
~~~~~~~~~~~~~~

`nbstripout <https://github.com/kynan/nbstripout>`_ automates *Clear all
outputs*. It uses `nbformat <https://nbformat.readthedocs.io/>`_ and a few auto
magic to set up ``.git config``. In my opinion, however, it has two drawbacks:

* it is limited to the problematic metadata section
* it is slow.
