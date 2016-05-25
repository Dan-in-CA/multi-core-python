#!/usr/bin/python
# -*- coding: utf-8 -*- 

from multiprocessing import Process, Queue, current_process
from time import sleep

functionQueue = Queue()
Queue_2 = Queue()
Queue_3 = Queue()

def fast_loop():
    while True:
        pass

def test_process_1():
    """ Function to run a loop that processes functions in queue. """    
    print current_process().name, 'starting'       
    while True:  
        items = functionQueue.get()
        func = items[0]
        args = items[1:]
        if func:
            func(*args)


def test_process_2():
    """ Function to run a loop that processes functions in queue. """  
    print current_process().name, 'starting'  
    while True:  
        items = Queue_2.get()
        func = items[0]
        args = items[1:]
        if func:
            func(*args)


def test_process_3():
    """ Function to run a loop that processes functions in queue.""" 
    print current_process().name, 'starting'    
    while True:  
        items = Queue_3.get()
        func = items[0]
        args = items[1:]
        if func:
            func(*args)


def main():
    print current_process().name, 'starting'
    
    functionQueue.put((fast_loop,))
#    Queue_2.put((fast_loop,))
#    Queue_3.put((fast_loop,))

    while True:
        print "main is running"
        sleep(5)
        

if __name__ == '__main__':
    # comment out main and uncomment the following line to enable multi-core operation
    main()
 #   p1 = Process(name = "Main", target=main,).start()

    p2 = Process(name = "Test Process 1", target=test_process_1,).start()
    p3 = Process(name = "Test Process 2", target=test_process_2,).start()
    p4 = Process(name = "Test Process 3", target=test_process_3,).start()  