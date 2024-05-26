from abc import ABC, abstractmethod
from typing import Dict


class UserEdit(ABC):
    @abstractmethod
    def user_edit(self, user_id: int) -> Dict:
        pass
