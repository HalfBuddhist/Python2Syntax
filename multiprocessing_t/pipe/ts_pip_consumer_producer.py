#!/usr/bin/env python
# coding: UTF-8
"""
使用管道实现的生产者与消费者模型，注意关闭不用的输入与输出管道在每个进程中。
不关闭不必要的管道则可能会出错。
"""

import multiprocessing


def consumer(pipe):
    output_p, input_p = pipe
    input_p.close()  # 关闭管道的输入端
    while True:
        try:
            item = output_p.recv()
        except EOFError:
            break
        # 处理项目
        print item  # 可替换有用的工作
        # 关闭
        print "Consumer close"
    print "consuemr finished."


# 生产项目并将其放置到队列上，sequence是代表要处理项目的可迭代对象
def producer(sequence, input_p):
    for item in sequence:
        # 将项目放置在队列上
        input_p.send(item)


if __name__ == "__main__":
    (output_p, input_p) = multiprocessing.Pipe()
    # the input pip is also the child pipe end.

    # 启动使用者进程
    cons_p = multiprocessing.Process(target=consumer, args=((output_p, input_p),))
    cons_p.start()

    # 关闭生产者中的输出管道
    output_p.close()

    # 生产项目
    sequence = [1, 2, 3, 4]
    producer(sequence, input_p)

    # 关闭输入管道，表示完成
    input_p.close()

    print "producer wait."

    # 等待使用者进程关闭
    cons_p.join()

    print "producer finished."
