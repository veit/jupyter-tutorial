import logging

import grpc

import accounts_pb2_grpc as accounts_service
import accounts_pb2 as accounts_messages


def run():
    channel = grpc.insecure_channel("localhost:8081")
    stub = accounts_service.AccountsStub(channel)
    response = stub.CreateAccount(
        accounts_messages.CreateAccountRequest(account_name="tom"),
    )
    if response:
        print("Account created:", response.account.account_name)
    request = accounts_messages.GetAccountsRequest(
        account=[
            accounts_messages.Account(account_id=1, account_name="veit"),
            accounts_messages.Account(account_id=2, account_name="andy"),
        ]
    )
    response = stub.GetAccounts(request)
    for resp in response:
        print(resp)


if __name__ == "__main__":
    logging.basicConfig()
    run()
