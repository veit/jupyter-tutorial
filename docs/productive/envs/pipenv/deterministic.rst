Deterministische Builds
=======================

Ihr müsst nur spezifizieren, was ihr wollt:

Mit ``pipenv install requests`` wird z.B. ein ``Pipfile`` erzeugt wie das
folgende:

.. code-block:: ini

    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"

    [packages]
    requests = "*"

    [dev-packages]

    [requires]
    python_version = "3.6"

Die zugehörige ``Pipfile.lock``-Datei spezifiziert jedoch die Pakete exakt, z.B.:

.. code-block:: json

    {
        "default": {
            "requests": {
                "hashes": [
                    "sha256:63b52e3c866428a224f97cab011de738c36aec0185aa91cfacd418b5d58911d1",
                    "sha256:ec22d826a36ed72a7358ff3fe56cbd4ba69dd7a6718ffd450ff0e9df7a47ce6a"
                ],
                "index": "pypi",
                "version": "==2.19.1"
            },
            "urllib3": {
                "hashes": [
                    "sha256:a68ac5e15e76e7e5dd2b8f94007233e01effe3e50e8daddf69acfd81cb686baf",
                    "sha256:b5725a0bd4ba422ab0e66e89e030c806576753ea3ee08554382c14e685d117b5"
                ],
                "markers": "python_version != '3.2.*' and python_version != '3.1.*' and python_version < '4' and python_version != '3.3.*' and python_version >= '2.6' and python_version != '3.0.*'",
                "version": "==1.23"
            }
        },
        "develop": {}
    }

``Pipfile.lock`` spezifiziert auch alle Abhängigkeiten eures Projekts, wobei die
Hashwerte der heruntergeladenen Dateien gespeichert werden. Dies soll
wiederholbare und deterministische Builds gewährleisten.

