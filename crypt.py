from random import randint

# Iterative Function to calculate (a^c) in O(log c)
def encrypt(a, c, N) :
    cipher = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    a = a % N
     
    if (a == 0) :
        return 0
 
    while (c > 0) :
         
        # If c is odd, multiply
        # a with result
        if (c and 1) == 1 :
            cipher = (cipher * a) % N
 
        # c must be even now
        c /= 2 
        a = (a **2 ) % N
         
    return cipher

def decrypt(b,d,N):
    return encrypt(b,d,N)

def prime_generator(SIZE = 2**10):
    # if the number is greater than 2**10
    # set SIZE (max number to 2**10)
    if SIZE > 2**10: print("MAX PRIME <= {2**10-1}")
        
    is_prime = list(True for _ in range(SIZE))
    for n in range(1,int(  SIZE**(1/2)  )):
        if not is_prime[n]: continue
        
        for multiple in range(2*n,SIZE,n):
            is_prime[multiple] = False

    primes = [ ]
    for num , e_primo in is_prime[2:]:
        if e_primo:
            primes.append(num)

    Nprimes = len(primes)
    primo = primes[  randint( Nprimes//2,Nprimes )  ]

    return primo
            
def gcd(a, b):
    if(a == 0):
        return b
    elif b == 0:
        return a
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a

def no_common_factor():
    NotImplemented


def generate_keys():
    # c has no common factors with (p-1)(q-1)
    c = no_common_factor()
    gcd()
    
    p = prime_generator()
    d = c%((p-1)*(q-1)) # d is the inverse multiplicative of c
    
    
    return p,c,d

p = 13
q = 17
N = p*q
c = 7
d = c%((p-1)*(q-1))
print("msg: ",12)
cipher = encrypt(12,c,N)
print("msg crypted: ",cipher)
print("msg original: ",decrypt(cipher,d,N))

