# coding: UTF8

import subprocess
import os

for nfile in os.listdir("./"):
    if ".proto" in nfile:
        p = subprocess.Popen(["protoc.exe", "--python_out=./", nfile])
    