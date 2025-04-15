# Pascal's Triangle Generator

Generates Pascal's triangle up to the specified number of rows. Returns an empty list if `n <= 0`.

**Example:**
```py
from 0-pascal_triangle import pascal_triangle

print_triangle(pascal_triangle(5))
```

## Output:

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

**Implementation:**  
Calculates each row using binomial coefficients, optimized for integer operations.  
**File:** `0-pascal_triangle.py`

## Concepts Guide

### 1. Lists and List Comprehensions

**Lists** are ordered, mutable collections in Python that can store various data types.

- **Creating Lists:**
  ```python
  # Empty list
  my_list = []
  
  # List with elements
  numbers = [1, 2, 3, 4, 5]
  mixed = [1, "Hello", 3.14, True]
  ```

- **Accessing Elements:**
  ```python
  print(numbers[0])   # Output: 1 (first element)
  print(numbers[-1])  # Output: 5 (last element)
  ```

- **Modifying Lists:**
  ```python
  numbers[2] = 10
  print(numbers)      # Output: [1, 2, 10, 4, 5]
  
  numbers.append(6)
  print(numbers)      # Output: [1, 2, 10, 4, 5, 6]
  
  numbers.insert(2, 7)
  print(numbers)      # Output: [1, 2, 7, 10, 4, 5, 6]
  ```

- **Iterating Over Lists:**
  ```python
  for num in numbers:
      print(num)  # Prints each element
  ```

- **List Methods:**
  ```python
  my_list = [3, 1, 4, 2]
  my_list.sort()
  print(my_list)      # Output: [1, 2, 3, 4]
  
  my_list.reverse()
  print(my_list)      # Output: [4, 3, 2, 1]
  
  my_list.remove(2)
  print(my_list)      # Output: [4, 3, 1]
  
  my_list.pop()
  print(my_list)      # Output: [4, 3]
  
  my_list.extend([5, 6])
  print(my_list)      # Output: [4, 3, 5, 6]
  ```

- **List Comprehensions:**
  A concise way to create or transform lists.
  ```python
  squares = [x**2 for x in range(5)]
  print(squares)      # Output: [0, 1, 4, 9, 16]
  
  even_numbers = [x for x in range(10) if x % 2 == 0]
  print(even_numbers) # Output: [0, 2, 4, 6, 8]
  ```

---

### 2. Functions

**Functions** are reusable blocks of code that perform specific tasks.

- **Defining and Calling Functions:**
  ```python
  def greet(name):
      return f"Hello, {name}!"
  
  print(greet("Alice"))  # Output: Hello, Alice!
  ```

- **Parameters and Return Values:**
  ```python
  def add(a, b):
      return a + b
  
  result = add(3, 5)
  print(result)  # Output: 8
  ```

- **Default Parameters:**
  ```python
  def power(base, exponent=2):
      return base ** exponent
  
  print(power(3))     # Output: 9
  print(power(3, 3))  # Output: 27
  ```

- **Lambda Functions:**
  Anonymous functions defined in a single line.
  ```python
  square = lambda x: x**2
  print(square(5))    # Output: 25
  ```

- **Function Annotations:**
  Optional type hints for parameters and return values.
  ```python
  def add(a: int, b: int) -> int:
      return a + b
  
  print(add(3, 4))    # Output: 7
  ```

---

### 3. Loops

**Loops** allow you to repeat code execution.

- **For Loops:**
  ```python
  for i in range(5):
      print(i)  # Outputs: 0, 1, 2, 3, 4
  ```

