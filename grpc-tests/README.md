# grpc-demo

gRPC：Google 于 2015 年对外开源的跨语言 RPC 框架，支持多种语言。

[java和python使用grpc交互](https://blog.csdn.net/zhj_fly/article/details/82684970)

[gRPC 官方文档中文版](https://doc.oschina.net/grpc?t=58009)

[grpc的demo](https://blog.csdn.net/u010970956/article/details/108252079)

# protobuf 

[protobuf 语法介绍](https://developers.google.com/protocol-buffers/docs/pythontutorial)

[protobuf 语法介绍](https://jitwxs.cn/60aca815.html)

```python
#python发送二维数组
message GetUsersRequest {
	repeated User user = 1;
}
message User {
  repeated string username = 1;
}

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
        
```



```python
#python发送二维数组
message GetUsersRequest {
  repeated User user = 1;
}
message User {
  repeated double username = 1;
//  double user_id = 2;
}
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
def test6(self):
    userlist=[]
    user1=vedo_service_pb2.User()
    user1.username.append(1)
    user1.username.append(2)
    user2 = vedo_service_pb2.User()
    user2.username.append(1)
    user2.username.append(2)
    userlist.append(user1)
    userlist.append(user2)
    request = vedo_service_pb2.GetUsersRequest(
    user=userlist
    )
    print(request)
```

