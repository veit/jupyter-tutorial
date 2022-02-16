NumPy
=====

`NumPy <https://numpy.org/>`_ is the abbreviation for numeric Python. Many Python
packages that provide scientific functions use NumPy’s array objects as one of the
standard interfaces for data exchange. In the following, I will give a brief overview of
the main functionality of NumPy:

* :doc:`ndarray <ndarray>`, an efficient multidimensional array that provides fast
  array-based operations, such as shuffling and cleaning data, subgrouping and filtering,
  transformation and all other kinds of computations. There are also flexible functions
  for broadcasting, i.e. evaluations of arrays of different sizes.
* Mathematical functions for fast operations on whole arrays of data, such as sorting,
  uniqueness and set operations. Instead of loops with ``if``-``elif``-``else`` branches,
  the expressions are written in conditional logic.
* Tools for reading and writing array data to disk and working with `memory mapped
  <https://en.wikipedia.org/wiki/Memory-mapped_I/O>`_ files.
* Functions for linear algebra, random number generation and Fourier transform.
* A C API for connecting NumPy to libraries written in C, C++ or FORTRAN.

.. note::

    This section introduces you to the basics of using NumPy arrays and should be
    sufficient to follow the rest of the tutorial. For many data analytic applications,
    it is not necessary to have a deep understanding of NumPy, but mastering
    array-oriented programming and thinking is an important step on the way to becoming a
    data scientist.

.. seealso::
    * `Home
      <https://numpy.org/>`_
    * `Docs
      <https://numpy.org/doc/stable/>`_
    * `GitHub
      <https://github.com/numpy/numpy>`_
    * `Tutorials
      <https://numpy.org/numpy-tutorials/>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    intro.ipynb
    ndarray.ipynb
    dtype.ipynb
    arithmetic.ipynb
    indexing-slicing.ipynb
    transpose.ipynb
    ufunc.ipynb
    vectorisation.ipynb
    where.ipynb
    statistics.ipynb
    bool.ipynb
    sort.ipynb
    unique.ipynb
    file.ipynb
