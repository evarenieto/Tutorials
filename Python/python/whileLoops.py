#password
import sys
master_pasword = 'potato'
password = input("please enter the super secret password?   ")
attempt_count = 1
while password != master_pasword:
    if attempt_count > 2:
        sys.exit('To many invalid password attempt.')
        #if we pass any value to sys.exit will be a error
    password = input("invalid, try again:")
    attempt_count += 1
print("welcome to secret town")
