# Data Structure

According aggregated information from Claude, Python 3.12 and Python 3.11 are currently the most widely used versions Python Developers Survey 2024 is now open: respond and share! - PSF - Discussions on Python.org, with Python 3.11 reaching 27% adoption approximately nine months after release.

So this note do not consider any Pyton version older than 3.10

## Built in Data Structure in Python

- Evaluation Aspects:

  | Trait Name | List | Tuple | Array | Set | Dict |
  |-------|------|-------|-------|-----|------|
  | Ordered | ✓ | ✓ | ✓ | ✗ | ✓* |
  | Mutable | ✓ | ✗ | ✓ | ✓ | ✓ |
  | Duplicates | ✓ | ✓ | ✓ | ✗ | ✗** |
  | Indexed | ✓ | ✓ | ✓ | ✗ | ✗*** |
  | Homogeneous | ✗ | ✗ | ✓ | ✗ | ✗ |
  | Hashable | ✗ | ✓ | ✗ | ✗ | ✗ |

- Explanation of above terms
  - `Indexed`: Indexed means you can access elements using their position number (index).
  - `Homogeneous`: means all elements must be of the same data type
  - `Hashable`: means an object has a hash value that never changes during its lifetime.
  - Notes for Dict:
    - *Ordered since Python 3.7+ (insertion order is preserved)
    - **No duplicate keys (values can be duplicated)
    - ***Key-based access, not indexed by position
- Built-in collection types in Python
  - list - `[1, 2, 3]`
  - tuple - `(1, 2, 3)`
  - set
    - set - `{1, 2, 3}`
    - frozenset - `frozenset([1, 2, 3])`
  - dict - `{'key': 'value'}`
  - str (string) - `"hello"`
  - bytes - `b"hello"`
  - bytearray - `bytearray(b"hello")`
  
Array is not built-in to Python.

## Grammar Tricks

### Terms to understand

**iterable**: An iterable is any Python object that can be looped over (iterated through) one element at a time. It is similar to the `iterable` concept in JavaScript.

### Grammar sugar

- `*`: unpack an iterable in to params of a function. For example

```python
  tasks = (fetchUserById, fetchReportOfUser)
  results = await asyncio.gather(*tasks)
```

- `**`unpacking dictionary

```python
# Function call with dictionary unpacking
def greet(name, age, city):
    print(f"Hi {name}, age {age}, from {city}")

person = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# These are equivalent:
greet(**person)                           # Unpacks dictionary
greet(name='Alice', age=30, city='NYC')   # Direct keyword arguments
```
