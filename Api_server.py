import socket
import threading
import json

import v
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 98))
s.listen(100)

gxnr = '''
1.0.7更新
· 更新了服务器及穿透节点，现在终于不是只有自己用了...
· 更新了抽的次数等
· 修复了在内测版本获得金色时无法增加抽数导致显示错误
· 修复了部分服务器问题,现在理论上更快了
'''
V = v.ver
V0 = v.Ver
Download = v.d
def api_socket(sock, addr):
    try:
        print("来自api的链接成功:", addr)
        
        o = sock.recv(100000).decode("utf-8")
        o = json.loads(o)
        "o:dict"
        code = o["code"]
        if code == "V":
            sock.send(json.dumps({
                "code": "ok",
                "V0": V0,
                "V": V
            }).encode("utf-8"))
            sock.close()
            return
        elif code == "D":
            sock.send(json.dumps({
                "code": "ok",
                "Download": Download,
                'jx':gxnr
            }).encode('utf-8'))
            sock.close()
            return
    except:
        print("不合法的错误...")


def main():
    print("api成功启动")
    while 1:
        try:
            sock, addr = s.accept()
            thread_os = threading.Thread(target=api_socket, args=(sock, addr))
            thread_os.start()
        except:
            print("不合法的错误")
