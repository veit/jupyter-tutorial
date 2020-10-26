View pipelines
==============

Such data pipelines can be displayed or represented as a dependency graph with
``dvc dag``:

  .. code-block:: console

    $ dvc dag

        +-------------------+
        | data/data.xml.dvc |
        +-------------------+
                  *
                  *
                  *
              +-------+
              | split |
              +-------+
                  *
                  *
                  *
            +-----------+
            | featurize |
            +-----------+
             **        **
           **            *
          *               **
    +-------+               *
    | train |             **
    +-------+            *
             **        **
               **    **
                 *  *
            +----------+
            | evaluate |
            +----------+

    data/data.xml.dvc
    prepare.dvc
    featurize.dvc
    train.dvc
    evaluate.dvc

* With ``dvc dag --dot`` a ``.dot`` file for `Graphviz
  <http://www.graphviz.org/>`_ is generated:

.. graphviz::

    strict digraph  {
        "data/data.xml.dvc";
        "split";
        "train";
        "featurize";
        "evaluate";
        "data/data.xml.dvc" -> "split";
        "split" -> "featurize";
        "featurize" -> "train";
        "featurize" -> "evaluate";
        "train" -> "evaluate";
    }
