Pipelines anzeigen
==================

Solche Datenpipelines lassen sich anzeigen oder als Abhängigkeitsgraph
darstellen mit ``dvc dag``:

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

* Mit ``dvc dag --dot`` kann auch eine ``.dot``-Datei für `Graphviz
  <http://www.graphviz.org/>`_ generiert werden:

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

