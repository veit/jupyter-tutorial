Alembic
=======

`Alembic <https://alembic.sqlalchemy.org/>`_ basiert auf SQLAlchemy und dient als
Datenbankmigrationswerkzeug mit den folgenden Funktionen:

* ``ALTER``-Anweisungen an eine Datenbank ausgeben um die Strukturen von
  Tabellen und anderen Konstrukten zu ändern
* System zum Erstellen von Migrationsskripten. Optional kann auch die
  Reihenfolge der Schritte für das Downgrade angegeben werden.
* Die Skripte werden in einer bestimmten Reihenfolge ausgeführt.

Migrationsumgebung erstellen
----------------------------

Das Migration Environment ist ein Verzeichnis, das für eine bestimmte Anwendung
spezifisch ist. Sie wird mit dem ``ini``-Befehl von Alembic erstellt und
anschließend zusammen mit dem Quellcode der Anwendung verwaltet.

::

    $ cd myrproject
    $ alembic init alembic
    Creating directory /path/to/myproject/alembic...done
    Creating directory /path/to/myproject/alembic/versions...done
    Generating /path/to/myproject/alembic.ini...done
    Generating /path/to/myproject/alembic/env.py...done
    Generating /path/to/myproject/alembic/README...done
    Generating /path/to/myproject/alembic/script.py.mako...done
    Please edit configuration/connection/logging settings in
    '/path/to/myproject/alembic.ini' before proceeding.

Die Struktur eines solchen Migrationsumgebung kann später dann  z.B. so
aussehen:

::

    myproject/
    └── alembic
        ├── alembic.ini
        ├── env.py
        ├── README
        ├── script.py.mako
        └── versions
            ├── 2b1ae634e5cd_add_order_id.py
            ├── 3512b954651e_add_account.py
            └── 3adcc9a56557_rename_username_field.py

Vorlagen
--------

Alembic erhält eine Reihe von Vorlagen, die mit ``list`` angezeigt werden
können::

    $ alembic list_templates
    Available templates:

    generic - Generic single-database configuration.
    multidb - Rudimentary multi-database configuration.
    pylons - Configuration that reads from a Pylons project environment.

    Templates are used via the 'init' command, e.g.:

      alembic init --template pylons ./scripts

ini-Datei konfigurieren
-----------------------

Die mit der ``generic``-Vorlage erstellte Datei sieht folgendermaßen aus::

    # A generic, single database configuration.

    [alembic]
    # path to migration scripts
    script_location = alembic

    # template used to generate migration files
    # file_template = %%(rev)s_%%(slug)s

    # timezone to use when rendering the date
    # within the migration file as well as the filename.
    # string value is passed to dateutil.tz.gettz()
    # leave blank for localtime
    # timezone =

    # max length of characters to apply to the
    # "slug" field
    #truncate_slug_length = 40

    # set to 'true' to run the environment during
    # the 'revision' command, regardless of autogenerate
    # revision_environment = false

    # set to 'true' to allow .pyc and .pyo files without
    # a source .py file to be detected as revisions in the
    # versions/ directory
    # sourceless = false

    # version location specification; this defaults
    # to alembic/versions.  When using multiple version
    # directories, initial revisions must be specified with --version-path
    # version_locations = %(here)s/bar %(here)s/bat alembic/versions

    # the output encoding used when revision files
    # are written from script.py.mako
    # output_encoding = utf-8

    sqlalchemy.url = driver://user:pass@localhost/dbname

    # Logging configuration
    [loggers]
    keys = root,sqlalchemy,alembic

    [handlers]
    keys = console

    [formatters]
    keys = generic

    [logger_root]
    level = WARN
    handlers = console
    qualname =

    [logger_sqlalchemy]
    level = WARN
    handlers =
    qualname = sqlalchemy.engine

    [logger_alembic]
    level = INFO
    handlers =
    qualname = alembic

    [handler_console]
    class = StreamHandler
    args = (sys.stderr,)
    level = NOTSET
    formatter = generic

    [formatter_generic]
    format = %(levelname)-5.5s [%(name)s] %(message)s
    datefmt = %H:%M:%S

