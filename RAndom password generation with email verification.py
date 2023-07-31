# @: Rupam Das, 31.07.2023
import string
import random
import os
import math
import smtplib
import ssl
from email.message import EmailMessage

length = int(input("Enter password length: "))

print('''Choose character set for password from these :
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""


while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		
		characterList += string.ascii_letters
	elif(choice == 2):
		
		
		characterList += string.digits
	elif(choice == 3):
		
		
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []
# otp ={}
for i in range(length):
	randomchar = random.choice(characterList)
	password.append(randomchar)
print("The random password is " + "".join(password))
# otp = password + " is your OTP"
ms= password
msg= ''.join([str(elem) for elem in ms])
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Sender mail", "App password")
emailid = input("Enter reciver email id : ")
s.sendmail('Your passWord-',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == msg:
    print("Verified")
else:
    print("Please Check your OTP again")