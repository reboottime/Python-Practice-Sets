# json package

## Core Methods

### 1. `json.dumps()` - Python object to JSON string

```python
import json

# Basic usage
data = {"name": "John", "age": 30}
json_string = json.dumps(data)
# Output: '{"name": "John", "age": 30}'

# Pretty printing
json_string = json.dumps(data, indent=2)
# Formatted with indentation

# Custom separators
json_string = json.dumps(data, separators=(',', ':'))
# Compact format without spaces

# Sort keys
json_string = json.dumps(data, sort_keys=True)
```

### 2. `json.loads()` - JSON string to Python object

```python
# Parse JSON string
json_string = '{"name": "John", "age": 30}'
data = json.loads(json_string)
# Output: {'name': 'John', 'age': 30}

# Handle errors
try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

### 3. `json.dump()` - Write Python object to file

```python
# Write to file
data = {"users": [{"name": "John", "age": 30}]}
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

### 4. `json.load()` - Read JSON from file

```python
# Read from file
with open('data.json', 'r') as f:
    data = json.load(f)
```

## Data Type Mappings

| Python | JSON |
|--------|------|
| dict | object |
| list, tuple | array |
| str | string |
| int, float | number |
| True | true |
| False | false |
| None | null |

## Common Parameters

- `indent`: Pretty print with indentation (int or string)
- `sort_keys`: Sort dictionary keys (bool)
- `separators`: Custom separators tuple `(',', ':')`
- `ensure_ascii`: Escape non-ASCII characters (bool, default True)
- `skipkeys`: Skip invalid dict keys (bool)

## Practical Examples

### Custom JSON Encoder

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"timestamp": datetime.now()}
json_string = json.dumps(data, cls=DateTimeEncoder)
```

### Working with APIs

```python
import json
import requests

# Sending JSON
payload = {"username": "john", "email": "john@example.com"}
response = requests.post(url, json=payload)  # Automatically converts to JSON

# Receiving JSON
response = requests.get(url)
data = response.json()  # Automatically parses JSON response
```

### Validation and Error Handling

```python
def safe_json_load(json_string):
    try:
        return json.loads(json_string), None
    except json.JSONDecodeError as e:
        return None, str(e)

data, error = safe_json_load('{"invalid": json}')
if error:
    print(f"JSON error: {error}")
```
