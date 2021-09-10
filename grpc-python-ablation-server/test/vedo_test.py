import unittest
import grpc
from protos import vedo_service_pb2, vedo_service_pb2_grpc
from protos import users_pb2, users_pb2_grpc


class MyTestCase(unittest.TestCase):
    def test_GetMeshPoints(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = vedo_service_pb2_grpc.VedoStub(channel)
            # response = stub.GetMeshPoints(vedo_service_pb2.GetMeshPointsRequest())
            response = stub.GetMeshPoints(vedo_service_pb2.GetMeshPointsRequest(mesh_index=1))
        print(response.point)
    def test(self):
        point = [vedo_service_pb2.Point(coordinate="1.1"), vedo_service_pb2.Point(coordinate="2")]
        response = vedo_service_pb2.GetMeshPointsResult(
            point=[vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate="1.1"),vedo_service_pb2.Point(coordinate="2")]),
                   vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate="1.1"),vedo_service_pb2.Point(coordinate="2")])]
        )
        # point = vedo_service_pb2.Point(coordinate=1)
        # response = vedo_service_pb2.GetMeshPointsResult(
        #     point=point
        # )
        print(response)
    def test5(self):
        user = vedo_service_pb2.ShuzuRequest(shuzu=vedo_service_pb2.Shuzu(shu="0.1"))

        print(user)
    def test4(self):
        request = vedo_service_pb2.GetUsersRequest(
            user=[vedo_service_pb2.User(username=["1","1","1"]),
                  vedo_service_pb2.User(username=["1","1","1"])]
        )
        print(request)
    def test5(self):
        userlist=[]
        user1=vedo_service_pb2.User()
        user1.username.append("1")
        user1.username.append("2")
        user2 = vedo_service_pb2.User()
        user2.username.append("1")
        user2.username.append("2")
        userlist.append(user1)
        userlist.append(user2)
        request = vedo_service_pb2.GetUsersRequest(
            user=userlist
        )
        print(request)

    def test6(self):
        userlist=[]
        user1=vedo_service_pb2.User()
        user1.username.append(1.1)
        user1.username.append(2.1)
        user1.username.append(3.1)
        user2 = vedo_service_pb2.User()
        user2.username.append(1.1)
        user2.username.append(2.1)
        user1.username.append(3.1)
        userlist.append(user1)
        userlist.append(user2)
        request = vedo_service_pb2.GetUsersRequest(
            user=userlist
        )
        print(request)
    def test7(self):
        data=[[1.1,1,1],[2.1,1,1]]
        userlist=[]
        for i in range(len(data)):
            useri=vedo_service_pb2.User()
            for j in range(len(data[i])):
                useri.username.append(data[i][j])
            userlist.append(useri)
        request = vedo_service_pb2.GetUsersRequest(
            user=userlist
        )
        print(request)
    def test3(self):
        # response = vedo_service_pb2.GetMeshPointsResult(
        #     point=[vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate=1),vedo_service_pb2.Point(coordinate=2)]),
        #            vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate=1),vedo_service_pb2.Point(coordinate=2)])]
        # )
        user = vedo_service_pb2.User(username="1",user_id=2.1)
        request = vedo_service_pb2.GetUsersRequest(
            user=[vedo_service_pb2.User(username="1", user_id=1.1),
                  vedo_service_pb2.User(username="1", user_id=1.1)]
        )
        print(request)

    def test2(self):
        # response = vedo_service_pb2.GetMeshPointsResult(
        #     point=[vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate=1),vedo_service_pb2.Point(coordinate=2)]),
        #            vedo_service_pb2.Point(point=[vedo_service_pb2.Point(coordinate=1),vedo_service_pb2.Point(coordinate=2)])]
        # )
        user = users_pb2.User(username="1",user_id=2)
        request = users_pb2.GetUsersRequest(
            user=[users_pb2.User(username="alexa", user_id=1),
                  users_pb2.User(username="christie", user_id=1)]
        )
        print(request)

    def test_users(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.GetUsersRequest(
                user=[users_pb2.User(username="alexa", user_id=1),
                      users_pb2.User(username="christie", user_id=1)]
            )
            response = stub.GetUsers(request)
        print(response)

    def test_users2(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = users_pb2_grpc.UsersStub(channel)
            request = users_pb2.TestRequest(test=users_pb2.Test(myint=[1,2,3]))
            response = stub.Test(request)
        print(response)


if __name__ == '__main__':
    unittest.main()
