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

un = ""
pw = ""

while un != "admin" and pw != "12345":
  un = input("enter username")
  pw = input("enter password")
  if un != "admin" and pw != "12345" :
    print("Access danied")
    
print("Access granted")


