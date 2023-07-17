Configuration
=============

JupyterHub configuration
------------------------

Create configuration file:

.. code-block:: console

    $  pipenv run jupyterhub --generate-config
    Writing default config to: jupyterhub_config.py

.. seealso::

   * :doc:`JupyterHub Configuration Basics
     <jupyterhub:tutorial/getting-started/config-basics>`
   * :doc:`JupyterHub Networking basics
     <jupyterhub:tutorial/getting-started/networking-basics>`

System Service for JupyterHub
-----------------------------

#. Determine the Python virtual environment:

   .. code-block:: console

    $ cd ~/jupyter-tutorial
    $ pipenv --venv
    /srv/jupyter/.local/share/virtualenvs/jupyter-tutorial-aFv4x91W

#. Configure the absolute path to :file:`jupyterhub-singleuser` in the
   :file:`jupyterhub_config.py` file:

   .. code-block:: python

    c.Spawner.cmd = ['/srv/jupyter/.local/share/virtualenvs/jupyter-tutorial-aFv4x91/bin/jupyterhub-singleuser']

#. Add a new systemd unit file :file:`/etc/systemd/system/jupyterhub.service`
   with the command:

   .. code-block:: console

    $ sudo systemctl edit --force --full jupyterhub.service

   Add your corresponding Python environment.

   .. code-block:: ini

    [Unit]
    Description=Jupyterhub

    [Service]
    User=root
    Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/srv/jupyter/.local/share/virtualenvs/jupyterhub-aFv4x91W/bin"
    ExecStart=/srv/jupyter/.local/share/virtualenvs/jupyterhub-aFv4x91W/bin/jupyterhub -f /srv/jupyter/jupyterhub_env/jupyterhub_config.py

    [Install]
    WantedBy=multi-user.target

#. Loading the configuration with:

   .. code-block:: console

    $ sudo systemctl daemon-reload

#. The JupyterHub can be managed with:

   .. code-block:: console

    $ sudo systemctl <start|stop|status> jupyterhub

#. To ensure that the service is also loaded during a system start, the
   following is called:

   .. code-block:: console

    $ sudo systemctl enable jupyterhub.service
    Created symlink /etc/systemd/system/multi-user.target.wants/jupyterhub.service → /etc/systemd/system/jupyterhub.service.

#. To be able to use the ``jupyterhub-singleuser`` and start your own server,
   the ix users must be entered in the ``jupyter`` group, for example with
   :samp:`usermod -aG jupyter {VEIT}`.


Since JupyterHub includes authentication and allows the execution of any code,
it should not be executed without SSL (HTTPS). To do this, an official,
trustworthy SSL certificate must be created. After you have received and
installed a key and a certificate, you don’t configure the JupyterHub itself,
but the upstream Apache web server.

#. For this purpose, the additional modules are first activated with

   .. code-block:: apacheconf

    # a2enmod ssl rewrite proxy proxy_http proxy_wstunnel

#. Then the VirtualHost can be configured in
   ``/etc/apache2/sites-available/jupyter.cusy.io.conf``

   .. code-block:: console

     # redirect HTTP to HTTPS
     <VirtualHost 172.31.50.170:80>
         ServerName jupyter.cusy.io
         ServerAdmin webmaster@cusy.io

         ErrorLog ${APACHE_LOG_DIR}/jupyter.cusy.io_error.log
         CustomLog ${APACHE_LOG_DIR}/jupyter.cusy.io_access.log combined

         Redirect / https://jupyter.cusy.io/
     </VirtualHost>

     <VirtualHost 172.31.50.170:443>
       ServerName jupyter.cusy.io
       ServerAdmin webmaster@cusy.io

       # configure SSL
       SSLEngine On
       SSLCertificateFile /etc/ssl/certs/jupyter.cusy.io_cert.pem
       SSLCertificateKeyFile /etc/ssl/private/jupyter.cusy.io_sec_key.pem
       # for an up-to-date SSL configuration see e.g.
       # https://ssl-config.mozilla.org/

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

       ErrorLog ${APACHE_LOG_DIR}/jupyter.cusy.io_error.log
       CustomLog ${APACHE_LOG_DIR}/jupyter.cusy.io_access.log combined
     </VirtualHost>

#. This VirtualHost is activated with

   .. code-block:: console

     # a2ensite jupyter.cusy.io.conf

#. Finally, the status of the Apache web server is checked with

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

    Mar 27 06:25:01 jupyter.cusy.io systemd[1]: Reloaded The Apache HTTP Server.

Cookie Secret
-------------

The cookie secret is used to encrypt the browser cookies that are used for
authentication.

#. The cookie secret can e.g. be created with

   .. code-block:: console

    $ openssl rand -hex 32 > /srv/jupyterhub/venv/jupyterhub_cookie_secret

#. The file should not be readable by either  ``group`` or ``anonymous``:

   .. code-block:: console

    $ chmod 600 /srv/jupyterhub/venv/jupyterhub_cookie_secret

#. Finally it will be entered in the :file:`jupyterhub_config.py` file:

   .. code-block:: python

    c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

Proxy authentication token
--------------------------

The hub authenticates its requests to the proxy using a secret token that the
hub and proxy agree on. Usually, the proxy authentication token does not need to
be set, as the hub itself generates a random key. This means that the proxy has
to be restarted every time unless the proxy is a subprocess of the hub.

#. Alternatively, the value can e.g. can be generated with

   .. code-block:: console

    $ openssl rand -hex 32

#. It can then be entered in the configuration file, for example with

   .. code-block:: python

    c.JupyterHub.proxy_auth_token = '18a0335b7c2e7edeaf7466894a32bea8d1c3cff4b07860298dbe353ecb179fc6'
