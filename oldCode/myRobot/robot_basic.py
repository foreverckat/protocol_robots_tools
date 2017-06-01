'''
@author: chengjie
'''
import logging

LogFileLevel = getattr(logging, "INFO")
ConsoleLevel = getattr(logging, "INFO")
LogFileName  = "robot.log"
logging.basicConfig(filename = LogFileName, level = LogFileLevel, filemode = 'w', format = '%(asctime)s - %(threadName)-10s  %(levelname)s: %(message)s') 
console = logging.StreamHandler()
console.setLevel(ConsoleLevel)
formatter = logging.Formatter('%(asctime)s - %(threadName)-10s  %(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


        
    