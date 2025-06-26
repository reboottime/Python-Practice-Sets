# Python vs TypeScript Type Annotations Comparison

Python's type hints (introduced in Python 3.5+ and enhanced in later versions) are very similar to TypeScript's type annotations. Here's a comprehensive comparison:

## **Similarities between Python and TypeScript**

### 1. **Basic Type Annotations**

**Python:**

```python
name: str = "John"
age: int = 25
is_active: bool = True
```

**TypeScript:**

```typescript
name: string = "John";
age: number = 25;
isActive: boolean = true;
```

### 2. **Union Types (Multiple Possible Types)**

**Python (3.10+):**

```python
flight_number: str | None = None
user_id: int | str = "abc123"
```

**Python (3.5-3.9):**

```python
from typing import Union
flight_number: Union[str, None] = None
user_id: Union[int, str] = "abc123"
```

**TypeScript:**

```typescript
flightNumber: string | null = null;
userId: number | string = "abc123";
```

### 3. **Function Type Annotations**

**Python:**

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

**TypeScript:**

```typescript
function greet(name: string): string {
    return `Hello, ${name}`;
}
```

### 4. **Optional Parameters**

**Python:**

```python
def create_user(name: str, email: str | None = None) -> dict:
    return {"name": name, "email": email}
```

**TypeScript:**

```typescript
function createUser(name: string, email?: string): object {
    return { name, email };
}
```

## **Key Differences**

### 1. **Runtime Behavior**

- **Python**: Type hints are mostly for development tools and documentation - they don't affect runtime behavior
- **TypeScript**: Types are checked at compile time but removed in JavaScript output

### 2. **Syntax Differences**

**Python uses `|` for unions (3.10+):**

```python
value: str | int | None = None
```

**TypeScript uses `|` too:**

```typescript
value: string | number | null = null;
```

### 3. **Optional vs None/Null**

**Python:**

```python
# These are different concepts:
optional_param: str | None = None  # Can be string or None
def func(param: str | None = None): pass  # Default parameter
```

**TypeScript:**

```typescript
// Optional parameter with undefined
function func(param?: string): void { }

// Nullable parameter
function func(param: string | null): void { }
```

### 4. **Generic Types**

**Python:**

```python
from typing import List, Dict
items: List[str] = ["a", "b", "c"]
data: Dict[str, int] = {"count": 5}

# Python 3.9+
items: list[str] = ["a", "b", "c"]
data: dict[str, int] = {"count": 5}
```

**TypeScript:**

```typescript
items: string[] = ["a", "b", "c"];
data: { [key: string]: number } = { count: 5 };
// or
data: Record<string, number> = { count: 5 };
```

## **Real-World Example**

From the airline agent code:

```python
flight_number: str | None = None
```

This is equivalent to TypeScript's:

```typescript
flightNumber: string | null = null;
```

Both mean: "This variable can hold either a string value or None/null, and it starts as None/null."

## **Why Use Type Hints?**

1. **Better IDE support** - autocomplete, error detection
2. **Documentation** - makes code easier to understand
3. **Catch bugs early** - tools like `mypy` can check types before runtime
4. **Refactoring safety** - easier to change code without breaking things

## **Conclusion**

TypeScript checks types at build time, python check types at runtime.
 Python is an interpreted language, so technically everything happens at "runtime" .

- Runtime: When your program is actually executing.
- Build time: When code is prepared for execution. Python doesn't have traditional build time since it's interpreted, but there's an import/loading phase where modules are parsed.

**Python Type Checking**

- **Dynamic (Runtime)**: Python checks types when operations are performed. Errors happen during execution.

    ```python
    x = "hello" + 5  # TypeError at runtime
    ```

- **Static Type Hints**: Optional annotations that don't affect runtime behavior.

    ```python
    def greet(name: str) -> str:
        return f"Hello {name}"

    greet(123)  # Runs fine despite wrong type
    ```

- how to check before runtime
    **Static Type Checkers**: Tools like `mypy` check types before runtime.

    ```bash
    mypy script.py  # Catches type errors without running code
    ```

**Bottom line**: Python's built-in type checking happens at runtime. Type hints are optional metadata. Static type checking requires external tools and happens before execution.
