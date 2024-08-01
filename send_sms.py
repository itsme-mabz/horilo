import os
from twilio.rest import Client

account_sid = 'AC5ea52ec31f08661af28a196946f1e308'
auth_token = 'd7c97be1aa6bbddd3f0d9ffa9f860502'
client = Client(account_sid, auth_token)

service = client.verify.v2.services.create(
    friendly_name="Horlio"
)

SID = service.sid
print(SID)

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(
   SID
).verifications.create(to="+14696659865", channel="sms")

print(verification.status)
print(verification)
