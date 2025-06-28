
from enum import Enum

class Agent:
    def __init__(self, name: str):
        self.name = name
        
class TriageAgent(Agent):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = 'Triage agent'

class LifeCoachAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name)
        self.description = 'life coach keeps you on track'


class PersonalHealthCoachAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name)
        self.description = 'health coach helps you have a happy healthy life'
        
class ExecutiveAssitant(Agent):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = 'executive assitant, your executive asistant! you are your own CEO'
        
class PersonalAssitant(Agent):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = 'Your personal life assistant. Helps you, your wife and family, lol'

class AnalysisRange(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'


class AnalysisEngine:
    def __init__(self, name: str):
        self.name = name

    def analyze(self, range: AnalysisRange):
        pass