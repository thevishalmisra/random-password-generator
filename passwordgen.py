#random password generator
import random
import string
print("welcome to our password generator")
length=int(input("Entre the length of password you want: "))                 
lowerD=string.ascii_lowercase
upperD=string.ascii_uppercase
digitD=string.digits
symbolsD=string.punctuation
combine=lowerD+upperD+digitD+symbolsD
x=random.sample(combine,length)
print(x)



