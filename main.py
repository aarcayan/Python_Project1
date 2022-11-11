# This is a sample Python script.
import os.path
import sys
import unittest
from datetime import datetime
# import time
# import yaml
# import json
# import re
# import xmlrunner
# import requests
# import os
# from os.path import exists
# from requests. exceptions import HTTPError
# import subprocess
# import sys
# import urllib3

# Datetime object containing current date and time
now = datetime.now()
date_string = now.strftime("%d/%m/%Y %H:%M:%S")
current_dir = os.path.dirname((os.path.realpath(sys.argv[0])))

print("")
print("*"*len(current_dir))
print("*    This is my framework    *")
print("*"*len(current_dir))
print("* Time:{}".format(date_string))
print("* Path:{}".format(current_dir))
print("*"*len(current_dir))
print("")

# Logging configuration
log_file = current_dir + "/" + "my_logfile.log"
def LogFile(text):
    outputFile = open(log_file, 'a')
    if outputFile:
        outputFile.write(str(text)+ "\n")
    outputFile.close()

# Initialize Logging file
def config_LogFile():
    if os.path.exists(log_file):
        print("***Removing log file:{}".format(log_file))
        os.remove(log_file)
    else:
        print("***Log file does not exist")
    open(log_file, 'a')
    LogFile("")
    LogFile("*" * len(current_dir))
    LogFile("*    This is my framework    *")
    LogFile("*" * len(current_dir))
    LogFile("* Time:{}".format(date_string))
    LogFile("* Path:{}".format(current_dir))
    LogFile("*" * len(current_dir))
    LogFile("")



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    config_LogFile()
    unittest.main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
