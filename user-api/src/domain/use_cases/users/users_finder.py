from abc import ABC, abstractmethod
from typing import Dict


class UsersFinder(ABC):
    @abstractmethod
    def users_finder(self) -> Dict:
        pass
