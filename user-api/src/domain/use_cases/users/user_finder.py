from abc import ABC, abstractmethod
from typing import Dict


class UserFinder(ABC):
    @abstractmethod
    def user_finder(self, user_id: int) -> Dict:
        pass
