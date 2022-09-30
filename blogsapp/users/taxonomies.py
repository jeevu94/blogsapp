from djchoices import ChoiceItem, DjangoChoices


class UserRole(DjangoChoices):
    customer = ChoiceItem(1, "Customer")
    admin = ChoiceItem(2, "Admin")
