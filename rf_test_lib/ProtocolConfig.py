#-*- coding=utf8 -*-

import Launch_pb2

game_protobuf = {
                 # 1级 server index
                 1: {# 2级
                     1:{},
                     2:{    1: Launch_pb2.LaunchRequest(),
                            2: Launch_pb2.LaunchResponse(),
                        },
                            
                    }
                }