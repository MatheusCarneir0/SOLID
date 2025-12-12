from abc import ABC, abstractmethod

class GetRepositoryProtocol(ABC):
    @abstractmethod
    def read(self, item_id: str):
        pass


class GetAllRepositoryProtocol(ABC):
    @abstractmethod
    def read_all(self):
        pass


class InsertRepositoryProtocol(ABC):
    @abstractmethod
    def save(self, data: dict):
        pass


class UpdateRepositoryProtocol(ABC):
    @abstractmethod
    def update(self, item_id: str, data: dict):
        pass


class DeleteRepositoryProtocol(ABC):
    @abstractmethod
    def delete(self, item_id: str):
        pass