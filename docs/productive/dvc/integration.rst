Vim and IDE integration
=======================

Vim
---

To recognize DVC files in Vim as YAML, you should add the following in
``~/.vimrc``::

    " DVC
    autocmd! BufNewFile,BufRead Dvcfile,*.dvc setfiletype yaml

IntelliJ IDEs
-------------

`intellij-dvc
<https://plugins.jetbrains.com/plugin/11368-data-version-control-dvc-support>`_
is a plugin for IntelliJ IDEs including PyCharm, IntelliJ IDEA and CLion. It can
be downloaded from the `JetBrains Plugins-Repository
<https://plugins.jetbrains.com/plugin/11368-data-version-control-dvc-support/>`_.
