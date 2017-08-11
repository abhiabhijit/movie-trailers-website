from twilio.rest import TwilioRestClient

account_sid = "AC7b86a3bc8a58ccff9182da55c6b5f161" # Your Account SID from www.twilio.com/console
auth_token  = "0c5b5ac9bdfc4abe36ba4a6c42224d4c "  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body=" AC OFF CHEYODHU ",
    to="+919849467725",    # Replace with your phone number
    from_="+19032005455") # Replace with your Twilio number

print(message.sid)

