Voilà vs. Panel
===============

A major difference between Panel and Voilà lies in the processing of the
notebooks: Voilà is based directly on the notebook format and transfers the
entire output to the Voilà dashboard, whereas in Panel the output of a notebook
cell must be explicitly declared as a panel object. Voilà therefore has the
advantage that existing notebooks can be used unchanged. However, if not all
notebook cells are to be transferred to the dashboard, two similar notebooks
must be maintained – one for `Literate Programming
<https://en.wikipedia.org/wiki/Literate_programming>`_ and one for the
dashboard. However, if `the inverted pyramid
<https://slides.cusy.io/data-visualisation/#/2/6/0>`_ is to be used for
storytelling in a dashboard, two notebooks are required in both cases.

Scalability
-----------

Voilà and Panel are based on `Tornado <https://www.tornadoweb.org/en/stable/>`_,
but they differ in that Voilà starts a new Jupyter kernel for each person, while
the Bokeh server serves multiple people with the same Python process. This
difference has two main effects:

* The overhead per person for a dashboard is much lower with the Bokeh server
  than with Voilà: After the libraries are imported, there is only a tiny
  overhead for creating each new session. For a session that imports pandas and
  Matplotlib, the overhead per user is about 75 MB, and the number of people a
  Voilà server can handle for a given application is reduced. Also, startup and
  data access times are usually slower.
* Since a Bokeh server shares a single process for multiple sessions, data or
  processing can also be shared between the different sessions if necessary.

Multi-page app
--------------

Voilà is not designed for multi-page applications while Panel offers several
options for creating multi-page apps, including :doc:`panel/pipelines` and
overview pages with a collection of independent dashboards and apps.

Authorisation and authentication
--------------------------------

Typically, the dashboard should not be used for authentication and
authorisation, but delegated to a service. `ContainDS Dashboards
<https://cdsdashboards.readthedocs.io/en/stable/>`_ is an example of a
:doc:`/hub/index` extension that does this dashboard-independently.
Authentication and authorisation can also be performed via a web server using
one of the following tools:

* `Traefik Forward Auth <https://github.com/thomseddon/traefik-forward-auth>`_
* `OAuth2 Proxy <https://oauth2-proxy.github.io/oauth2-proxy>`_
* `PyCasbin <https://github.com/casbin/pycasbin>`_

If you still want to let the dashboarding library do the authentication, there
are a few options of varying maturity:

* Panel is based on Bokeh, which provides authentication, and Panel ships with a
  number of OAuth providers, such as GitHub, GitLab, and Azure.

  .. seealso::
     `Configuring Authentication
     <https://panel.holoviz.org/how_to/authentication/index.html>`_

* Voilà can reuse authentication from :doc:`/hub/index`.

BI tool
-------

Both Voilà and Panel require programming knowledge in order to create
dashboards. However, `Lumen <https://github.com/holoviz/lumen>`_, which is based
on Panel, offers a promising BI-like user interface.
