#!/usr/bin/env python
# coding=utf-8
import argparse
import datetime
import logging
import os,commands
from multiprocessing import Process
import time
from dateutil.parser import parse as parse_date

import subprocess






cmd = "./1.sh"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ret_info, err_info = process.communicate()
ret_code = process.returncode

print "gexing, out"
print ret_info

print "gexing, err"
print err_info

print "gexing,return"
print ret_code
