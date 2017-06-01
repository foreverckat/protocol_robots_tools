#coding=utf8
'''

@author: chengjie
'''
import logging
import Queue

class dataManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataQueue = Queue.Queue()
        
    def write(self, data):
        logging.info(data)
        self.dataQueue.put(data)
    
    def read(self):
        logging.info(self.dataQueue.get())