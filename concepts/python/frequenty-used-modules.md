# Frequently used modules

- [asyncio](https://docs.python.org/3/library/asyncio.html)
  - what problem does it solve?: asyncio is a library to write concurrent code using the async/await syntax. Asyncio is ofen a perfect fit for `IO-bound` and high level structured network code.
  - If I'm not familiar with other similar terms, [where to learn it conceptually](https://www.youtube.com/watch?v=K56nNuBEd0c)
  - terms to understand: 
    - synchronous & asynchronous
    - [subroutine and coroutine](https://youtu.be/K56nNuBEd0c?si=KlwKIRFeVu3Y3rPR&t=111)
      - subroutine: can't be stoped and paused
      - coroutine: can be stoped or paused. coroutine maintain state between pauses
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

- [] need deep recap about asynchronous programming