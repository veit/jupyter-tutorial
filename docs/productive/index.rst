Create a product
================

    «Non-reproducible single occurrences are of no significance to science.»[#]_

.. [#] Karl Popper in *The Logic of Scientific Discovery*, 1959

In order for others to be able to use your code, it should meet some conditions:

* You should not silently rely on specific resources and environments
* Required software packages and hardware should be specified in the
  requirements
* Path information will only work in a different context within your package or
  in previously generated directories and files
* Do not share secrets like login details or internal IP numbers in your
  published product

There are various tools that support you in creating shareable products. These
can be tools on the one hand for the :doc:`versioning of the source code
<git/index>` and the :doc:`training data <dvc/index>` as well as for the
reproducibility of the :doc:`execution environments <envs/index>`, on the other
hand for :doc:`testing`, :doc:`logging/index`, :doc:`documenting
<documenting/index>` and :doc:`creating packages <packaging/index>`.

.. seealso::

   * `Dustin Boswell, Trevor Foucher: The Art of Readable Code
     <https://learning.oreilly.com/library/view/~/9781449318482/>`_
   * TIB workshop «FAIR Data and Software»

     * `GitHub Page
       <https://tibhannover.github.io/2018-07-09-FAIR-Data-and-Software/>`_
     * `GitHub Repository
       <https://github.com/TIBHannover/2018-07-09-FAIR-Data-and-Software>`_
     * `Slides <https://doi.org/10.5281/zenodo.3707745>`_
   * `Dryad: Best practices for creating reusable data publications
     <https://datadryad.org/stash/best_practices>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    git/index
    dvc/index
    packaging/index
    documenting/index
    licensing
    cite/index
    envs/index
    testing
    logging/index
