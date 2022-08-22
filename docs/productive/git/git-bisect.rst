Find regressions with ``git bisect``
====================================

``git bisect`` allows you to find the git commit that introduced a regression.

#. To do this, start the search with ``git bisect start``. Then you can narrow
   down the area where a bug was introduced with  ``git bisect bad [COMMIT]``
   and ``git bisect good [COMMIT]``. Alternatively, you can use the short form
   ``git bisect start [BAD COMMIT] [GOOD COMMIT]``. ``git bisect`` then checks
   out a commit in the middle and asks you to test it, for example:

   .. code-block:: console

    $ git bisect start v2.6.27 v2.6.25
    Bisecting: 10928 revisions left to test after this (roughly 14 steps)
    [2ec65f8b89ea003c27ff7723525a2ee335a2b393] x86: clean up using max_low_pfn on 32-bit

#. The search can now be continued manually or automatically with a script.
   Manually, you can use  ``git bisect bad`` and ``git bisect good`` to narrow
   down the area in which an error was introduced. If this commit is found, the
   output may look like this:

   .. code-block:: console

    $ git bisect bad
    2ddcca36c8bcfa251724fe342c8327451988be0d is the first bad commit
    commit 2ddcca36c8bcfa251724fe342c8327451988be0d
    Author: Linus Torvalds <torvalds@linux-foundation.org>
    Date:   Sat May 3 11:59:44 2008 -0700

        Linux 2.6.26-rc1

    :100644 100644 5cf82581... 4492984e... M      Makefile

#. We then use ``git show HEAD`` to check what changes have been made in this
   commit:

   .. code-block:: console

    $ git show HEAD
    commit 2ddcca36c8bcfa251724fe342c8327451988be0d
    Autor: Linus Torvalds <torvalds@linux-foundation.org>
    Datum: Sa 3. Mai 11:59:44 2008 -0700

        Linux 2.6.26-rc1

    diff --git a / Makefile b / Makefile
    index 5cf8258 ..4492984 100644
    --- a / Makefile
    +++ b / Makefile
    @@ -1,7 +1,7 @@
     VERSION = 2
     PATCHLEVEL = 6
    -SUBLEVEL = 25
    -EXTRAVERSION =
    + SUBLEVEL = 26
    + EXTRAVERSION = -rc1
     NAME = Funky Weasel ist Jiggy wit it

     # * DOKUMENTATION *

   Checking whether faulty code was introduced with a commit can also be
   automated. You can find an example of this in the issue
   `fetch_california_housing fails in CI on master
   <https://github.com/scikit-learn/scikit-learn/issues/14956>`_ from
   scikit-learn:

   .. code-block:: console

    git bisect run pytest sklearn/utils/tests/test_multiclass.py -k test_unique_labels_non_specific

#. The scikit-learn-issue also shows how you can tell others the results of your
   bisect search in a traceable way using  ``$ git bisect log``:

   .. code-block::

    $ git bisect log
    81f2d3a0e *   massich/multiclass_type_of_target Merge branch 'master' into multiclass_type_of_target
              |\
    15f24f25d | * bad DOC Cleaning for what's new
    fbb2c7c70 | * good-fbb2c7c7007dc373c462e39ab273a183a8823d58 @ ENH Adds _MultimetricScorer for Optimized Scoring  (#14593)
    …

   With ``$ git bisect log > bisect_log.txt`` you can save your search in a
   reproducible way for others:

   .. code-block:: console

    $ git bisect replay bisect_log.txt

#. Finally, you can use ``$ git bisect reset`` to return to the branch you were
   in before the bisect search:

   .. code-block:: console

    $ git bisect reset
    Checking out files: 100% (21549/21549), done.
    Previous HEAD position was 2ddcca3... Linux 2.6.26-rc1
    Switched to branch 'master'

.. seealso::
   * `Fighting regressions with git bisect
     <https://git-scm.com/docs/git-bisect-lk2009>`_
   * `Docs <https://git-scm.com/docs/git-bisect>`_
