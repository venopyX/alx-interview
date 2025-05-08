#!/usr/bin/python3

"""Log Generator Script.

Generates random HTTP access logs in Apache/Nginx format with:
- Random IP addresses (1-255 for each octet)
- Current timestamps
- HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500)
- File sizes (1-1024 bytes)

Format: <IP> - [<timestamp>] "GET /projects/260 HTTP/1.1" <status> <size>
"""
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
