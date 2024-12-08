"""

| **Feature**            | **List**                              | **Tuple**                              | **Set**                                | **Dictionary**                          |
|------------------------|---------------------------------------|----------------------------------------|----------------------------------------|-----------------------------------------|
| **Definition**         | Ordered, mutable collection of items  | Ordered, immutable collection of items | Unordered, mutable collection of unique items | Unordered, mutable collection of key-value pairs |
| **Syntax**             | `[1, 2, 3]`                          | `(1, 2, 3)`                           | `{1, 2, 3}`                            | `{"key1": "value1", "key2": "value2"}`  |
| **Mutability**         | Mutable (can change after creation)   | Immutable (cannot change after creation) | Mutable (can add or remove items, but elements must be immutable) | Mutable (keys must be immutable, values can be mutable) |
| **Duplicates**         | Allowed                              | Allowed                               | Not allowed                            | Keys must be unique; values can have duplicates |
| **Order**              | Preserves order of elements (Python 3.7+) | Preserves order of elements           | Does not guarantee order               | Preserves insertion order (Python 3.7+)         |
| **Indexing & Slicing** | Supported                             | Supported                             | Not supported                          | Keys can be used for direct access; slicing not supported |
| **Usage Scenario**     | When frequent modifications are needed | When data needs to be immutable       | When uniqueness of elements is required | When key-value associations are required |
| **Adding Elements**    | `list.append()` or `list.insert()`    | Not allowed (create a new tuple)      | `set.add()` or `set.update()`          | `dict[key] = value`                     |
| **Removing Elements**  | `list.remove()` or `list.pop()`       | Not allowed                           | `set.remove()` or `set.discard()`      | `dict.pop()` or `del dict[key]`         |
| **Duplicates Handling**| Allows duplicates                    | Allows duplicates                     | Automatically removes duplicates       | Keys must be unique; duplicate values allowed |
| **Speed (Membership Test)** | Slower than sets (O(n))           | Slower than sets (O(n))               | Faster for membership tests (O(1))     | Faster for key lookups (O(1))           |
| **Hashability**        | Not hashable                          | Hashable if all elements are immutable | Hashable but only if all elements are immutable | Hashable keys; values can be mutable or immutable |
| **Iteration**          | Iterates in insertion order           | Iterates in insertion order           | Iterates in arbitrary order            | Iterates over keys by default           |
| **Memory Efficiency**  | Uses more memory for dynamic resizing | More memory efficient due to immutability | Less memory efficient when storing many elements | Uses more memory for maintaining key-value mappings |
| **Nesting**            | Can nest any data type (lists, tuples, sets) | Can nest any data type                | Can only nest immutable data types     | Can nest any data type as keys or values, but keys must be hashable |
| **Common Operations**  | Extensive operations like sort, reverse | Basic operations (concatenation, slicing) | Operations like union, intersection, and difference | Operations like key lookup, addition, deletion |
| **Applications**       | Dynamic arrays, frequently updated data | Fixed collections, read-only data     | Collections with unique items and fast membership checks | Mappings for fast retrieval using keys  |
"""

