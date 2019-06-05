"""
services/sms.py

SMS Service, provides alias to Twilio SMS client (can be used
as level of abstraction in the future) and should contain
all SMS messaging related code
"""

import os

from twilio.rest import Client as TwilioClient

from_phone_number = os.environ.get("SMS_SERVICE_PHONE_NUMBER")
sms_service = TwilioClient(os.environ.get("SMS_SERVICE_KEY"), os.environ.get("SMS_SERVICE_SECRET"))


