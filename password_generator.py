#import necessary modules
import string 
import random

print("Hello !, Welcome to the password generator.")

#input the length of the password
p_length = int(input("Enter the length of password you want.\n"))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbol = string.punctuation

#combine the data 
All = lower+upper+digit+symbol

#create the password
password = "".join(random.sample(All,p_length))

#print the password
print("Here is  your {} digit password : {}\nThankyou!".format(p_length,password))
