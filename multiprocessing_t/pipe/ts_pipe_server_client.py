#!/usr/bin/env python
# coding: UTF-8
"""
使用管道实现的客户机服务器模型，注意关闭不用的输入与输出管道在每个进程中。
send()和recv()方法使用pickle模块对对象进行序列化
管道可用于双向通信
"""

import multiprocessing


def adder(pipe):
    server_p, client_p = pipe
    client_p.close()
    while True:
        try:
            x, y = server_p.recv()
        except EOFError:
            break
        result = x + y
        server_p.send(result)
        # 关闭
        print "server done"
    print "server out."


if __name__ == "__main__":
    (server_p, client_p) = multiprocessing.Pipe()

    # 启动服务器进程
    adder_p = multiprocessing.Process(target=adder, args=((server_p, client_p),))
    adder_p.start()

    # client process.
    # 关闭客户端中的服务器管道
    server_p.close()

    # 在服务器上提出一些请求
    client_p.send((3, 4))
    print client_p.recv()

    client_p.send(("hello", "world"))
    print client_p.recv()

    print "send eof"

    # 完成，关闭管道
    client_p.close()

    print "client wait."

    # 等待消费者进程关闭
    adder_p.join()

    print "client out."
