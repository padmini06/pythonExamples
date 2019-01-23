#!/usr/bin/python3
"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import random
import string

x=random.randint(0,9)
char_lc=random.choice(string.ascii_lowercase)
char_uc=random.choice(string.ascii_uppercase)

print(x)
print(char_lc)
print(char_uc)

print(''.join(random.SystemRandom().choice(string.ascii_uppercase+string.ascii_lowercase + string.digits) for _ in range(8)))

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)