import socket
# 创建Socket对象
socket_server = socket.socket()
# 绑定IP和端口
socket_server.bind(('127.0.0.1', 8080))
# 监听端口
socket_server.listen(5)
# listen方法内接受一个整数传参数，表示接受的链接数量
# 等待客户端链接
# result: tuple = socket_server.accept()
# conn =  result[0]
# address = result[1]
conn, address = socket_server.accept()
# accept方法返回一个元组，第一个元素是链接对象，第二个元素是链接地址

print(f"接收到客户端的链接: {address}")
while True:
    # 接受客户端信息，要使用客户端和服务器的本次链接对象，而非socket_server
    data: str = conn.recv(1024).decode("utf-8")
    # recv方法返回一个字节对象，需要decode成字符串
    print(f"客户端发送了：{data}")
    msg = input("请输入你要和客户端回复的信息：").encode("utf-8")
    if msg == "exit":
        break
    conn.send(msg)
conn.close()
socket_server.close()