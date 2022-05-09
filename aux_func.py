from random import randint

# Iterative Function to calculate (a^c) in O(log c)
def modExp(a, c, N) :
    
    cipher = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    a = a % N
     
    if (a == 0) :
        return 0
 
    while (c > 0) :
         
        # If c is odd, multiply
        # a with result
        if (c & 1) == 1 :
            cipher = (cipher * a) % N
 
        # c must be even now
        c = c >> 1 
        a = (a * a ) % N
         
    return cipher

def decrypt(b,d,N):
    return modExp(b,d,N)

def primes_generator(Max = 2**10):
    # if the number is greater than 2**10
    # set Max (max number to 2**10)
    if Max > 2**10: print("MAX PRIME <= {2**10-1}")
        
    is_prime = list(True for _ in range(Max))
    for n in range(2,Max):
        if not is_prime[n]: continue
        
        for multiple in range(2*n,Max,n):
            is_prime[multiple] = False
            
    is_prime[0] = is_prime[1] = False
    primes = [ ]
    for num , e_primo in enumerate(is_prime):
        
        if e_primo:
            primes.append(num)

    return primes
            
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



def modInverse(a, m):
    m0 = m
    y  = 0
    x  = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

if __name__ == "__main__":
    
    primes = primes_generator()
    Nprimes = len(primes)
    while True:
        # choose two primes: p and q
        prime_index = randint( Nprimes//2, Nprimes-1 )
        p = primes[  prime_index ]

        prime_index = randint( Nprimes//4, Nprimes//2 - 1 )
        q = primes[  prime_index ] 
        p,q =23,29
        #choose key
        product = (p-1)*(q-1)
        c = 17
        if gcd(c,product) == 1:
            print("p = ",p)
            print("q = ",q)
            print("c = ",c)
            break
            
    print("p = ",p)
    print("q = ",q)
    print("c = ",c)
    N = p*q
    d = modInverse(c,(p-1)*(q-1))
    msg = 10
    print("1 = ", (c*d)%product)
    print((msg**c)%N, " = ", modExp(msg,c,N))
    print((((msg**c)%N)**d)%N, " = ", modExp(modExp(msg,c,N),d,N))
    print("\n\n")
    print("msg: ",msg)
    cipher = modExp(msg,c,N)
    print("msg crypted:  ",cipher)
    print("msg original: ",modExp(cipher,d,N))

