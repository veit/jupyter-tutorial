Vim and IDE integration
=======================

Vim
---

To recognize DVC files in Vim as YAML, you should add the following in
``~/.vimrc``::

    " DVC
    autocmd! BufNewFile,BufRead Dvcfile,*.dvc setfiletype yaml


Visual Studio Code
------------------

For `Visual Studio Code <https://code.visualstudio.com>`_, there is an extension
for `DVC <https://marketplace.visualstudio.com/items?itemName=Iterative.dvc>`_
that can be downloaded from the Visual Studio Marketplace
<https://marketplace.visualstudio.com>`_.

IntelliJ IDEs
-------------

`intellij-dvc
<https://plugins.jetbrains.com/plugin/11368-data-version-control-dvc-support>`_
is a plugin for IntelliJ IDEs including PyCharm, IntelliJ IDEA and CLion. It can
be downloaded from the `JetBrains Plugins-Repository
<https://plugins.jetbrains.com/plugin/11368-data-version-control-dvc-support/>`_.
