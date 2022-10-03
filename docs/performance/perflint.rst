perflint
========

`perflint <https://github.com/tonybaloney/perflint>`_ is an extension for
`pylint <https://pylint.org/>`_ for performance anti-patterns, among others:

W8101: ``unnecessary-list-cast``
    Unnecessary use of ``list()`` on an already iterable type.
W8102: ``incorrect-dictionary-iterator``
    Incorrect iterator method for ``dict``: Python dictionaries store keys and
    values in two separate tables. They can be iterated separately. Using
    ``.items()`` and discarding either the key or the value with ``_`` is
    inefficient when ``.keys()`` or ``.values()`` can be used instead.
W8201: ``loop-invariant-statement``
    The loop is examined to determine statements or expressions whose result is
    constant on each iteration of a loop because they are based on named
    variables that are not changed during the iteration.
W8202: ``loop-global-usage``
    Global name usage in a loop: loading global variables is slower than loading
    local variables. The difference is marginal, but when passed in a loop,
    there can be a noticeable speed improvement.
R8203: ``loop-try-except-usage``
    Up until Python 3.10, ``try``…``except`` blocks are very computationally
    intensive compared to ``if`` statements.

    Avoid using them in a loop as they can cause significant overhead. Refactor
    your code so that no iteration-specific details are required and put the
    entire loop in the ``try`` block.

W8204: ``memoryview-over-bytes``
    Slicing byte objects in loops is inefficient because it creates a copy of
    the data. Use ``memoryview()`` instead.

    .. seealso::
        * `Zero-copy interactions
          <https://effectivepython.com/2019/10/22/memoryview-bytearray-zero-copy-interactions>`_
        * `Memoryview Benchmarks
          <https://jakevdp.github.io/blog/2012/08/08/memoryview-benchmarks/>`_
        * `Memoryview Benchmarks 2
          <https://jakevdp.github.io/blog/2012/08/16/memoryview-benchmarks-2/>`_

W8205: ``dotted-import-in-loop``
    Direct import of the name ``%s`` is more efficient in a loop. In Python, you
    can import a module and then access submodules as attributes. You can also
    access functions as attributes of that module. This keeps the import
    statements to a minimum. However, if you use this method in a loop, it is
    inefficient because each loop pass loads the global, then the attribute,
    then the method.
W8301: ``use-tuple-over-list``
    Use a tuple instead of a list for an immutable sequence: both the
    construction and indexing of a tuple is faster than that of a list.
W8401: ``use-list-comprehension``
    Use list comprehensions with or without an ``if`` statement instead of a
    ``for`` loop.
W8402: ``use-list-copy``
    Use ``list.copy()`` instead of a ``for`` loop.
W8403: ``use-dict-comprehension``
    Uses a dictionary comprehension instead of a simple ``for`` loop.
