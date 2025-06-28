# Type Safe

- Define Enum

> Python has built-in support for enumerations (Enums) starting from Python 3.4.

```python
from enum import Enum

class AnalysisRange(Enum):
    SHORT_TERM = "short_term"
    MEDIUM_TERM = "medium_term"
    LONG_TERM = "long_term"
    FULL_RANGE = "full_range"

class AnalysisEngine:
    def __init__(self, name: str):
        self.name = name

    def analyze(self, range: AnalysisRange):
        pass
```