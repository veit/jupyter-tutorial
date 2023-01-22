import logging

import accounts_pb2 as accounts_messages
import accounts_pb2_grpc as accounts_service
import grpc


def run():
    channel = grpc.insecure_channel("localhost:8081")
    stub = accounts_service.AccountsStub(channel)
    response = stub.CreateAccount(
        accounts_messages.CreateAccountRequest(account_name="tom"),
    )
    print("Account created:", response.account.account_name)


if __name__ == "__main__":
    logging.basicConfig()
    run()
