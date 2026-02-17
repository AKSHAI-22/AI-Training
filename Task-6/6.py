from abc import ABC, abstractmethod
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):

    def send(self, message):
        print("Sending Email:", message)

class SMSNotification(Notification):

    def send(self, message):
        print("Sending SMS:", message)

class NotificationSender:

    def notify(self, notification, message):
        notification.send(message)

sender = NotificationSender()

email = EmailNotification()
sms = SMSNotification()

sender.notify(email, "Your order is confirmed!")
sender.notify(sms, "OTP: 123456")
