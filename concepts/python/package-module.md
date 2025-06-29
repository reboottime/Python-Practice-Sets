# Python Modules & Packages

## 📚 Core Concepts

### Module

- **Definition**: A single Python file (`.py`) containing code (functions, classes, variables)
- **Example**: `math_utils.py` is a module
- **Usage**:

```python
import math_utils
# or
from math_utils import add
```

### Package

- **Definition**: A directory containing multiple modules + `__init__.py` file
- **Purpose**: Organize related modules together
- **Structure**:

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

## 🔧 Creating a Module

Create a `.py` file:

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Use it:

```python
import math_utils
result = math_utils.add(5, 3)

# or
from math_utils import add
result = add(5, 3)
```

## 📦 Creating a Package

1. Create directory
2. Add `__init__.py` file (marks it as a package)
3. Add modules

Example structure:

```
calculator/
    __init__.py          # Entry point:similar the index.ts in ts 
    basic_ops.py         # Module with basic operations
    advanced_ops.py      # Module with advanced operations
```

## 🎯 What goes in `__init__.py`?

**Analogy**: `__init__.py` is like `index.ts` in TypeScript - it's the entry point for the folder!

### Option 1: Empty (minimal)

```python
# __init__.py - completely empty file
```

Usage: `from calculator.basic_ops import add`

### Option 2: Import for convenience

```python
# __init__.py
from .basic_ops import add, subtract, multiply, divide
from .advanced_ops import power, sqrt, factorial
```

Usage: `from calculator import add, power`  # Much cleaner!

### Option 3: Control imports with **all**

```python
# __init__.py
from .basic_ops import add, subtract, multiply, divide
from .advanced_ops import power, sqrt, factorial

# Define what gets imported with "from calculator import *"
__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt']
```

### Option 4: Package metadata

```python
# __init__.py
"""Calculator package for mathematical operations."""

__version__ = "1.0.0"
__author__ = "Your Name"

from .basic_ops import add, subtract, multiply, divide
from .advanced_ops import power, sqrt, factorial

# Package-level initialization
print(f"Calculator package v{__version__} loaded")

__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt']
```

## 🚀 Publishing a Package

**Analogy**: `setup.py` is like `package.json` in Node.js - defines package metadata and dependencies!

### 1. Package Structure

```
my_awesome_package/
    setup.py             # Like package.json
    README.md
    my_awesome_package/
        __init__.py
        core.py
```

### 2. Create setup.py

```python
from setuptools import setup, find_packages

setup(
    name="my-awesome-package",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests>=2.25.0",  # Like dependencies in package.json
    ],
)
```

### 3. Install Build Tools

```bash
pip install build twine
```

**What this does**:

- `build`: Creates distribution packages (.whl and .tar.gz files)
- `twine`: Securely uploads packages to PyPI
- Both are essential tools for packaging and publishing

### 4. Build and Publish

```bash
# Build the package
python -m build

# Upload to Test PyPI first (recommended)
twine upload --repository testpypi dist/*

# Then upload to real PyPI
twine upload dist/*
```

## 🔄 TypeScript Analogies Summary

| Python | TypeScript | Purpose |
|--------|------------|----------|
| `__init__.py` | `index.ts` | Entry point for folder/package |
| `setup.py` | `package.json` | Package metadata & dependencies |
| `pip install` | `npm install` | Install packages |
| PyPI | npm registry | Package repository |

## 💡 Key Takeaways

1. **Module** = single `.py` file
2. **Package** = directory with `__init__.py` + modules
3. `__init__.py` controls what gets imported (like `index.ts`)
4. `setup.py` defines package info (like `package.json`)
5. Use `build` and `twine` to publish packages
6. Test on TestPyPI first, then publish to real PyPI

## 🎯 Quick Commands Reference

```bash
# Create and publish workflow
pip install build twine          # Install tools
python -m build                  # Build package
twine upload --repository testpypi dist/*  # Test upload
twine upload dist/*              # Real upload

# Install your published package
pip install my-awesome-package
```
