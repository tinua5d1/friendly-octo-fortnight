import socket
import threading
import json
import ys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 101))
s.listen(100)

def game_server_socket(sock, addr):
    try:
        print("来自gameS的链接成功:", addr)
        o = sock.recv(100000).decode("utf-8")
        o = json.loads(o)  # o:dict
        code = o["code"]  # code:str
        if code == "Y":
            type_s = o["type"]
            if type_s == "ck1":
                jg = [ys.oen(o["num"])]
                sock.send(json.dumps({
                    "code": "ok",
                    "jg": jg,
                    "up": ys.up,
                }).encode("utf-8"))
            elif type_s == "ck10":
                jg = []
                for i in range(10):
                    jg.append(ys.oen(o["num"]+i))
                sock.send(json.dumps({
                    "code": "ok",
                    "jg": jg,
                    "up": ys.up,
                }).encode("utf-8"))
            sock.close()
            return

        elif code == "F":
            return
    except:
        print("不合法的错误...")


def run():
    print("gameS成功启动")
    while 1:
        try:
            sock, addr = s.accept()
            thread_os = threading.Thread(
                target=game_server_socket, args=(sock, addr))
            thread_os.start()
        except:
            print("不合法的错误")
