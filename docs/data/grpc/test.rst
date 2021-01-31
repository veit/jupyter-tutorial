Test gRPC
=========

gRPC can be tested automatically with `pytest-grpc
<https://pypi.org/project/pytest-grpc/>`_.

#. First, we create a :term:`Test Fixture` for our :doc:`example` with:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 2,4-25

   .. seealso::
      * `pytest fixtures <https://docs.pytest.org/en/latest/fixture.html>`_

#. Afterwards we can write tests, e.g.:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 28-38

#. Authentication can also be tested, e.g. with:

   .. literalinclude:: tests/test_accounts.py
      :language: python
      :lines: 1,3,39-93

#. Afterwards we can test against a real gRPC server with:

   .. code-block:: console

    $ pytest

   or directly against the Python code:

   .. code-block:: console

    $ pytest --grpc-fake-server
