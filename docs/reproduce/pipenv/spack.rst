Pipenv und Spack
================

Pipenv wurde bereits zur :doc:`Installation von Jupyter Notebooks
</first-steps/install>` verwendet. Wir benötigen hier jedoch Pipenv für unsere
:doc:`Spack Environments </reproduce/spack/envs>` um einerseits binärkompatible
Builds mit Spack erzeugen zu können und andererseits Python-Pakete für die
Datenerhebung, -Visualisierung etc. einfach nutzen zu können.

Zunächst muss hierfür die Passende Python-Version aus dem Spack-Environment
aktiviert werden:

   .. code-block:: console

    $ spack env activate python-374
    $ spack env status
    ==> In environment python-374
    $ which python
    /Users/veit/jupyter-tutorial/spackenvs/python-374/.spack-env/view/bin/python

Bestehendes Pipenv-Environment installieren:

   .. code-block:: console

    $ cd ~/jupyter-tutorial/pipenvs/python-374/
    $ pipenv install

