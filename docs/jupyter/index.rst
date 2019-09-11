Jupyter
=======

.. graphviz::

    digraph decide_jupyter {
        graph [fontname = "Calibri", fontsize="16"];
        node [fontname = "Calibri", fontsize="16"];
        edge [fontname = "Calibri", fontsize="16"];
        tooltip="Wie entscheide ich, welche Jupyter-Pakete ich benötige?";
        // Top Level
        what [
            shape=diamond,
            label="Was wollt ihr machen?",
            tooltip="Jupyter bietet euch verschiedene Möglichkeiten, wie ihr die Notebooks nutzen könnt"]
        // Second Level
        jupyter [
            label="Jupyter",
            tooltip="Jupyter lokal installieren",
            target="_top",
            href="../jupyter/notebook/index.html"]
        hub [
            label="JupyterHub",
            tooltip="JupyterHub\ninstallieren",
            target="_top",
            href="../jupyter/jupyterhub/index.html"]
        nbconvert [
            label="nbconvert",
            tooltip="nbconvert installieren und nutzen",
            target="_top",
            href="../jupyter/nbconvert.html"]
        nbviewer [
            label="nbviewer",
            tooltip="nbviewer installieren und nutzen",
            target="_top",
            href="../jupyter/nbviewer.html"]
        kernels [
            label="Kernels",
            tooltip="Kernels installieren, anzeigen und starten",
            target="_top",
            href="../jupyter/kernels/install.html"]
        extensions [
            shape=plaintext,
            label=" ",
            tooltip="Notebook-Erweiterungen installieren"]
        embed [
            shape=plaintext,
            label="",
            tooltip="Notebooks in andere Anwendungen einbinden"]
        examples [
            label="Unternehmens-\nanwendungen",
            tooltip="Anwendungsbeispiele bei Netflix, Bloomberg etc.",
            target="_top",
            href="../jupyter/use-cases.html"]
        // 3rd Level
        widgets [
            label="Widgets",
            tooltip="ipywidgets installieren und nutzen",
            target="_top",
            href="../jupyter/ipywidgets/index.html"]
        extend [
            label="nbextensions",
            tooltip="Installieren und Verwenden verschiedener Notebook-Erweiterungen",
            target="_top",
            href="../jupyter/nbextensions/index.html"]
        dash [
            label="Dashboards",
            tooltip="Installieren und Verwenden von Dashboards",
            target="_top",
            href="../jupyter/dashboards/index.html"]
        html [
            label="HTML",
            tooltip="Einbinden von Notebooks in statisches HTML",
            target="_top",
            href="../jupyter/ipywidgets/embedding.html"]
        sphinx [
            label="Sphinx",
            tooltip="Einbinden von Notebooks in den Sphinx Document Generator",
            target="_top",
            href="../jupyter/nbsphinx.html"]
        // Edges
        what -> jupyter [label="Einzel-\nnutzer"]
        what -> hub [label="Team-\narbeit"]
        what -> nbconvert [label="Konvertieren"]
        nbconvert -> nbviewer [label="Konvertier-\nservice"]
        what -> kernels [label="Java, R,\nJulia etc."]
        what -> extensions [label="Notebook\nerweitern"]
        what -> embed [label="Notebooks\neinbetten"]
        what -> examples [label="Beispiele"]
        extensions -> {widgets extend dash}
        embed -> {html sphinx}
        // Arrangement
        {rank = same; what;}
        {rank = same; jupyter; hub; nbconvert; kernels; extensions; embed; examples;}
        {rank = same; widgets; extend; dash;}
        {rank = same; html; sphinx}
    }

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    notebook/index
    hub/index
    nbconvert
    nbviewer
    kernels/index
    ipywidgets/index
    nbextensions/index
    dashboards/index
    nbsphinx
    use-cases

