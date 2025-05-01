# 🧮 0x02. Minimum Operations

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python 3.7+"/>
  <img src="https://img.shields.io/badge/Algorithm-Prime_Factorization-brightgreen.svg" alt="Algorithm"/>
  <img src="https://img.shields.io/badge/Complexity-O(√n)-orange.svg" alt="Complexity"/>
</p>

## 📝 Problem Statement

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: **Copy All** and **Paste**. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` H characters in the file.

### Requirements:

- Prototype: `def minOperations(n)`
- Returns an integer representing the minimum number of operations
- If `n` is impossible to achieve, return `0`

## 🧪 Test Case Example

```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

Output:

```
Min # of operations to reach 4 characters: 4
Min # of operations to reach 12 characters: 7
```

## 🔍 Example Explained

For `n = 9`:

1. Initial state: `H`
2. Copy All: `H` (in clipboard)
3. Paste: `HH` (2 characters)
4. Paste: `HHH` (3 characters)
5. Copy All: `HHH` (in clipboard)
6. Paste: `HHHHHH` (6 characters)
7. Paste: `HHHHHHHHH` (9 characters)

Total operations: 6

## 💡 Solution Approach

The solution leverages prime factorization because:

1. We start with 1 character (`H`)
2. At any point, we can either:

   - Copy all existing characters (1 operation)
   - Paste previously copied characters (1 operation)

3. To get from 1 to `n` characters optimally:
   - We need to find the prime factors of `n`
   - Each prime factor `p` contributes `p` operations to the total

For any number `n`, the sum of its prime factors (counting repetitions) gives us the minimum operations needed.

### Complexity Analysis:

- **Time Complexity**: O(√n) - As we only need to check divisors up to the square root of n
- **Space Complexity**: O(1) - We only use a constant amount of extra space

## 🛠️ Setup & Testing

```bash
# Create and set permissions
chmod +x ./0-minoperations.py

# Lint your code
pycodestyle ./0-minoperations.py

# Test the solution
python3 0-main.py
```

## 📚 References

- [Prime Factorization](https://en.wikipedia.org/wiki/Integer_factorization)
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Greedy Algorithms](https://en.wikipedia.org/wiki/Greedy_algorithm)

## 👨‍💻 Author

This project was completed by [Gemechis Chala](https://github.com/venopyx).

<p align="center">
  <a href="https://github.com/venopyx"><img src="https://img.shields.io/badge/GitHub-@venopyx-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
</p>

<p align="center">
  <em>Special thanks to <a href="https://www.alxafrica.com/">ALX Africa Software Engineering</a> program for the project requirements.</em>
</p>