``%(here)s``
    Ersetzungsvariable zum Erstellen absoluter Pfade
``file_template``
    Dies ist das Namensschema, das zum Generieren neuer Migrationsdateien
    verwendet wird. Zu den verfügbaren Variablen gehören:

    ``%%(rev)s``
        Revision-ID
    ``%%(slug)s``
        Verkürzte Revisionsnachricht
    ``%%(year)d, %%(month).2d, %%(day).2d, %%(hour).2d, %%(minute).2d, %%(second).2d``
        Erstellungszeitpunkt

Erstellen eines Migrationsskripts
---------------------------------

Eine neue Revision kann erstellt werden mit::

    $ alembic revision -m "create account table"
    Generating /path/to/yourproject/alembic/versions/1975ea83b712_create_account_table.py...done

Die Datei ``1975ea83b712_create_account_table.py`` sieht dann folgendermaßen aus::

    """create account table

    Revision ID: 1975ea83b712
    Revises:
    Create Date: 2018-12-08 11:40:27.089406

    """

    # revision identifiers, used by Alembic.
    revision = '1975ea83b712'
    down_revision = None
    branch_labels = None

    from alembic import op
    import sqlalchemy as sa

    def upgrade():
        pass

    def downgrade():
        pass

``down_revision``
    Variable, die Alembic mitteilt, in welcher Reihenfolge die Migrationen
    ausgeführt werden sollen, z.B.::

        # revision identifiers, used by Alembic.
        revision = 'ae1027a6acf'
        down_revision = '1975ea83b712'

``upgrade``, ``downgrade``
    z.B.::

        def upgrade():
            op.create_table(
                'account',
                sa.Column('id', sa.Integer, primary_key=True),
                sa.Column('name', sa.String(50), nullable=False),
                sa.Column('description', sa.Unicode(200)),
            )

        def downgrade():
            op.drop_table('account')

    ``create_table()`` und ``drop_table()`` sind Alembic-Direktiven. Einen
    Überblick über alle Alembic-Direktiven erhaltet ihr in der `Operation Reference
    <https://alembic.sqlalchemy.org/en/latest/ops.html#ops>`_.

Ausführen von Migration
-----------------------

Erste Migration::

    $ alembic upgrade head
    INFO  [alembic.context] Context class PostgresqlContext.
    INFO  [alembic.context] Will assume transactional DDL.
    INFO  [alembic.context] Running upgrade None -> 1975ea83b712

Wir können auch direkt auf Revisionsnummern verweisen::

    $ alembic upgrade ae1

Auch relative Migrationen können angestoßen werden::

    $ alembic upgrade +2

oder::

    $ alembic downgrade -1

oder::

$ alembic upgrade ae10+2

Informationen anzeigen
----------------------

Aktuelle Version
    ::

        $ alembic current
        INFO  [alembic.context] Context class PostgresqlContext.
        INFO  [alembic.context] Will assume transactional DDL.
        Current revision for postgresql://scott:XXXXX@localhost/test: 1975ea83b712 -> ae1027a6acf (head), Add a column

Historie
    ::

        $ alembic history --verbose

        Rev: ae1027a6acf (head)
        Parent: 1975ea83b712
        Path: /path/to/yourproject/alembic/versions/ae1027a6acf_add_a_column.py

            add a column

            Revision ID: ae1027a6acf
            Revises: 1975ea83b712
            Create Date: 2014-11-20 13:02:54.849677

        Rev: 1975ea83b712
        Parent: <base>
        Path: /path/to/yourproject/alembic/versions/1975ea83b712_add_account_table.py

            create account table

            Revision ID: 1975ea83b712
            Revises:
            Create Date: 2014-11-20 13:02:46.257104

    Die Historie kann auch spezifischer angezeigt werden::

        $ alembic history -r1975ea:ae1027

    oder::

        $ alembic history -r-3:current

    oder::

        $ alembic history -r1975ea:

.. seealso::
   `Auto Generating Migrations <https://alembic.sqlalchemy.org/en/latest/autogenerate.html>`_
