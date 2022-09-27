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

``nbdime``
----------

`nbdime <https://nbdime.readthedocs.io/>`_ is a GUI for diffs of `nbformat
<https://nbformat.readthedocs.io/>`_ and replaces `nbdiff
<https://github.com/tarmstrong/nbdiff>`_. It tries content-aware diffing as well
as the merging of notebooks, is not limited to the display of diffs, but also
prevents unnecessary changes from being checked in.

.. _nbstripout_label:

``nbstripout``
--------------

`nbstripout <https://github.com/kynan/nbstripout>`_ automates *Clear all
outputs*. It uses `nbformat <https://nbformat.readthedocs.io/>`_ and a few auto
magic to set up ``.git config``. In my opinion, however, it has two drawbacks:
it is limited to the problematic metadata section, and it is slow.
