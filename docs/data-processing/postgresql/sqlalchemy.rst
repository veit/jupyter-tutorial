SQLAlchemy
==========

`SQLAlchemy <https://www.sqlalchemy.org/>`_ is a Python-SQL-Toolkit and
object-relational mapper.

SQLAlchemy is known for its ORM, whereby it provides different patterns for
object-relational mapping, whereby classes can be mapped to the database in
different ways. The object model and the database schema are cleanly decoupled
from the start.

SQLAlchemy differs fundamentally from other ORMs, as SQL and details of the
object relation are not abstracted away: all processes are represented as a
collection of individual tools.

SQLAlchemy supports PostgreSQL as well as other dialects of relational
databases:

+---------------+-------------------+---------------+-------------------+
| Dialects      | Python package    | import        | Docs              |
+===============+===================+===============+===================+
| postgresql    | psycopg2-binary   | psycopg2      | `Installation`_   |
+---------------+-------------------+---------------+-------------------+
| mysql         | mysqlclient       | MySQLdb       | `README`_         |
+---------------+-------------------+---------------+-------------------+
| mssql         | pyodbc            | pyodbc        | `Wiki`_           |
+---------------+-------------------+---------------+-------------------+
| oracle        | cx_oracle         | cx_Oracle     | `cx_Oracle`_      |
+---------------+-------------------+---------------+-------------------+

.. _`Installation`: https://www.psycopg.org/docs/install.html
.. _`README`: https://github.com/PyMySQL/mysqlclient#readme
.. _`Wiki`: https://github.com/mkleehammer/pyodbc/wiki
.. _`cx_Oracle`: https://oracle.github.io/python-cx_Oracle/

Database connection
-------------------

::

    from sqlalchemy import create_engine
    engine = create_engine('postgresql:///example', echo=True)

Data model
----------

::

    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship

    Base = declarative_base()

    class Address(Base):
        __tablename__ = 'address'

        id = Column(Integer, primary_key=True)
        street = Column(String)
        zipcode = Column(String)
        country = Column(String, nullable=False)

    class Contact(Base):
        __tablename__ = 'contact'

        id = Column(Integer, primary_key=True)

     firstname = Column(String, nullable=False)
     lastname = Column(String, nullable=False)
     email = Column(String, nullable=False)
     address_id = Column(Integer, ForeignKey(Address.id), nullable=False)
     address = relationship('Address')

Create tables
-------------

::

    Base.metadata.create_all(engine)

Create Session
--------------

::

    session = Session(engine)
    address = Address(street='Birnbaumweg 10', zipcode='79115', country='Germany')

    contact = Contact(
        firstname='Veit', lastname='Schiele',
        email='veit@cusy.io',
        address=address
    )

    session.add(contact)
    session.commit()

Read
----

::

    contact =
    session.query(Contact).filter_by(email='veit@cusy.io').first()
    print(contact.firstname)

    contacts = session.query(Contact).all()
    for contact in contacts:
        print(contact.firstname)

    contacts =
    session.query(Contact).filter_by(email='veit@cusy.io').all()
    for contact in contacts:
        print(contact.firstname)

Update
------

::

    contact = session.query(Contact) \
        .filter_by(email='veit@cusy.io').first()
    contact.email = ‘info@veit-schiele.de'
    session.add(contact)
    session.commit()

Delete
------

::

    contact = session.query(Contact) \
       .filter_by(email='info@veit-schiele.de').first()
    session.delete(contact)
    session.commit()

Extensions
----------

`SQLAlchemy-Continuum <https://sqlalchemy-continuum.readthedocs.io/en/latest/>`_
    Versioning and revision extension for SQLAlchemy
`SQLAlchemy-Utc <https://github.com/spoqa/sqlalchemy-utc>`_
    SQLAlchemy type for storing `datetime.datetime` values
`SQLAlchemy-Utils <https://sqlalchemy-utils.readthedocs.io/en/latest/>`_
    Various utility functions, new data types and utilities for SQLAlchemy
`DEPOT <https://depot.readthedocs.io/en/latest/>`_
    Framework for easy storage and retrieval of files in web applications
`SQLAlchemy-ImageAttach <https://sqlalchemy-imageattach.readthedocs.io/>`_
    RSQLAlchemy extension for attaching images to entity objects
`SQLAlchemy-Searchable <https://sqlalchemy-searchable.readthedocs.io/en/latest/>`_
    Full-text searchable models for SQLAlchemy

.. seealso::

   * `Awesome SQLAlchemy <https://github.com/dahlia/awesome-sqlalchemy>`_
