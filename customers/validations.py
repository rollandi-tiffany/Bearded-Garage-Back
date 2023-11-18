from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()


def custom_validation(data):
    email = data["email"].strip()
    username = data["username"].strip()
    password = data["password"].strip()

    if not email or UserModel.objects.filter(email=email).exists():
        raise ValueError("Email failed. Try again")
    if not password or len(password) <9:
        raise ValueError(" Try again. Password needs to be 9 characters.")