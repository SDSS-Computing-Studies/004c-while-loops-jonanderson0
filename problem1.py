##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
un="admin"
pw="12345"
a = 0
a = int(a)

while a<3:
  b=input("un: ").strip()
  c=input("pw: ").strip()
  if b==user and c==password:
    print("Access granted")
    break
  else:
    print("Access denied")
    a = a+1
    a = int(a)
