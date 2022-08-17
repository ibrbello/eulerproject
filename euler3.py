import math as m
def isprime (num):
    for i in range(2,int(m.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
    
def largest_prime_factor (num): # Not always right
    for factor in range(int(m.sqrt(num)),2,-1):
        if num % factor == 0 and isprime(factor) == True:
            return factor
    
print(isprime(600851475143))
print(largest_prime_factor(600851475143)) # Correct Answer
print(largest_prime_factor(77)) # Incorrect Answer
