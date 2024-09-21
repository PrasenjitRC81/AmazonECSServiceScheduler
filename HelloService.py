import random
import time
import signal
import sys
import time
import datetime
import csv
import boto3
from io import StringIO

print("Hello World1")
current_time = datetime.datetime.fromtimestamp(time.time())
print(f"Current time: {current_time}")
i = 0
while i<5:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Hello, World! Current time: {current_time}")
        i = i+1
        time.sleep(10)
current_time = datetime.datetime.fromtimestamp(time.time())
print(f"Current time+: {current_time}")



