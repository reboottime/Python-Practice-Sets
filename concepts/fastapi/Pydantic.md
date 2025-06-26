# Data Format validation using `Pydantic`

## What is `Pydantic`?

**Pydantic** is a Python library that provides data validation, serialization, and documentation using Python type hints. It's like having a "smart assistant" that checks your data automatically.

## What is BaseModel?

`BaseModel` is the main class from Pydantic that you inherit from to create data classes

### Basic Example

```python
from pydantic import BaseModel

# Regular Python class (basic)
class PersonBasic:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Pydantic class (with superpowers!)
class PersonPydantic(BaseModel):
    name: str
    age: int
```

## Why Use BaseModel? (The Superpowers!)

### 1. **Automatic Type Validation**

```python
# This will work fine
person = PersonPydantic(name="Alice", age=25)

# This will raise an error automatically!
person = PersonPydantic(name="Alice", age="twenty-five")  # ❌ Error!
# ValidationError: Input should be a valid integer
```

### 2. **Easy JSON Conversion**

```python
person = PersonPydantic(name="Alice", age=25)

# Convert to dictionary/JSON
data = person.model_dump()
print(data)  # {'name': 'Alice', 'age': 25}

# Create from dictionary/JSON
data = {"name": "Bob", "age": 30}
person = PersonPydantic.model_validate(data)
```

### 3. **Optional Fields with Default Values**

```python
class AirlineAgentContext(BaseModel):
    passenger_name: str | None = None  # Can be string or None, defaults to None
    confirmation_number: str | None = None
    seat_number: str | None = None
    flight_number: str | None = None
    account_number: str | None = None
```

### 4. **Runtime Type Checking**

Unlike regular Python classes, `Pydantic` checks types when you create or modify objects:

```python
ctx = AirlineAgentContext()
ctx.passenger_name = "John Smith"  # ✅ Works
ctx.passenger_name = 123          # ❌ Will warn/error in strict mode
```

## The Wrapper Pattern Explained

In the airline code, you see this confusing pattern:

```python
context.context.confirmation_number = "ABC123"
```

## Real-World Benefits

### 1. **API Development**

```python
# When receiving data from web requests
class UserRegistration(BaseModel):
    email: str
    password: str
    age: int

# Pydantic automatically validates incoming JSON data
# and tells you exactly what's wrong if it's invalid
```

### 2. **Configuration Management**

```python
class DatabaseConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    username: str
    password: str

# Load from environment variables or config files
# with automatic validation
```

### 3. **Data Processing**

```python
class FlightData(BaseModel):
    flight_number: str
    departure_time: datetime
    passengers: list[str]

# Process data from multiple sources with confidence
# that the structure is correct
```

## Summary

**Pydantic and BaseModel provide:**

- ✅ Automatic data validation
- ✅ Easy JSON serialization/deserialization  
- ✅ Clear error messages
- ✅ Type safety at runtime
- ✅ Great IDE support and autocompletion
- ✅ Documentation through type hints

**Think of BaseModel as:**
> A "smart" data class that automatically checks your data, converts between formats, and tells you when something is wrong - before your program crashes!
