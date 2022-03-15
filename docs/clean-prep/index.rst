Data cleansing and validation
=============================

In the following, we want to give you a practical overview of various libraries
and methods for `data cleansing <https://en.wikipedia.org/wiki/Data_cleansing>`_
and validation with Python. Besides well-known libraries like NumPy and Pandas,
we also use several small, specialised libraries like :doc:`dedupe
<deduplicate>`, :doc:`fuzzywuzzy <string-matching>`, :doc:`voluptuous
<voluptuous>`, :doc:`bulwark <bulwark>`, :doc:`tdda <tdda>` and :doc:`hypothesis
<hypothesis>`. We prefer these more lightweight solutions to large, universal
systems like `Great Expectations <https://greatexpectations.io/>`_ or `MobyDQ
<https://ubisoft.github.io/mobydq/>`_.

Overview
--------

.. csv-table:: GitHub-Insights
    :header: "Name", "Stars", "Mitwirkende", "Commit-Aktivität", "Lizenz"

    "`fuzzywuzzy <https://github.com/seatgeek/fuzzywuzzy>`_",".. image:: https://raster.shields.io/github/stars/seatgeek/fuzzywuzzy",".. image:: https://raster.shields.io/github/contributors/seatgeek/fuzzywuzzy",".. image:: https://raster.shields.io/github/commit-activity/y/seatgeek/fuzzywuzzy",".. image:: https://raster.shields.io/github/license/seatgeek/fuzzywuzzy"
    "`dedupe <https://github.com/dedupeio/dedupe>`_",".. image:: https://raster.shields.io/github/stars/dedupeio/dedupe",".. image:: https://raster.shields.io/github/contributors/dedupeio/dedupe",".. image:: https://raster.shields.io/github/commit-activity/y/dedupeio/dedupe",".. image:: https://raster.shields.io/github/license/dedupeio/dedupe"
    "`Engarde <https://github.com/engarde-dev/engarde>`_",".. image:: https://raster.shields.io/github/stars/engarde-dev/engarde",".. image:: https://raster.shields.io/github/contributors/engarde-dev/engarde",".. image:: https://raster.shields.io/github/commit-activity/y/engarde-dev/engarde",".. image:: https://raster.shields.io/github/license/engarde-dev/engarde"
    "`Bulwark <https://github.com/ZaxR/bulwark>`_",".. image:: https://raster.shields.io/github/stars/ZaxR/bulwark",".. image:: https://raster.shields.io/github/contributors/ZaxR/bulwark",".. image:: https://raster.shields.io/github/commit-activity/y/ZaxR/bulwark",".. image:: https://raster.shields.io/github/license/ZaxR/bulwark"
    "`Hypothesis <https://github.com/HypothesisWorks/hypothesis>`_",".. image:: https://raster.shields.io/github/stars/HypothesisWorks/hypothesis",".. image:: https://raster.shields.io/github/contributors/HypothesisWorks/hypothesis",".. image:: https://raster.shields.io/github/commit-activity/y/HypothesisWorks/hypothesis",".. image:: https://raster.shields.io/github/license/HypothesisWorks/hypothesis"
    "`TDDA <https://github.com/tdda/tdda>`_",".. image:: https://raster.shields.io/github/stars/tdda/tdda",".. image:: https://raster.shields.io/github/contributors/tdda/tdda",".. image:: https://raster.shields.io/github/commit-activity/y/tdda/tdda",".. image:: https://raster.shields.io/github/license/tdda/tdda"
    "`Voluptuous <https://github.com/alecthomas/voluptuous>`_",".. image:: https://raster.shields.io/github/stars/alecthomas/voluptuous",".. image:: https://raster.shields.io/github/contributors/alecthomas/voluptuous",".. image:: https://raster.shields.io/github/commit-activity/y/alecthomas/voluptuous",".. image:: https://raster.shields.io/github/license/alecthomas/voluptuous"
    "`scikit-learn <https://github.com/scikit-learn/scikit-learn>`_",".. image:: https://raster.shields.io/github/stars/scikit-learn/scikit-learn",".. image:: https://raster.shields.io/github/contributors/scikit-learn/scikit-learn",".. image:: https://raster.shields.io/github/commit-activity/y/scikit-learn/scikit-learn",".. image:: https://raster.shields.io/github/license/scikit-learn/scikit-learn"
    "`pandera <https://github.com/pandera-dev/pandera>`_",".. image:: https://raster.shields.io/github/stars/pandera-dev/pandera",".. image:: https://raster.shields.io/github/contributors/pandera-dev/pandera",".. image:: https://raster.shields.io/github/commit-activity/y/pandera-dev/pandera",".. image:: https://raster.shields.io/github/license/pandera-dev/pandera"
    "`Validr <https://github.com/guyskk/validr>`_",".. image:: https://raster.shields.io/github/stars/guyskk/validr",".. image:: https://raster.shields.io/github/contributors/guyskk/validr",".. image:: https://raster.shields.io/github/commit-activity/y/guyskk/validr",".. image:: https://raster.shields.io/github/license/guyskk/validr"
    "`marshmallow <https://github.com/marshmallow-code/marshmallow>`_",".. image:: https://raster.shields.io/github/stars/marshmallow-code/marshmallow",".. image:: https://raster.shields.io/github/contributors/marshmallow-code/marshmallow",".. image:: https://raster.shields.io/github/commit-activity/y/marshmallow-code/marshmallow",".. image:: https://raster.shields.io/github/license/marshmallow-code/marshmallow"
    "`datacleaner <https://github.com/rhiever/datacleaner>`_",".. image:: https://raster.shields.io/github/stars/rhiever/datacleaner",".. image:: https://raster.shields.io/github/contributors/rhiever/datacleaner",".. image:: https://raster.shields.io/github/commit-activity/y/rhiever/datacleaner",".. image:: https://raster.shields.io/github/license/rhiever/datacleaner"
    "`Probatus <https://github.com/ing-bank/probatus>`_",".. image:: https://raster.shields.io/github/stars/ing-bank/probatus",".. image:: https://raster.shields.io/github/contributors/ing-bank/probatus",".. image:: https://raster.shields.io/github/commit-activity/y/ing-bank/probatus",".. image:: https://raster.shields.io/github/license/ing-bank/probatus"
    "`popmon <https://github.com/ing-bank/popmon>`_",".. image:: https://raster.shields.io/github/stars/ing-bank/popmon",".. image:: https://raster.shields.io/github/contributors/ing-bank/popmon",".. image:: https://raster.shields.io/github/commit-activity/y/ing-bank/popmon",".. image:: https://raster.shields.io/github/license/ing-bank/popmon"
    "`Pandas Profiling <https://github.com/ydataai/pandas-profiling>`_",".. image:: https://raster.shields.io/github/stars/ydataai/pandas-profiling",".. image:: https://raster.shields.io/github/contributors/ydataai/pandas-profiling",".. image:: https://raster.shields.io/github/commit-activity/y/ydataai/pandas-profiling",".. image:: https://raster.shields.io/github/license/ydataai/pandas-profiling"
    "`pandas-validation <https://github.com/jmenglund/pandas-validation>`_",".. image:: https://raster.shields.io/github/stars/jmenglund/pandas-validation",".. image:: https://raster.shields.io/github/contributors/jmenglund/pandas-validation",".. image:: https://raster.shields.io/github/commit-activity/y/jmenglund/pandas-validation",".. image:: https://raster.shields.io/github/license/jmenglund/pandas-validation"
    "`PandasSchema <https://github.com/multimeric/PandasSchema>`_",".. image:: https://raster.shields.io/github/stars/multimeric/PandasSchema",".. image:: https://raster.shields.io/github/contributors/multimeric/PandasSchema",".. image:: https://raster.shields.io/github/commit-activity/y/multimeric/PandasSchema",".. image:: https://raster.shields.io/github/license/multimeric/PandasSchema"
    "`Opulent-Pandas <https://github.com/danielvdende/opulent-pandas>`_",".. image:: https://raster.shields.io/github/stars/danielvdende/opulent-pandas",".. image:: https://raster.shields.io/github/contributors/danielvdende/opulent-pandas",".. image:: https://raster.shields.io/github/commit-activity/y/danielvdende/opulent-pandas",".. image:: https://raster.shields.io/github/license/danielvdende/opulent-pandas"
    "`signpost <https://github.com/ilsedippenaar/signpost>`_",".. image:: https://raster.shields.io/github/stars/ilsedippenaar/signpost",".. image:: https://raster.shields.io/github/contributors/ilsedippenaar/signpost",".. image:: https://raster.shields.io/github/commit-activity/y/ilsedippenaar/signpost",".. image:: https://raster.shields.io/github/license/ilsedippenaar/signpost"

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    nulls.ipynb
    outliers.ipynb
    string-matching.ipynb
    deduplicate.ipynb
    engarde.ipynb
    bulwark.ipynb
    hypothesis.ipynb
    tdda.ipynb
    voluptuous.ipynb
    scikit-learn-reprocessing.ipynb
    dask-pipeline.ipynb
