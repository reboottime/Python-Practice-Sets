# Data Structure

## List, Tuple & Dictionary

See symbols, `*` and `**`

Keywords: ordered, immutable

- List  & Tuple: A tuple is a built-in data type in Python that stores an ordered collection of items. It's similar to a list, but with one key difference: tuples are immutable (cannot be changed after creation).
- Dictionary: not ordered and is mutable

```python
    student = {"name": "Alice", "age": 20, "grade": "A"}

    # Accessing values
    print(student["name"])        # "Alice"
    print(student.get("age"))     # 20
    print(student.get("height", "Unknown")) 

```