#!/usr/bin/python3
"""
Module that determines if all boxes can be opened.
Each box is numbered sequentially from 0 to n - 1 and may
contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists where each inner list
            contains keys (integers) to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)

    if n == 1:
        return True

    unlocked = [False] * n
    unlocked[0] = True

    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if not isinstance(key, int) or key < 0 or key >= n:
                continue

            if not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
