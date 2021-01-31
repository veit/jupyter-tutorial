gRPC
====

gRPC is a modern, open source, high-performance remote procedure call (RPC)
framework. By default, gRPC uses :doc:`../serialisation-formats/protobuf` as the
Interface Definition Language (IDL) for describing both the service interface
and the structure of the payload messages. In gRPC, a client application can
directly call a method on a server application on a different machine as if it
were a local object, making it easier for you to create distributed applications
and services. As in many RPC systems, gRPC is based on the idea of defining a
service, specifying the methods that can be called remotely with their
parameters and return types. On the server side, the server implements this
interface and runs a gRPC server to handle client calls; on the client side, the
client has a stub that provides the same methods as the server.

.. graphviz::

    digraph grpc_concept {
        rankdir="LR";
        graph [fontname = "Calibri", fontsize="16", overlap=false];
        node [fontname = "Calibri", fontsize="16", style="bold", penwidth="5px"];
        edge [fontname = "Calibri", fontsize="16", style="bold", penwidth="5px"];
        tooltip="gRPC concept";

        // C++ service
        subgraph "cluster_cpp_service" {
            label="C++ Service";
            shape=box;
            style= "rounded, filled";
            color="#00FFFF";
            "grpc_server" [
                label="gRPC server",
                shape=box,
                style= "rounded, filled",
                color="#4da6ff"
                ];
            }

        // Python stub
        subgraph cluster_python_client {
            label="Python client";
            shape=box;
            style= "rounded, filled";
            color="#00FFFF";
            grpc_python_stub [
                label="gRPC Python stub",
                shape=box,
                style= "rounded, filled",
                color="#4da6ff"
                ];
            }

        // Android-Java stub
        subgraph cluster_android_java_client {
            label="Android-Java client";
            shape=box;
            style= "rounded, filled";
            color="#00FFFF";
            grpc_android_java_stub [
                label="gRPC Android-Java stub",
                shape=box,
                style= "rounded, filled",
                color="#4da6ff"
                ];
            }

        grpc_python_stub -> grpc_server [label="Proto-Request", color="#4da6ff"]
        grpc_server -> grpc_python_stub [label="Proto-Response", color="#4da6ff"]
        grpc_server -> grpc_android_java_stub [label="Proto-Response", color="#4da6ff"]
        grpc_android_java_stub -> grpc_server [label="Proto-Request", color="#4da6ff"]

    }

Starting with an interface definition in a ``.proto`` file, gRPC provides
Protocol Compiler plugins that generate Client- and Server-side APIs. Both
synchronous and asynchronous communication is supported in most languages. gRPC
also supports streaming of messages in a single RPC call. The `gRPC protocol
<https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md>`_ abstractly
specifies the communication between clients and servers:

#. First the stream is started by the client with a mandatory ``Call Header``

   #. followed by optional ``Initial-Metadata``
   #. followd by optional ``Payload Messages``.

   The contents of ``Call Header`` and ``Initial Metadata`` are sent as HTTP/2
   headers compressed with ``HPACK``.

#. The server answers with an optional ``Initial-Metadata``

   #. followed by ``Payload Messages``
   #. and terminated with mandatory ``Status`` and optional ``Status-Metadata``.

   Payload Messages are serialised into a byte stream fragmented into HTTP/2
   frames. ``Status`` and ``Trailing-Metadata`` are sent as HTTP/2 trailing
   headers.

.. seealso::
    * `Home <https://grpc.io/>`_
    * `GitHub <https://github.com/grpc/grpc>`_
    * `gRPC Load Balancing <https://grpc.io/blog/grpc-load-balancing/#why-grpc>`_

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 0

    install
    example
    test
