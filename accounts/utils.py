import random
from twilio.rest import Client

# Twilio credentials
account_sid = 'AC5ea52ec31f08661af28a196946f1e308'
auth_token = 'd7c97be1aa6bbddd3f0d9ffa9f860502'
client = Client(account_sid, auth_token)

service_sid = 'VA6fc61732c1c63ec75d502530a31fdf8b'

client = Client(account_sid, auth_token)

def send_verification_code(phone_number):
    verification = client.verify.v2.services(service_sid).verifications.create(
        to=phone_number,
        channel="sms"
    )
    return verification.status

def verify_code(phone_number, code):
    verification_check = client.verify.v2.services(service_sid).verification_checks.create(
        to=phone_number,
        code=code
    )
    return verification_check.status
