Object-relational mapping
=========================

    «Object-relational mapping (…) in computer science is a programming
    technique for converting data between incompatible type systems using
    object-oriented programming languages.»[#]_

.. [#] `Wikipedia: relational mapping
    <https://en.wikipedia.org/wiki/Object-relational_mapping>`_

In the simplest case, classes are mapped to tables, with each object
corresponding to a table row and each attribute to a table column.

There are essentially three different methods of mapping inheritance
hierarchies:

*Single Table*
    One table is created for each inheritance hierarchy, with all attributes of
    the base class and all classes derived from it being stored in a common
    table.
*Joined Table* or *Class Table*
    A table is created for each subclass and a further table for each subclass
    derived from it.
*Table per Class* or *Concrete Table*
    The attributes of the abstract base class are included in the tables for the
    specific subclasses. However, it is not possible to determine instances of
    different classes with one query.
