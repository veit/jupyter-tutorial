Splitting repos
===============

Here I describe how you can split a Git repository without losing the associated
history.

Scenario and goals
------------------

We want to split out from the Jupyter tutorial repository the part that deals
with visualising the data: ``docs/viz/``. The challenge is that the history for
the ``docs/viz/`` directory is mixed with other changes. Therefore, we first
clone the same repository twice:

.. code-block:: console

    $ git clone git@github.com:veit/jupyter-tutorial.git
    Klone nach 'jupyter-tutorial'...
    $ git clone git@github.com:veit/jupyter-tutorial.git pyviz-tutorial
    Klone nach 'pyviz-tutorial' ...

The next step is to filter out the unwanted histories from each of the two
repos. To rewrite the history and keep only those commits that actually affect
your content of a particular subfolder, we use `git-filter-repo
<https://github.com/newren/git-filter-repo>`_:

.. code-block:: console

    $ curl https://raw.githubusercontent.com/newren/git-filter-repo/main/git-filter-repo -o git-filter-repo
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  161k  100  161k    0     0   578k      0 --:--:-- --:--:-- --:--:--  584k

    $ cd pyviz-tutorial
    $ python3 ../git-filter-repo --path docs/viz

The only thing left to do now is to adjust the remote URL:

.. code-block:: console

    $ git remote add origin git@github.com:veit/pyviz-tutorial.git
    $ git push -u origin main

For our Jupyter tutorial repository, we now invert the selected path:

.. code-block::

    $ cd jupyter-tutorial
    $ python3 ../git-filter-repo --invert-paths --path docs/viz
    $ git remote add origin git@github.com:veit/jupyter-tutorial.git
    $ git push -f -u origin main
