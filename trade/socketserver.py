import socket
import threading

global clients
clients = {}


class Websocket_Server(threading.Thread):
    def __init__(self, port):
        self.port = port
        super(Websocket_Server, self).__init__()

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", self.port))
        sock.listen(5)
        while (True):
            # 等待客户端连接
            conn, addr = sock.accept()
            print("客户端{}连接成功:".format(addr))
            conn.send(("welcome...").encode("utf8"))
            while (True):
                try:
                    info = conn.recv(1024)
                    connId = "ID:" + str(addr[1])
                    clients[connId] = conn
                    print("{0}:{1}".format(connId, info.decode("utf8")))
                except Exception as e:
                    print(e)
                msg = input()
                conn.send(msg.encode("utf8"))
                if info == b"bye":
                    print("客户端退出")
                    conn.close()
                    break
