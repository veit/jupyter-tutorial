from concurrent import futures
import logging

import grpc

import person_pb2
import person_pb2_grpc


class Salutation(person_pb2_grpc.SalutationServicer):
    def Salutation(self, request, context):
        return person_pb2.SalutationReply(message="Hello, %s!" % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_SalutationServicer_to_server(Salutation(), server)
    server.add_insecure_port("[::]:8081")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
