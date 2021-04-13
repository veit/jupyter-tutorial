Alembic
=======

`Alembic <https://alembic.sqlalchemy.org/>`_ is based on SQLAlchemy and serves
as a database migration tool with the following functions:

* ``ALTER`` statements to a database to change the structure of tables and other
  constructs
* System for creating migration scripts. Optionally, the sequence of steps for
  the downgrade can also be specified.
* The scripts are executed in a specific order.

Create migration environment
----------------------------

The Migration Environment is a directory that is specific to a particular
application. It is created with the Alembic ``ini`` command and then managed
along with the application’s source code.

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

The structure of such a migration environment can e.g. look like this::

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

Templates
---------
Alembic includes a number of templates that can be displayed with list::

    $ alembic list_templates
    Available templates:

    generic - Generic single-database configuration.
    multidb - Rudimentary multi-database configuration.
    pylons - Configuration that reads from a Pylons project environment.

    Templates are used via the 'init' command, e.g.:

      alembic init --template pylons ./scripts

Configure ``ini`` file
----------------------

The file created with the ``generic`` template looks like this::

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
    Replacement variable for creating absolute paths
``file_template``
    This is the naming scheme used to generate new migration files. The
    available variables include:

    ``%%(rev)s``
        Revision ID
    ``%%(slug)s``
        Abbreviated revision message
    ``%%(year)d, %%(month).2d, %%(day).2d, %%(hour).2d, %%(minute).2d, %%(second).2d``
        Creation time

Create a migration script
-------------------------

A new revision can be created with::

    $ alembic revision -m "create account table"
    Generating /path/to/yourproject/alembic/versions/1975ea83b712_create_account_table.py...done

Then the file ``1975ea83b712_create_account_table.py`` looks like this::

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
    Variable that tells Alembic in which order the migrations should be carried
    out, e.g.::

        # revision identifiers, used by Alembic.
        revision = 'ae1027a6acf'
        down_revision = '1975ea83b712'

``upgrade``, ``downgrade``
    e.g.::

        def upgrade():
            op.create_table(
                'account',
                sa.Column('id', sa.Integer, primary_key=True),
                sa.Column('name', sa.String(50), nullable=False),
                sa.Column('description', sa.Unicode(200)),
            )

        def downgrade():
            op.drop_table('account')

    ``create_table()`` and ``drop_table()`` are Alembic directives. You can get
    an overview of all Alembic directives in the `Operation Reference
    <https://alembic.sqlalchemy.org/en/latest/ops.html#ops>`_.

Run migration
-------------

First migration::

    $ alembic upgrade head
    INFO  [alembic.context] Context class PostgresqlContext.
    INFO  [alembic.context] Will assume transactional DDL.
    INFO  [alembic.context] Running upgrade None -> 1975ea83b712

We can also refer directly to revision numbers::

    $ alembic upgrade ae1

Relative migrations can also be initiated::

    $ alembic upgrade +2

or::

    $ alembic downgrade -1

or::

$ alembic upgrade ae10+2

Display Information
-------------------

Current version::

        $ alembic current
        INFO  [alembic.context] Context class PostgresqlContext.
        INFO  [alembic.context] Will assume transactional DDL.
        Current revision for postgresql://scott:XXXXX@localhost/test: 1975ea83b712 -> ae1027a6acf (head), Add a column

History::

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

    The history can also be displayed more specifically::

        $ alembic history -r1975ea:ae1027

    or::

        $ alembic history -r-3:current

    or::

        $ alembic history -r1975ea:

.. seealso::
   `Auto Generating Migrations <https://alembic.sqlalchemy.org/en/latest/autogenerate.html>`_
