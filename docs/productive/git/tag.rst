Git tags
========

Git tags are references that point to specific commits in the Git history. This
allows certain points in the history to be marked for a particular version, for
example :samp:`v3.9.16`. Tags are like :doc:`branch` that do not change, so have
no further history of commits.

:samp:`git tag {TAGNAME}`
    creates a tag, where :samp:`{TAGNAME}` is a semantic label for the current
    state of the Git repository. Git distinguishes between two different types
    of tags: annotated and lightweight tags. They differ in the amount of
    associated metadata.

    Annotated tags
        They store not only the :samp:`{TAGNAME}`, but also additional metadata
        such as the name and email address of the person who created the tag and
        the date. In addition, annotated tags have messages, similar to commits.
        You can create such tags, for example with :samp:`git tag -a {v3.9.16}
        -m '{Python 3.9.16}'`. You can then display this additional metadata for
        example with :samp:`git show {v3.9.16}`.
    Lightweight tags
        Lightweight tags can be created, for example, with :samp:`git tag
        {v3.9.16}` without the :samp:`-a`, :samp:`-s` or :samp:`-m` options.
        They create a tag checksum that are stored in the :file:`.git/`
        directory of your repo.

:samp:`git tag`
    lists the tags of your repo, for example:

    .. code-block:: console

        v0.9.9
        v1.0.1
        v1.0.2
        v1.1
        ...

    :samp:`git tag -l '{REGEX}'`
        lists only tags that match a regular expression.

:samp:`git tag -a {TAGNAME} {COMMIT-SHA}`
    creates a tag for a previous commit.

    The previous examples create tags for implicit commits that reference
    ``HEAD``. Alternatively, :samp:`git tag` can be passed the reference to a
    specific commit that you get with :doc:`log`.

    However, if you try to create a tag with the same identifier as an existing
    tag, Git will give you an error message, for example :samp:`Fatal: tag
    'v3.9.16' already exists`. If you try to tag an older commit with an
    existing tag, Git will give the same error.

    In case you need to update an existing tag, you can use the ``-f`` option,
    for example:

    .. code-block:: console

        $ git tag -af v3.9.16 595f9ccb0c059f2fb5bf13643bfc0cdd5b55a422 -m 'Python 3.9.16'
        Tag 'v3.9.16' updated (was 4f5c5473ea)

:samp:`git push origin {TAGNAME}`
    Sharing tags is similar to pushing branches: by default, :samp:`git push`
    does not share tags, but they must be explicitly passed to :samp:`git push
    for example`:

    .. code-block:: console

        $ git tag -af v3.9.16 -m 'Python 3.9.16'
        $ git push origin v3.9.16
        Counting objects: 1, done.
        Writing objects: 100% (1/1), 161 bytes, done.
        Total 1 (delta 0), reused 0 (delta 0)
        To git@github.com:python/cpython.git
         * [new tag]         v3.9.16 -> v3.9.16

    To push multiple tags at once, pass the :samp:`--tags` option to the
    :samp:`git push` command. Others get the tags on :samp:`git clone` or
    :samp:`git pull` of the repo.

:samp:`git checkout {TAGNAME}`
    switches to the state of the repo with this tag and detaches ``HEAD``. This
    means that any changes made now will not update the tag, but will end up in
    a detached commit that cannot be part of a branch and will only be directly
    accessible via the SHA hash of the commit. Therefore, a new branch is
    usually created when such changes are to be made, for example with
    :samp:`git checkout -b v3.9.17 v3.9.16`.

:samp:`git tag -d {TAGNAME}`
    deletes a tag, for example:

    .. code-block:: console

        $ git tag -d v3.9.16
        $ git push origin --delete v3.9.16
