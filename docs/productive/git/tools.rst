Git tools for notebooks
=======================

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
