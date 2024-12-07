"""
| Feature                | **List**                              | **Tuple**                             | **Set**                                |
|------------------------|---------------------------------------|---------------------------------------|----------------------------------------|
| **Definition**         | Ordered, mutable collection of items | Ordered, immutable collection of items | Unordered, mutable collection of unique items |
| **Syntax**             | `[1, 2, 3]`                          | `(1, 2, 3)`                          | `{1, 2, 3}`                            |
| **Mutability**         | Mutable (can change after creation)  | Immutable (cannot change after creation) | Mutable (can add or remove items, but elements must be immutable) |
| **Duplicates**         | Allowed                              | Allowed                              | Not allowed                            |
| **Order**              | Preserves order of elements          | Preserves order of elements          | Does not guarantee any order           |
| **Indexing & Slicing** | Supported                            | Supported                            | Not supported                          |
| **Usage Scenario**     | When frequent modifications are needed | When data needs to be immutable      | When uniqueness of elements is required |
| **Adding Elements**    | `list.append()` or `list.insert()`   | Not allowed (create a new tuple)     | `set.add()` or `set.update()`          |
| **Removing Elements**  | `list.remove()` or `list.pop()`      | Not allowed                          | `set.remove()` or `set.discard()`      |
| **Duplicates Handling**| Allows duplicates                   | Allows duplicates                   | Automatically removes duplicates       |
| **Speed** (Membership Test) | Slower than sets (O(n))           | Slower than sets (O(n))              | Faster for membership tests (O(1))     |
| **Hashability**        | Not hashable                         | Hashable if immutable elements       | Hashable but only for immutable elements |
| **Iteration**          | Iterates in insertion order          | Iterates in insertion order          | Iterates in arbitrary order            |
"""
