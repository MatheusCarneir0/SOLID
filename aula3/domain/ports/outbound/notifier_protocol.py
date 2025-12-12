from abc import ABC, abstractmethod

class NotifyByCellPhone(ABC):
    @abstractmethod
    def send_message(self, message: str, number: str):
        pass


class NotifyByEmail(ABC):
    @abstractmethod
    def send_message(self, message: str, email: str):
        pass