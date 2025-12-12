from ABC import ABC, abstractmethod
from src.domain.value_object.phone import Phone
from src.domain.value_object.email import Email

class NotifyByCellPhone(ABC):
    """Protocolo abstrato para notificação via celular."""
    @abstractmethod
    def send_message(self, message: str, number: Phone):
        pass


class NotifyByEmail(ABC):
    """Protocolo abstrato para notificação por e-mail."""
    @abstractmethod
    def send_email(self, message: str, email: Email):
        pass

