from pathlib import Path
import pytest
import grpc
from accounts_pb2 import CreateAccountRequest, GetAccountsRequest


@pytest.fixture(scope="module")
def grpc_add_to_server():
    from accounts_pb2_grpc import add_AccountsServicer_to_server

    return add_AccountsServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    from accounts_server import AccountsService

    return AccountsService()


@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    from accounts_pb2_grpc import AccountsStub

    return AccountsStub(grpc_channel)


def test_create_account(grpc_stub):
    value = "test-data"
    nl = "\n"
    request = CreateAccountRequest(account_name=value)
    response = grpc_stub.CreateAccount(request)

    assert (
        f"{response.account}"
        == f'account_id: 1{nl}account_name: "test-data"{nl}'
    )


def test_get_accounts(grpc_stub):
    request = GetAccountsRequest()
    response = accounts_server.GetAccounts(request)

    assert response.name == f"test-{request.name}"


@pytest.fixture(scope="module")
def grpc_server(_grpc_server, grpc_addr, my_ssl_key_path, my_ssl_cert_path):
    """
    Overwrites default `grpc_server` fixture with ssl credentials
    """
    credentials = grpc.ssl_server_credentials(
        [(my_ssl_key_path.read_bytes(), my_ssl_cert_path.read_bytes())]
    )

    _grpc_server.add_secure_port(grpc_addr, server_credentials=credentials)
    _grpc_server.start()
    yield _grpc_server
    _grpc_server.stop(grace=None)


@pytest.fixture(scope="module")
def my_channel_ssl_credentials(my_ssl_cert_path):
    # If we're using self-signed certificate it's necessarily to pass root certificate to channel
    return grpc.ssl_channel_credentials(
        root_certificates=my_ssl_cert_path.read_bytes()
    )


@pytest.fixture(scope="module")
def grpc_channel(my_channel_ssl_credentials, create_channel):
    """
    Overwrites default `grpc_channel` fixture with ssl credentials
    """
    with create_channel(my_channel_ssl_credentials) as channel:
        yield channel


@pytest.fixture(scope="module")
def grpc_authorized_channel(my_channel_ssl_credentials, create_channel):
    """
    Channel with authorization header passed
    """
    grpc_channel_credentials = grpc.access_token_call_credentials("some_token")
    composite_credentials = grpc.composite_channel_credentials(
        my_channel_ssl_credentials, grpc_channel_credentials
    )
    with create_channel(composite_credentials) as channel:
        yield channel


@pytest.fixture(scope="module")
def my_authorized_stub(grpc_stub_cls, grpc_channel):
    """
    Stub with authorized channel
    """
    return grpc_stub_cls(grpc_channel)
