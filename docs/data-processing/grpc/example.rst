gRPC-Example
============

By default, gRPC uses :doc:`../serialisation-formats/protobuf` for serialising
data, although it also works with other data formats such as JSON.

Define the data structure
-------------------------
The first step when working with protocol buffers is to define the structure for
the data you want to serialise in a ``.proto`` file. Protocol buffer data is
structured as *messages*, where each message is a small logical record of
information containing a series of name-value pairs called *fields*. Here’s a
simple example ``accounts.proto``:

.. literalinclude:: accounts.proto
   :language: proto
   :lines: 1-6

.. warning::
    Please note that you should not simply use ``uint32`` for user or group IDs,
    as these would be far too easy to guess. You can use an `RFC 4122
    <https://tools.ietf.org/html/rfc4122>`_-compliant implementation for this
    purpose. You can find a corresponding protobuf configuration in
    :download:`rfc4122.proto`.

After you have defined your data structure, you use the protocol buffer compiler
``protoc`` to generate descriptors in your preferred languages. These provide
simple accessors for each field, as well as methods to serialise the whole
structure. For example, if your language is Python, running the compiler on the
example above will generate declarators you can then use in your application to
populate, serialise, and retrieve protocol buffer messages.

Define the gRPC service
-----------------------
gRPC services are also defined in the ``.proto`` files, with RPC method
parameters and return types specified as protocol buffer messages:

.. literalinclude:: accounts.proto
   :language: proto
   :lines: 8-

Generate the gRPC Code
----------------------

.. code-block:: console

    $ pipenv install grpcio grpcio-tools
    $ pipenv run python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. person.proto

This generates two files:

:download:`accounts_pb2.py`
    which contains the generated request and response classes.
:download:`accounts_pb2_grpc.py`
    which contains the generated client and server classes.

Update the server
-----------------

Now we can define our ``Salutation`` in :download:`accounts_server.py`:

.. literalinclude:: accounts_server.py
   :language: python

Update the client
-----------------

We create :download:`accounts_client.py` with the ``run`` method:

.. literalinclude:: accounts_client.py
   :language: python

Run client and server
---------------------

#. Run the server:

   .. code-block:: console

        $ pipenv run python accounts_server.py

#. Run the client from another terminal:

   .. code-block:: console

    $ pipenv run python accounts_client.py
    Account created: tom
    account {
      account_id: 1
      account_name: "veit"
    }

    account {
      account_id: 2
      account_name: "andy"
    }
