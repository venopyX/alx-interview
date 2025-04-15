# Pascal's Triangle Generator

Generates Pascal's triangle up to the specified number of rows. Returns an empty list if `n <= 0`.

**Example:**
```py
from 0-pascal_triangle import pascal_triangle

print_triangle(pascal_triangle(5))
```

# Output:

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
