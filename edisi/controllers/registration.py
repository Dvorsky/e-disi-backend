"""
controllers/registration.py

Handling generation of verification codes and verifying them.
"""

from flask import Request

from edisi.services.sms import sms_service, from_phone_number


def get_welcome_text():
    return f"Tvoj e-Disi aktivacijski ključ je:\n{6969}"


def handle_register(request: Request):
    """
    Method for handling user registration attempt. It expects
    request with phoneNumber property which will be used for
    sending SMS verification key.

    TODO: generate key and store it in database
    """
    if request.method != "POST":
        return

    content = request.json

    phone_number = content['phoneNumber']

    message = sms_service.messages.create(
        to=phone_number,
        from_=from_phone_number,
        body=get_welcome_text()
    )

    print(message.sid)
