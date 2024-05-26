from abc import ABC, abstractmethod
from typing import Dict


class UserDelete(ABC):
    @abstractmethod
    def user_delete(self, user_id: int) -> Dict:
        pass
