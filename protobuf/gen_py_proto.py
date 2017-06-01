#-*- coding=utf8 -*-

import os
import shutil
import subprocess
python_out = "./pb_protos"

def getFiles(p = "./proto"):
    l = []
    for root, dirs, files in os.walk(p):
        for f in files:
            if "." in f and len(f) > 4 and (f[-6:] == ".proto"):
                fpath = os.path.join(root, f)
                l.append(fpath)
    return l

def makePB(pbfile = "", proto_exe = "./tools/protoc.exe", protoGen_exe = "./tools/protoGen.exe"):
    newPb = os.path.basename(pbfile)
    shutil.copy(pbfile, newPb)
    argus = [proto_exe, "--python_out=%s" % python_out, newPb]
    p = subprocess.Popen(argus, stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell = False)
    p.communicate()
    os.remove(newPb)
    
if os.path.exists(python_out):
    shutil.rmtree(python_out)    

if not os.path.exists(python_out):
    os.makedirs(python_out)
    
for npbfile in getFiles():
    makePB(pbfile = npbfile)
    
