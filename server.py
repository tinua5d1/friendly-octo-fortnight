import Api_server as Api_server
import main as main
import threading
import time
import v
print("主服务器成功启动")
time.sleep(2)
print('当前服务器要求版本至少为:',v.ver,",数字编号为",v.Ver)
for i in [threading.Thread(target=main.run,), threading.Thread(target=Api_server.main,)]:
    time.sleep(2)
    i.start()

print("全部成功启动")
