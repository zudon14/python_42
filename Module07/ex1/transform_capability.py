from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        # Persistent state: it changes what attack() does.
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Enter the transformed state and describe it."""
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        """Leave the transformed state and describe it."""
        raise NotImplementedError
