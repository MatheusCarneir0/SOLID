from abc import ABC, abstractmethod
from aula4.domain.value_object.phone import Phone
from aula4.domain.value_object.email import Email

class NotifyViaEmail(ABC):
    @abstractmethod
    def send_message(self, message: str,  phone: Phone):
        pass


class NotifyViaCellphone(ABC):
    @abstractmethod
    def send_message(self, message: str,  email: Email):
        pass
