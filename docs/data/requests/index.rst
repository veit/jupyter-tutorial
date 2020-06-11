Web-API
=======

Ein **A** pplication **P** rogramming **I** nterface (API) ist eine
Schnittstelle zum programmgesteuerten Arbeiten mit einer bestimmten Anwendung.
Eine API muss nicht zwingend das Web einbeziehen. Viele lokale Anwendungen auf
eurem Computer verfügen über eigene APIs, sodass wir über Python oder eine
andere Sprache mit ihm interagieren können. In unserem nächsten Beispiel
erhalten wir die Daten jedoch über eine Web-API, d.h. über HTTP-Requests und
-Responses. Viele aktuelle API sind genauer spezifiziert als sog. `REST
<https://de.wikipedia.org/wiki/Representational_State_Transfer>`_-APIs, d.h.,
sie kommunizieren über das HTTP/HTTPS-Protokoll mit den Consumers:
HTTP-Requests verwenden meist die GET- oder POST-Methode sowie in der URL
definierte Parameter, um die Anfrage zu stellen. Die HTTP-Responses haben eine
ähnliche Struktur, enthalten jedoch zusätzlich noch einen HTTP-Statuscode.

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    requests.ipynb
    module.ipynb

