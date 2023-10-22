# Amirabbas_R.o

import requests

input = input("Enter your number (ex: 9350000000): ")

url = "https://api.divar.ir/v5/auth/authenticate"
payload = {"phone": "0"+input}
response = requests.post(url, json=payload)
print(response.status_code)
