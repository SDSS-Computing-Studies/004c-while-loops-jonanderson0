#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""


if "admin" in username:
  print("Enter password")
else:
  print("invalid user")

if "12345password" in password:
  print("Access granted")
