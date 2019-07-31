Konfiguration
=============

JupyterHub-Konfiguration
------------------------

.. code-block:: console

    $  pipenv run jupyterhub --generate-config
    Writing default config to: jupyterhub_config.py

.. seealso::

   * :doc:`JupyterHub Configuration Basics <jupyterhub:getting-started/index>`
   * :doc:`JupyterHub Networking basics <jupyterhub:getting-started/networking-basics>`

System service für JupyterHub
-----------------------------

#. Ermitteln des *Python Virtual Environment*:

   .. code-block:: console

    $ cd ~/jupyterhub
    $ pipenv --venv
    /srv/jupyter/.local/share/virtualenvs/jupyterhub-aFv4x91W
 
#. Konfigurieren von ``/etc/systemd/system/jupyterhub.service`` und
   ``/lib/systemd/system/jupyterhub.service``:

   .. code-block:: ini

    [Unit]
    Description=Jupyterhub

    [Service]
    User=root
    Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/srv/jupyter/.local/share/virtualenvs/jupyterhub-aFv4x91W/bin"
    ExecStart=/srv/jupyter/.local/share/virtualenvs/jupyterhub-aFv4x91W/bin/jupyterhub -f /srv/jupyter/jupyterhub/jupyterhub_config.py

    [Install]
    WantedBy=multi-user.target

#. Laden der Konfiguration

   mit:

   .. code-block:: console

    # systemctl daemon-reload

#. Der JupyterHub lässt sich verwalten mit:

   .. code-block:: console

    # systemctl <start|stop|status> jupyterhub

#. Um sicherzustellen, dass der Dienst auch bei einem Systemstart mitgeladen
   wird, wird folgendes aufgerufen:

TLS-Verschlüsselung
-------------------

Da JupyterHub eine Authentifizierung beinhaltet und die Ausführung von
beliebigem Code erlaubt, sollte es nicht ohne SSL (HTTPS) ausgeführt werden.
Dazu muss ein offizielles, vertrauenswürdiges SSL-Zertifikat erstellt werden.
Nachdem ihr einen Schlüssel und ein Zertifikat erhalten und installiert habt,
konfiguriert ihr jedoch nicht das JupyterHub selbst sondern den vorgeschalteten
Apache Webserver.

#. Hierfür werden zunächst die Zusatzmodule aktiviert mit

   .. code-block:: apacheconf

    # a2enmod ssl rewrite proxy proxy_http proxy_wstunnel

#. Anschließend kann der VirtualHost in
   ``/etc/apache2/sites-available/jupyter.ise.fhg.de.conf`` konfiguriert
   werden mit

   .. code-block:: console

     # redirect HTTP to HTTPS
     <VirtualHost 172.31.50.170:80>
         ServerName jupyter.ise.fhg.de
         ServerAdmin webmaster@localhost

         ErrorLog ${APACHE_LOG_DIR}/jupyter.ise.fhg.de_error.log
         CustomLog ${APACHE_LOG_DIR}/jupyter.ise.fhg.de_access.log combined

         Redirect / https://jupyter.ise.fhg.de/
     </VirtualHost>

     <VirtualHost 172.31.50.170:443>
       ServerName jupyter.ise.fhg.de
       ServerAdmin webmaster@localhost

       # configure SSL
       SSLEngine On
       SSLCertificateFile /etc/ssl/certs/jupyter.ise.fhg.de_cert.pem
       SSLCertificateKeyFile /etc/ssl/private/jupyter.ise.fhg.de_sec_key.pem
       SSLCertificateChainFile /etc/ssl/certs/fhg_dfn_chain.pem
       SSLProtocol All -SSLv2 -SSLv3
       SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH

       # Use RewriteEngine to handle websocket connection upgrades
       RewriteEngine On
       RewriteCond %{HTTP:Connection} Upgrade [NC]
       RewriteCond %{HTTP:Upgrade} websocket [NC]
       RewriteRule /(.*) ws://127.0.0.1:8000/$1 [P,L]

       <Location "/">
         # preserve Host header to avoid cross-origin problems
         ProxyPreserveHost on
         # proxy to JupyterHub
         ProxyPass         http://127.0.0.1:8000/
         ProxyPassReverse  http://127.0.0.1:8000/
       </Location>

       ErrorLog ${APACHE_LOG_DIR}/jupyter.ise.fhg.de_error.log
       CustomLog ${APACHE_LOG_DIR}/jupyter.ise.fhg.de_access.log combined
     </VirtualHost>

#. Dieser VirtualHost wird aktiviert mit

   .. code-block:: console

     # a2ensite jupyter.ise.fhg.de.conf

#. Schließlich wird der Status des Apache-Webserver überprüft mit

   .. code-block:: console

    # systemctl status apache2
    ● apache2.service - The Apache HTTP Server
       Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
       Active: active (running) (Result: exit-code) since Mon 2019-03-25 16:50:26 CET; 1 day 22h ago
      Process: 31773 ExecReload=/usr/sbin/apachectl graceful (code=exited, status=0/SUCCESS)
     Main PID: 20273 (apache2)
        Tasks: 55 (limit: 4915)
       CGroup: /system.slice/apache2.service
               ├─20273 /usr/sbin/apache2 -k start
               ├─31779 /usr/sbin/apache2 -k start
               └─31780 /usr/sbin/apache2 -k start

    Mar 27 06:25:01 sxv13130.ise.fhg.de systemd[1]: Reloaded The Apache HTTP Server.

Cookie-Secret
-------------

Das Cookie secret ist zum Verschlüsseln der Browser-Cookies, die zur
Authentifizierung verwendet werden.

#. Das Cookie-Secret kann z.B. erstellt werden mit

   .. code-block:: console

    $ openssl rand -hex 32 > /srv/jupyterhub/venv/jupyterhub_cookie_secret

#. Die Datei sollte weder für ``group`` noch für ``anonymous`` lesbar sein:

   .. code-block:: console

    $ chmod 600 /srv/jupyterhub/venv/jupyterhub_cookie_secret

#. Schließlich wird es in die ``jupyterhub_config.py``-Datei eingetragen:

   .. code-block:: python

    c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

Proxy authentication token
--------------------------

Der Hub authentifiziert seine Anforderungen an den Proxy unter Verwendung
eines geheimen Tokens, auf das sich der Hub und der Proxy einigen.
Üblicherweise muss der Proxy authentication token nicht festgelegt werden,
da der Hub selbst einen zufälligen Schlüssel generiert. Dies bedeutet, dass
der Proxy jedes Mal neu gestartet werden muss sofern der Proxy nicht ein
Unterprozess des Hubs ist.

#. Alternativ kann Der Wert z.B. generiert werden mit

   .. code-block:: console

    $ openssl rand -hex 32

#. Anschließend kann er in der Konfigurationsdatei eingetragen werde, z.B. mit

   .. code-block:: python

    c.JupyterHub.proxy_auth_token = '18a0335b7c2e7edeaf7466894a32bea8d1c3cff4b07860298dbe353ecb179fc6'

