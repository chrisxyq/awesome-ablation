#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

import grpc
from concurrent import futures

from protos import vedo_service_pb2_grpc, vedo_service_pb2
from server import vedo_server
from server.vedo_server import *
from vedo import *
_ONE_DAY_IN_SECONDS = 60 * 60 * 24
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vedo_service_pb2_grpc.add_VedoServicer_to_server(VedoServicer(), server)
    print('Starting server. Listening on port 5005.')
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()