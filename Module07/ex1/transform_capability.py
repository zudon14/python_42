from abc import ABC, abstractmethod

class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed : bool = False

    @abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        raise NotImplementedError
