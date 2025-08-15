# Frequently used modules


## modules

- [asyncio](./asyncio.md)
- [dataclass](https://docs.python.org/3/library/dataclasses.html):
  - what problem does it solve?: A decorator that reduces boilerplate code by automatically generating:
    - methods 
      - `__init__` constructor
      - `__repr__` method
      - `__eq__` method
    - Optional: frozen instances (immutable)
    - Optional: ordering methods (`__lt__`, `__gt__`, etc.)
  - related programming terms
    - immutable and freeze
    - constructor
  - usage

  ```python
    @dataclass(frozen=True, order=False)
    class Point:
        x: int
        y: int

    point = Point(1, 2)
    # point.x = 5  # Error! Cannot modify frozen dataclass
  ```

## Todos

- [x] need deep recap about asynchronous programming
