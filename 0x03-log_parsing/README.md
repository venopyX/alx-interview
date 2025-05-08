# 0x03. Log Parsing

## Overview
This project focuses on building a log parsing script in Python that processes log data from standard input (stdin). The script parses log entries in a specific format, calculates metrics, and displays statistics periodically or when interrupted.

## Requirements
- Python 3.4.3+
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)
- All files must be executable

## Project Timeline
- **Start Date**: May 5, 2025, 6:00 AM
- **End Date**: May 9, 2025, 6:00 AM
- **Auto Review**: Launched at deadline

## Task: Log Parsing

### Description
Write a script that reads stdin line by line and computes metrics:

- **Input format**: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  - If the format is not correct, the line must be skipped

- **Output**:
  - After every 10 lines and/or a keyboard interruption (CTRL + C), print the statistics
  - Statistics include:
    - Total file size: `File size: <total size>` where `<total size>` is the sum of all file sizes
    - Number of lines by status code in ascending order:
      - Valid status codes: 200, 301, 400, 401, 403, 404, 405, and 500
      - Format: `<status code>: <number>`
      - Only print status codes that have appeared in the input

### Implementation
The implementation consists of two files:
- `0-stats.py`: The main script that parses logs and displays statistics
- `0-generator.py`: A test script that generates random log entries

### Example
```
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
...
```

## Concepts Covered
- File I/O in Python (reading from stdin)
- Signal handling (for CTRL+C interruptions)
- Data parsing and string manipulation
- Dictionary usage for counting and aggregation
- Exception handling

## Author
**Gemechis Chala** [venopyx](https://github.com/venopyx)