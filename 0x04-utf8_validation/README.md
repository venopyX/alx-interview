# 0x04. UTF-8 Validation

## Overview

This project focuses on validating whether a given dataset represents a valid UTF-8 encoding using Python. The solution leverages bitwise operations and knowledge of the UTF-8 encoding scheme to check the validity of byte sequences.

## Author

**Gemechis Chala** ([venopyx](https://github.com/venopyx))

## Requirements

- Python 3.4.3+
- Ubuntu 20.04 LTS
- PEP 8 style (version 1.7.x)
- All files must be executable

## Project Timeline

- **Start Date**: May 12, 2025, 6:00 AM
- **End Date**: May 16, 2025, 6:00 AM
- **Auto Review**: Launched at deadline

## Task: UTF-8 Validation

### Description

Write a method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers (each integer represents 1 byte)
- Only the 8 least significant bits of each integer are considered

### Usage

Example usage with the provided test file:

```
$ ./0-main.py
True
True
False
```

## Concepts Covered

- Bitwise operations in Python
- UTF-8 encoding scheme and validation
- Data representation at the byte level
- List manipulation and iteration
- Boolean logic and control flow

## Files

- `0-validate_utf8.py`: Contains the `validUTF8` function for validation
- `0-main.py`: Example test cases for validation

## References

- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
