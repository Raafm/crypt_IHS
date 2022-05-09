from aux_func import *
from random import randint

class Cryptographer:
    def __init__(self,Key,Lock = None,N = None):
        self.key  = Key # inserido
        
        self.my_lock = Lock# deve ser enviado
        self.other_lock = None
        
        self.my_N    = None 
        self.other_N = None
        
        self.primes = None
    
    def generate_lock(self, Max = 2**10):
        if self.primes is None: self.primes = primes_generator(Max)
        
        Nprimes = len(self.primes)
    
        while True:
            # choose two primes: p and q
            prime_index = randint( Nprimes//2, Nprimes-1 )
            p = self.primes[  prime_index ]

            prime_index = randint( Nprimes//4, Nprimes//2 - 1 )
            q = self.primes[  prime_index ] 

            #choose key
            product = (p-1)*(q-1)
            
            if gcd(self.key,product) == 1:
                print("p = ",p)
                print("q = ",q)
                print("c = ",self.key)
                break
            
        self.my_N = p*q
        self.my_lock = modInverse(self.key,(p-1)*(q-1))       

    def set_lock(self,Lock,N):
        self.other_lock = Lock
        self.other_N    = N

    def encrypt(self, msg, Lock = None, N = None):
        if type(msg) != int:
            try:
                msg = int(msg)
            except :
                print(f"a mensagem: '{msg}' não pode ser convertida para int")
                return msg
        if (Lock is None) or (N is None): 
            Lock = self.other_lock
            N = self.other_N
        return str( modExp(msg,Lock,N) )

    def decrypt(self,cipher):

        if type(cipher) == int:
            return str(modExp(cipher,self.key,self.my_N))
        
        else:
            try:
                cipher = int(cipher) 
                return str(modExp(cipher,self.key,self.my_N))
            except:
                print(f"a mensagem: '{cipher}' não pode ser convertida para int")
                return cipher
        
        
    
    
if __name__ == "__main__":

    cry1 = Cryptographer(Key = 17)
    cry1.generate_lock()
    
    
    cry2 = Cryptographer(Key = 23)
    cry2.generate_lock()
    
    cry1.other_lock = cry2.my_lock
    cry2.other_lock = cry1.my_lock

    cry1.other_N = cry2.my_N
    cry2.other_N = cry1.my_N
    


    print()

    msg1 = 10
    print("msg1 = ",msg1)

    cipher1 = cry1.encrypt(msg1)
    print("cipher1 = ",cipher1)
    print("decrypted msg1 = ",cry2.decrypt(cipher1))

    print()

    msg2 = 12
    print("msg2 = ",msg2)

    cipher2 = cry2.encrypt(msg2)
    print("cipher2 = ",cipher2)
    print("decrypted msg2 = ",cry1.decrypt(cipher2))

    