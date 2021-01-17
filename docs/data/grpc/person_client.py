import logging

import grpc

import person_pb2
import person_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:8081")
    stub = person_pb2_grpc.SalutationStub(channel)
    response = stub.Salutation(person_pb2.SalutationRequest(name="you"))
    print("Person client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
