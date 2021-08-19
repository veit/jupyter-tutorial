from concurrent import futures
import logging

import grpc

import accounts_pb2_grpc as accounts_service
import accounts_pb2 as accounts_messages


class AccountsService(accounts_service.AccountsServicer):
    def CreateAccount(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        account = accounts_messages.Account(
            account_name=request.account_name, account_id=1
        )
        return accounts_messages.CreateAccountResult(account=account)

    def GetAccounts(self, request, context):
        for account in request.account:
            account = accounts_messages.Account(
                account_name=account.account_name,
                account_id=account.account_id,
            )
            yield accounts_messages.GetAccountsResult(account=account)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    accounts_service.add_AccountsServicer_to_server(AccountsService(), server)
    server.add_insecure_port("[::]:8081")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
