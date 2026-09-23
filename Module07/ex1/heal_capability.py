from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: "HealCapability | None" = None) -> str:
        """Return a string describing the healing action."""
        raise NotImplementedError
