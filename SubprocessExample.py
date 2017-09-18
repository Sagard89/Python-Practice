import sys
import os
import subprocess

def subprocess_cmd(command):
    try:
        process = subprocess.call(command,stdout=subprocess.PIPE, shell=True)
        
    except subprocess.CalledProcessError as e:
      print(e.returncode)

subprocess_cmd('ls -l; echo b')
