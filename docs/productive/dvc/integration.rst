Vim- und IDE-Integration
========================

Vim
---

Um DVC-Dateien in Vim als YAML zu erkennen, solltet ihr Folgendes in
``~/.vimrc`` hinzufügen::

    " DVC
    autocmd! BufNewFile,BufRead Dvcfile,*.dvc setfiletype yaml

IntelliJ IDEs
-------------

`intellij-dvc
<https://plugins.jetbrains.com/plugin/11368-data-version-control-dvc-support>`_
ist ein Plugin für IntelliJ IDEs einschließlich PyCharm, IntelliJ IDEA und
CLion. Es kann aus dem `JetBrains Plugins-Repository
<https://plugins.jetbrains.com/plugin/11368-dvc-support-poc>`_ heruntergeladen
werden.

