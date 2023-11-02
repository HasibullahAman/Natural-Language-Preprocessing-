import re

phoneNumber = "0t9-555-1212"

if re.search('\d{3}-\d{3}-\d{4}',phoneNumber):
    print("Correct Phone Number")
else:
    print("Incorrect phone number")