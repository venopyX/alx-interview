# 🔐 0x01. Lockboxes

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python 3.7+"/>
  <img src="https://img.shields.io/badge/Algorithm-BFS-brightgreen.svg" alt="Algorithm"/>
  <img src="https://img.shields.io/badge/Data_Structure-List-orange.svg" alt="Data Structure"/>
</p>

## 📝 Problem Statement

You have `n` number of locked boxes in front of you, numbered sequentially from `0` to `n - 1`. Each box may contain keys to other boxes. Write a method that determines if all the boxes can be opened.

### Requirements:

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- You can assume all keys will be positive integers
  - There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

## 🧪 Test Cases

```python
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

## 🛠️ Setup & Testing

```bash
# Create and set permissions
touch ./0-lockboxes.py
chmod +x ./0-lockboxes.py

# Lint your code
pycodestyle ./0-lockboxes.py

# Test the solution
python3 ./main_0.py
```

## 💡 Solution Approach

The solution uses a breadth-first search (BFS) algorithm to:

1. Start with box 0 (initially unlocked)
2. Collect keys from each opened box
3. Try to open other boxes with collected keys
4. Track which boxes have been unlocked
5. Check if all boxes were successfully unlocked

> 👉 [View Solution Code](0-lockboxes.py)

## 📚 References

- [Python Lists Documentation](https://www.w3schools.com/python/python_lists.asp)
- [Breadth-First Search Algorithm](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Graph Traversal Techniques](https://www.geeksforgeeks.org/graph-traversals-bfs-and-dfs/)

## 👨‍💻 Author

This project was completed by [Gemechis Chala](https://github.com/venopyx).

<p align="center">
  <a href="https://github.com/venopyx"><img src="https://img.shields.io/badge/GitHub-@venopyx-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
</p>

<p align="center">
  <em>Special thanks to <a href="https://www.alxafrica.com/">ALX Africa Software Engineering</a> program for the project requirements.</em>
</p>
