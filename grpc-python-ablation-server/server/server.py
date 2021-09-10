from concurrent import futures
import time

import grpc

import users_pb2_grpc as users_service


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class UsersService(users_service.UsersServicer):

    def CreateUser(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        user = users_service.User(username=request.username, user_id=1)
        return users_service.CreateUserResult(user=user)

    def Test(self, request, context):
        user = users_service.Test([1,2,3])
        userlist=[]
        for i in range(4):
            userlist.append(user)
        return users_service.Test(user=userlist)

    def GetUsers(self, request, context):
        for user in request.user:
            user = users_service.User(
                username=user.username, user_id=user.user_id
            )
            yield users_service.GetUsersResult(user=user)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_service.add_UsersServicer_to_server(UsersService(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
