from abc import ABC, abstractmethod
from typing import Optional

class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Optional["HealCapability"] = None) -> str:
        "Returns a string describing the cure."
        raise NotImplementedError

    