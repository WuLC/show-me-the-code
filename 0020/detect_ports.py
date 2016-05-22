# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-22 16:04:10
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-22 17:01:11
# @Email: liangchaowu5@gmail.com

import socket
import Queue
import time
from threading import Thread

class DetectPort(Thread):
    def __init__(self):
        Thread.__init__(self)
        print '%s is created'%self.name


    def run(self):
        while not PORT_QUEUE.empty():
            port = PORT_QUEUE.get()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            address = (IP, port)
            result = s.connect_ex(address)
            try:
                if result == 0:
                    print '%s on %s is open--%s'%(address[1],address[0],self.name)
            finally:
                PORT_QUEUE.task_done()
                s.close()

if __name__ == '__main__':
    IP = '110.64.76.111'
    start_port = 1
    end_port = 1000
    PORT_QUEUE = Queue.Queue()
    for i in xrange(start_port,end_port+1):
        PORT_QUEUE.put(i)
    thread_num = 10
    start_time = time.time()
    for i in xrange(thread_num):
        th = DetectPort()
        th.start()
    PORT_QUEUE.join()
    print 'finished,time consuming: %ss'%(int(time.time()-start_time))

    