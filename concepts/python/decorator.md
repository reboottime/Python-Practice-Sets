# Decorators

## 基本概念

Python 装饰器是一种设计模式，它允许你在不修改原函数代码的情况下，为函数添加额外的功能。装饰器本质上是一个接受函数作为参数并返回新函数的高阶函数。

装饰器使用 `@` 符号语法，放在函数定义之前：

```python
@decorator_name
def function_name():
    pass
```

这等价于：

```python
def function_name():
    pass
function_name = decorator_name(function_name)
```

## 简单示例

```python
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

输出：

```sh
函数执行前
Hello!
函数执行后
```

## 带参数的装饰器

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数 {func.__name__}")
        result = func(*args, **kwargs)
        print("函数执行完毕")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 5)  # 输出装饰器信息，返回 8
```

## 常见用途

装饰器常用于日志记录、性能监控、权限验证、缓存等场景。比如计时装饰器：

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)  # 保持原函数的元信息
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "完成"
```

装饰器是Python中非常强大的特性，能让代码更加简洁和模块化。
