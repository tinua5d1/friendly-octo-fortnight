#! /usr/bin/python3
# -*- coding:UTF-8 -*-
import requests
import os
import random
import socket
import json
import time

w = ["迪卢克", "七七", "提纳里", "琴", "刻晴", "莫娜"]

v0 = 107
v = "1.0.7"

print(f"抽卡系统:{v}(Ctrl+c可以退出)")
port_Api = 56010
port_gameS = 20701
gxnr = '''
1.0.7更新
· 更新了服务器及穿透节点，现在终于不是只有自己用了...
· 更新了抽的次数等
· 修复了在内测版本获得金色时无法增加抽数导致显示错误
· 修复了部分服务器问题,现在理论上更快了
'''


def progressbar(url, v, path=os.getcwd(),):
    if not os.path.exists(path):   # 看是否有该文件夹，没有则创建文件夹
        os.mkdir(path)
    start = time.time()  # 下载开始时间
    response = requests.get(url, stream=True)  # stream=True必须写上
    size = 0  # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])

    if response.status_code == 200:
        print('开始下载,文件总大小为{size:.2f} MB'.format(
            size=content_size / chunk_size / 1024))

        filepath = path+'\client' + v+".exe"

        with open(filepath, 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)
                print('\r'+'下载进度:%s%.2f%%' % ('>'*int(size*50 / content_size),
                                              float(size / content_size * 100)), end=' ')
    end = time.time()
    print('下载完成!用时%.2f秒' % (end - start))


def socket_cilent(host, num=0, num_=0, numm=0):
    api = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    api.connect((host, port_Api))
    api.send(json.dumps({"code": "V"}).encode("utf-8"))
    o = api.recv(100000).decode("utf-8")
    api.close()
    o = json.loads(o)
    code = o["code"]
    if code == "ok":
        print("版本检查中...")
        time.sleep(1)
        V0 = o["V0"]
        if V0 == v0:
            print("当前版本为最新版本")
            time.sleep(1)
            print("当前版本介绍:")
            time.sleep(1)
            print(gxnr)
        elif V0 < v0:
            print("当前版本为内测版")
            time.sleep(1)
            print("当前版本介绍:")
            time.sleep(1)
            print(gxnr)
        else:
            print("需要更新！")
            time.sleep(1)
            if input("回车将下载及显示更新内容，输入exit退出") == "exit":
                exit()
            else:
                V = o["V"]
                print(f"当前版本为{v},需要更新到的版本为{V}.准备下载...")

                api = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                api.connect((host, port_Api))
                api.send(json.dumps({
                    "code": "D"
                }).encode("utf-8"))
                o = api.recv(100000).decode("utf-8")
                o = json.loads(o)
                code = o["code"]
                time.sleep(5)
                if code == "ok":
                    print("获取成功...")
                    time.sleep(1)
                    Download = o["Download"]
                    jx = o["jx"]
                    print(jx)
                    time.sleep(5)
                    progressbar(Download, v=V)
                    time.sleep(5)
                    input("回车以成功")
                    exit()
                else:
                    print("请求失败...")
                    time.sleep(5)
                    input("回车以退出...")
                    exit()
    while 1:
        gameS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gameS.connect((host, port_gameS))
        co = input(f"(目前已抽{num_}发)1:单发,2:十连:")
        if co == '1':
            gameS.send(json.dumps({
                "code": "Y",
                "type": "ck1",
                "num": num
            }).encode("utf-8"))
            o = gameS.recv(100000).decode("utf-8")
            o = json.loads(o)
        elif co == "2":
            gameS.send(json.dumps({
                "code": "Y",
                "type": "ck10",
                "num": num
            }).encode("utf-8"))
            o = gameS.recv(100000).decode("utf-8")
            o = json.loads(o)
        else:
            print("输入错误...")
            gameS.close()
            continue
        gameS.close()
        code = o["code"]
        if code == "ok":
            print("请求成功...")
            time.sleep(2)
            jg = o["jg"]
            up = o["up"]
            for i in jg:
                num += 1
                num_ += 1
                numm += 1
                if i == "1":
                    print("获得答辩")
                elif i == "2":
                    num = 90

                    print(f"你使用{numm}抽获得{random.choice(w)}(歪了)")
                    numm = 0
                elif i == "3":
                    print(f"你使用{numm}抽获得当前up角色:{up}!")
                    numm = 0
                    num = 0
        else:
            print("请求失败")
            input("回车以退出...")
            exit()


try:
    socket_cilent("202.182.125.24")
except:
    input("\n回车以退出...")
# swswssdmdkmmedmsddwd
# dededddedswddes
# dedoedakdwdedmaxls//'[d\]wddw
# dwejdwjsw
#####################################################################################333332343333333333343333333333233333333333333333333333#233333333333333333333333333333333333333333333