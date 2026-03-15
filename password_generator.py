import random
import string
def password_generator():
 a=int(input("enter the length of password you want to generate"))
 characters=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
 password=""
 for i in range(a):
  password+=random.choice(characters)
 return password
p=password_generator()
print(p)
  