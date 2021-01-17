gRPC-Example
============

By default, gRPC uses :doc:`serialisation-formats/protobuf` for serialising
data, although it also works with other data formats such as JSON.

Define the data structure
-------------------------
The first step when working with protocol buffers is to define the structure for
the data you want to serialise in a ``.proto`` file. Protocol buffer data is
structured as *messages*, where each message is a small logical record of
information containing a series of name-value pairs called *fields*. Here’s a
simple example :download:`person.proto`:

.. code-block:: proto

    syntax = "proto3";

    message Person {
      int32 id = 1;
      string name = 2;
      string email = 3;
    }

After you have defined your data structure, you use the protocol buffer compiler
``protoc`` to generate data access classes in your preferred languages. These
provide simple accessors for each field, like ``name()`` and ``set_name()``, as
well as methods to serialise the whole structure. For example, if your language
is Python, running the compiler on the example above will generate a class
called ``Person``. You can then use this class in your application to populate,
serialise, and retrieve ``Person`` protocol buffer messages.

Define the gRPC service
-----------------------
gRPC services are also defined in the ``.proto`` files, with RPC method
parameters and return types specified as protocol buffer messages:

.. code-block:: proto

    syntax = "proto3";

    // The salutation service definition.
    service Salutation {
      rpc Salutation (SalutationRequest) returns (SalutationReply) {}
    }

    // The request message contains the person’s id.
    message SalutationRequest {
      string name = 1;
    }

    // The response message contains the person’s name
    message SalutationReply {
      string message = 2;
    }

Generate the gRPC Code
----------------------

.. code-block:: console

    $ pipenv install grpcio grpcio-tools
    $ pipenv run python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. person.proto

This generates two files:

:download:`person_pb2.py`
    which contains the generated request and response classes
:download:`person_pb2_grpc.py`
    which contains the generated client and server classes.

Update the server
-----------------

Now we can define our ``Salutation`` in :download:`person_server.py`:

.. code-block:: python

    from concurrent import futures
    import logging

    import grpc

    import person_pb2
    import person_pb2_grpc


    class Salutation(person_pb2_grpc.SalutationServicer):

        def Salutation(self, request, context):
            return person_pb2.SalutationReply(message='Hello, %s!' % request.name)


    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        person_pb2_grpc.add_SalutationServicer_to_server(Salutation(), server)
        server.add_insecure_port('[::]:8081')
        server.start()
        server.wait_for_termination()


    if __name__ == '__main__':
        logging.basicConfig()
        serve()

Update the client
-----------------

We create :download:`person_client.py` with the ``run`` method:

.. code-block:: python

    import logging

    import grpc

    import person_pb2
    import person_pb2_grpc


    def run():
        channel = grpc.insecure_channel('localhost:8081')
        stub = person_pb2_grpc.SalutationStub(channel)
        response = stub.Salutation(person_pb2.SalutationRequest(name='you'))
        print("Person client received: " + response.message)


    if __name__ == '__main__':
        logging.basicConfig()
        run()

Run client and server
---------------------

#. Run the server:

   .. code-block:: console

        $ pipenv run python person_server.py

#. Run the client from another terminal:

   .. code-block:: console

        $ pipenv run python person_client.py
        Person client received: Hello, you!
