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

Erweiterungen
-------------

`SQLAlchemy-Continuum <https://sqlalchemy-continuum.readthedocs.io/en/latest/>`_
    Versionierungs- und Revisionserweiterung für SQLAlchemy 
`SQLAlchemy-Utc <https://github.com/spoqa/sqlalchemy-utc>`_
    SQLAlchemy-Typ zum Speichern von `datetime.datetime`-Werten
`SQLAlchemy-Utils <https://sqlalchemy-utils.readthedocs.io/en/latest/>`_
    Verschiedene Utility-Funktionen, neue Datentypen und Hilfsprogramme für
    SQLAlchemy
`DEPOT <https://depot.readthedocs.io/en/latest/>`_
    Framework zur einfachen Speicherung und Bereitstellung von Dateien in
    Webanwendungen
`SQLAlchemy-ImageAttach <https://sqlalchemy-imageattach.readthedocs.io/>`_
    SQLAlchemy-Erweiterung zum Anhängen von Bildern an Entitätsobjekte
`SQLAlchemy-Searchable <https://sqlalchemy-searchable.readthedocs.io/en/latest/>`_
    Im Volltext durchsuchbare Modelle für SQLAlchemy

.. seealso::

   * `Awesome SQLAlchemy <https://github.com/dahlia/awesome-sqlalchemy>`_
