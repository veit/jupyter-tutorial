Git-Integration
===============

Wenn wir nun die Filter aus :doc:`tools` automatisiert beim Ein- und
Auschecken von Git anwenden wollen, könnt ihr dies für alle eure Git-Repositories
mit folgender Änderung in der Datei ``~/.gitconfig`` konfigurieren:

.. code-block:: ini

    [core]
    attributesfile = ~/.gitattributes

    [filter "nbstrip_jq"]
    clean = "jq --indent 1 \
            '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
            | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
            | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
            | .cells[].metadata = {} \
            '"
    smudge = cat
    required = true

… und dann für alle Git-Repositories in ``~/.gitattributes`` oder für
einzelne Repositories in der ``.gitattributes``-Datei des jeweiligen
Repositories:

.. code-block:: ini

    *.ipynb filter=nbstrip_jq

