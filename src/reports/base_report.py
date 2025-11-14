from abc import ABC, abstractmethod
from typing import List, Dict

class BaseReport(ABC):
    
    @abstractmethod
    def calculate(self, data: List[Dict]) -> List[Dict]:
        pass
    
    @abstractmethod
    def display(self, results: List[Dict]):
        pass
    
    def generate(self, data: List[Dict]):
        results = self.calculate(data)
        self.display(results)