- **While Loops:**
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1  # Outputs: 0, 1, 2, 3, 4
  ```

- **Nested Loops:**
  ```python
  for i in range(3):
      for j in range(2):
          print(f"i={i}, j={j}")
  # Outputs:
  # i=0, j=0
  # i=0, j=1
  # i=1, j=0
  # i=1, j=1
  # i=2, j=0
  # i=2, j=1
  ```

- **Loop Control Statements:**
  ```python
  for i in range(10):
      if i == 5:
          break    # Exits the loop
      if i % 2 == 0:
          continue # Skips to next iteration
      print(i)     # Outputs: 1, 3
  ```

---

### 4. Conditional Statements

**Conditional statements** execute code based on conditions.

- **If, Elif, Else:**
  ```python
  age = 20
  if age < 18:
      print("Minor")
  elif age >= 18 and age < 65:
      print("Adult")
  else:
      print("Senior")
  # Output: Adult
  ```

- **Ternary Operator:**
  A concise if-else statement.
  ```python
  status = "Minor" if age < 18 else "Adult"
  print(status)  # Output: Adult
  ```

---

### 5. Recursion (Optional)

**Recursion** involves a function calling itself to solve a problem.

- **Simple Recursive Function:**
  ```python
  def factorial(n):
      if n == 0:
          return 1
      else:
          return n * factorial(n - 1)
  
  print(factorial(5))  # Output: 120
  ```

- **Another Example (Countdown):**
  ```python
  def countdown(n):
      if n <= 0:
          print("Done!")
      else:
          print(n)
          countdown(n - 1)
  
  countdown(3)  # Outputs: 3, 2, 1, Done!
  ```

---

### 6. Arithmetic Operations

Basic **arithmetic operations** are essential for calculations.

- **Basic Operations:**
  ```python
  a = 10
  b = 3
  print(a + b)   # 13 (addition)
  print(a - b)   # 7 (subtraction)
  print(a * b)   # 30 (multiplication)
  print(a / b)   # 3.333... (division)
  print(a // b)  # 3 (integer division)
  print(a % b)   # 1 (modulus)
  print(a ** b)  # 1000 (exponentiation)
  ```

- **Floating Point Precision:**
  ```python
  print(0.1 + 0.2)         # Output: 0.30000000000000004
  print(0.1 + 0.2 == 0.3)  # Output: False
  ```

---

### 7. Indexing and Slicing

**Indexing** and **slicing** access parts of sequences like lists.

- **Indexing:**
  ```python
  my_list = [0, 1, 2, 3, 4]
  print(my_list[0])   # Output: 0
  print(my_list[-1])  # Output: 4
  ```

- **Slicing:**
  ```python
  print(my_list[1:3])   # Output: [1, 2]
  print(my_list[:2])    # Output: [0, 1]
  print(my_list[2:])    # Output: [2, 3, 4]
  print(my_list[::2])   # Output: [0, 2, 4]
  print(my_list[::-1])  # Output: [4, 3, 2, 1, 0]
  ```

---

### 8. Memory Management

Understanding how Python manages memory helps avoid unintended behavior.

- **Lists as References:**
  ```python
  a = [1, 2, 3]
  b = a  # b references the same list
  b.append(4)
  print(a)  # Output: [1, 2, 3, 4]
  ```

- **Copying Lists:**
  ```python
  c = a.copy()  # Creates a new list
  c.append(5)
  print(a)  # Output: [1, 2, 3, 4]
  print(c)  # Output: [1, 2, 3, 4, 5]
  ```

- **Shallow vs Deep Copy:**
  ```python
  import copy
  a = [[1, 2], [3, 4]]
  b = a.copy()  # Shallow copy
  b[0][0] = 10
  print(a)  # Output: [[10, 2], [3, 4]]
  
  c = copy.deepcopy(a)  # Deep copy
  c[0][0] = 20
  print(a)  # Output: [[10, 2], [3, 4]]
  ```

---

### 9. Error and Exception Handling (Optional)

**Exception handling** manages errors in your code.

- **Try-Except Blocks:**
  ```python
  try:
      x = 1 / 0
  except ZeroDivisionError:
      print("Cannot divide by zero")
  ```

- **Multiple Except Clauses:**
  ```python
  try:
      x = int("abc")
  except ValueError:
      print("Invalid integer")
  except TypeError:
      print("Type error")
  ```

- **Finally Clause:**
  ```python
  try:
      x = 1 / 1
  except ZeroDivisionError:
      print("Cannot divide by zero")
  finally:
      print("This always runs")
  # Outputs: This always runs
  ```

---

### 10. Efficiency and Optimization

Writing efficient code improves performance.

- **Time Complexity Examples:**
  - List access: O(1)
  - List search: O(n)
  
- **Optimizing Loops:**
  ```python
  my_list = [1, 2, 3, 4]
  # Inefficient
  for i in range(len(my_list)):
      print(my_list[i])
  
  # Efficient
  for item in my_list:
      print(item)
  ```

- **Using Built-in Functions:**
  ```python
  total = sum(my_list)  # Faster than manual summation
  print(total)          # Output: 10
  ```

- **Avoiding Excessive Memory Use:**
  Use list comprehensions or generators for large datasets instead of building huge lists unnecessarily.

---

## Summary

This guide covers the core Python concepts with practical examples:
- **Lists and List Comprehensions**: Create, modify, and iterate efficiently.
- **Functions**: Organize code with parameters and returns.
- **Loops**: Repeat tasks with control.
- **Conditional Statements**: Add logic to your code.
- **Recursion**: Solve problems iteratively (optional).
- **Arithmetic Operations**: Perform calculations.
- **Indexing and Slicing**: Access data precisely.
- **Memory Management**: Handle data correctly.
- **Error Handling**: Manage exceptions (optional).
- **Efficiency**: Optimize for speed and space.

