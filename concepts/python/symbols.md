# Symbols

## `*` and `**`

The `*args` and `**kwargs` in the wrapper function are Python's mechanisms for handling variable numbers of arguments:

## `*args` (Positional Arguments)

The `*` collects any number of positional arguments into a tuple:

```python
def example(*args):
    print(args)
    print(type(args))

example(1, 2, 3, "hello")
# Output: (1, 2, 3, 'hello')
# Output: <class 'tuple'>
```

## `**kwargs` (Keyword Arguments)

The `**` collects any number of keyword arguments into a dictionary:

```python
def example(**kwargs):
    print(kwargs)
    print(type(kwargs))

example(name="Alice", age=25, city="Beijing")
# Output: {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
# Output: <class 'dict'>
```

## In Decorator Context

In the decorator's wrapper function, `*args` and `**kwargs` allow the decorator to work with functions that have any number of arguments:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        # Pass all arguments to the original function
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

# Works with functions having different signatures:
@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

# Both work seamlessly:
add(3, 5)                           # args=(3, 5), kwargs={}
greet("Alice", greeting="Hi")       # args=("Alice",), kwargs={"greeting": "Hi"}
```
