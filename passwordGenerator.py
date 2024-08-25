import random
import string
import time

lenght = int(input("Password lenght: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(lenght))
print('\nGenerating password...\n')
time.sleep(1)
print(f'Password generated: {password}')