#!/usr/bin/python3
"""
Log parsing script that reads from standard input and computes metrics.

This script reads log entries from stdin, computes metrics such as
total file size and counts of status codes, and prints statistics
every 10 lines and when interrupted.
"""

import sys


def print_stats(status_codes, total_file_size):
    """
    Print statistics about log processing.

    Args:
        status_codes (dict): Dictionary containing counts of HTTP status codes
        total_file_size (int): Total accumulated file size
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])
                code = parsed_line[1]

                if code in status_codes.keys():
                    status_codes[code] += 1

            if counter == 10:
                print_stats(status_codes, total_file_size)
                counter = 0

finally:
    print_stats(status_codes, total_file_size)
