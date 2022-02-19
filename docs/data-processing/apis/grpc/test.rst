Test gRPC
=========

``pytest-grpc``
---------------

gRPC can be tested automatically with `pytest-grpc
<https://pypi.org/project/pytest-grpc>`_.

#. First, we install

   .. code-block:: console

    $ pipenv install pytest-grpc
    Installing pytest-grpc…
    Adding pytest-grpc to Pipfile's [packages]…
    ✔ Installation Succeeded
    …

+. Then we create a :term:`Test Fixture` for our :doc:`example` with:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 2,4-25

   .. seealso::
      * `pytest fixtures <https://docs.pytest.org/en/latest/explanation/fixtures.html>`_

#. Afterwards we can write tests, e.g.:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 28-44

#. Authentication can also be tested, e.g. with:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 1,3,47-97

#. Afterwards we can test against a real gRPC server with:

   .. code-block:: console

    $ pipenv run pytest --fixtures tests/

   or directly against the Python code:

   .. code-block:: console

    $ pipenv run pytest --fixtures tests/ --grpc-fake-server
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.3, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    rootdir: /Users/veit/cusy/trn/jupyter-tutorial/docs/data/grpc
    plugins: grpc-0.8.0
    collected 2 items

    tests/test_accounts.py .F                                                [100%]
    …

.. seealso::
   * `GitHub <https://github.com/kataev/pytest-grpc>`_
   * `Example
     <https://github.com/kataev/pytest-grpc/blob/master/example/test_example.py>`_

Wireshark
---------

`Wireshark <https://www.wireshark.org/>`_ is an open source tool for analysing
network protocols. In the following, we will show you how to use the gRPC and
Protobuf dissectors. They make it easier for you to decode gRPC messages that
are serialised in :doc:`Protobuf <../../serialisation-formats/protobuf>` or
:doc:`../serialisation-formats/json/index` format. You can also use them to
analyse server, client and bidirectional gRPC streaming.

.. note::
    Usually, Wireshark can only analyse gRPC messages in plain text. For
    dissecting a TLS session, Wireshark needs the secret key, the export of
    which is currently only supported by `Go gRPC
    <https://grpc.io/docs/languages/go/>`_ [#]_.

.. seealso::
    * `Analyzing gRPC messages using Wireshark
      <https://grpc.io/blog/wireshark/>`_

----

.. [#] `How to Export TLS Master keys of gRPC
       <https://gitlab.com/wireshark/wireshark/-/wikis/How-to-Export-TLS-Master-keys-of-gRPC>`_
