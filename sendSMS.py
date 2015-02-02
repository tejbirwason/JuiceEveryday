from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC487917c9de6d43515d79f9b4bb18b39a"
auth_token  = "c24fbbe33c17e3e1d585bc997ae65b28"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Sup bro!",
    to="+12063269548",    # Replace with your phone number
    from_="+12018775705",	# Replace with your Twilio number
    media_url=['http://juicerecipes.com/recipes/adios-coffee-19/infographic.png']) 
print message.sid