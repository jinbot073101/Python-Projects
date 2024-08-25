import random
import math
import time

def is_prime(n):
    if n == 2:
        return True  
    if n % 2 == 0:
        return False  
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

number = random.randint(2, 1000)
while not is_prime(number):
    number = random.randint(2, 1000)

number2 = random.randint(2,1000)
while not is_prime(number2):
    number2 = random.randint(2,1000)
    

phi_result = (number - 1) * (number2 - 1)

public_key = random.randint(2,1000)

private_key = public_key**(phi_result - 1) % phi_result

print("\nGenerating keys......")
time.sleep(3)

print(f"""
      Public key generated: {public_key} 
      Private key generated: {private_key}
      """)
