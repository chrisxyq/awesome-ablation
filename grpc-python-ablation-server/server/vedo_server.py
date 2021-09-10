#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

import grpc
from concurrent import futures

import numpy as np

from protos import vedo_service_pb2_grpc, vedo_service_pb2
from vedo import *
from io import BytesIO
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class VedoServicer(vedo_service_pb2_grpc.VedoServicer):

    def GetMeshPoints(self, request, context):
        response = vedo_service_pb2.GetMeshPointsResult(
            point=[vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate=1),vedo_service_pb2.Point(coordinate=2)]),
                   vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate=1),vedo_service_pb2.Point(coordinate=2)])]
        )
        # 数据源
        # data_list = Sphere().points().tolist()
        # lenth = len(data_list)
        # mesh_points = response.mesh_points
        # for j in range(0, lenth):
        #     # 第j个点
        #     data = data_list[j]
        #     point = mesh_points.Point()
        #     for column in range(0, len(data)):
        #         point.add(data[column])
        #     mesh_points.add(point)
        return response


        # Sphere().points()
        # response = vedo_service_pb2.GetMeshPointsResult()
        # response.mesh_points.append()
        # nda_bytes = BytesIO()
        # np.save(nda_bytes, Sphere().points(), allow_pickle=False)
        # response.mesh_points = nda_bytes.getvalue()

        # return vedo_service_pb2.GetMeshPointsResult(mesh_points=nda_bytes.getvalue())
        # return vedo_service_pb2.GetMeshPointsResult(mesh_points=Mesh('https://vedo.embl.es/example/data/man.vtk').points())


