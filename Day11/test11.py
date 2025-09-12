import socket
# 创建socket对象
socket_client = socket.socket()
# 连接服务器
socket_client.connect(('127.0.0.1', 8080))
while True:
    # 发送信息
    msg = input("请输入要发送的信息：")
    if msg == "exit":
        break
    socket_client.send(msg.encode("utf-8"))
    # 接受返回信息
    recv_data = socket_client.recv(1024).decode("utf-8")
    print(f"接收到服务器的信息：{recv_data}")

socket_client.close()