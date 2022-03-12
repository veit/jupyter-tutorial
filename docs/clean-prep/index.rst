Data cleansing and validation
=============================

In the following, we want to give you a practical overview of various libraries
and methods for `data cleansing <https://en.wikipedia.org/wiki/Data_cleansing>`_
and validation with Python. Besides well-known libraries like NumPy and Pandas,
we also use several small, specialised libraries like :doc:`dedupe
<deduplicate>`, :doc:`fuzzywuzzy <string-matching>`, :doc:`voluptuous
<voluptuous>`, :doc:`bulwark <bulwark>`, :doc:`tdda <tdda>` and :doc:`hypothesis
<hypothesis>`. We prefer these more lightweight solutions to large, universal
systems like `Great Expectations <https://greatexpectations.io/>`_.

.. seealso::
   * `pandera <https://pandera.readthedocs.io/en/stable/>`_
   * `pandas-validation <https://pandas-validation.readthedocs.io/en/latest/>`_
   * `PandasSchema <https://multimeric.github.io/PandasSchema/>`_
   * `Opulent-Pandas <https://github.com/danielvdende/opulent-pandas>`_
   * `signpost <https://github.com/ilsedippenaar/signpost>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    deduplicate.ipynb
    string-matching.ipynb
    nulls.ipynb
    scikit-learn-reprocessing.ipynb
    dask-pipeline.ipynb
    voluptuous.ipynb
    engarde.ipynb
    bulwark.ipynb
    tdda.ipynb
    hypothesis.ipynb
