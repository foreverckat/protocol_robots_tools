#coding=UTF8

robot_cfg = {
          "socket":{
                    "timeout":1,
                    },
          "server":{
                    "login":("120.25.152.20", 8090),
                    "logic":("localhost", 8771),
                    "chat":("localhost", 8771),
                    },
          "robot":{
                   "count": 400,
                   "action":[
                              ["action_login",],
                              #["action_login", (3,)],
                              #["action_login", (4,)],
                              #["action_login", (5,)],
                              #["action_login", (6,)],
                              #["action_login", (7,)],
                              
                              ]
                   },                
        }