import math

def isPrime(n):
    # Check if n is 1 or 0
    if n <= 1:
        return False
    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True
    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
  n = 7
  if(isPrime(n)): 
    print("true")
  else:
    print("false")
    
    
    
    """
    def sieve(n):
   
    #Create a boolean list to track prime status of numbers
    prime = [True] * (n + 1)
    p = 2

    # Sieve of Eratosthenes algorithm
    while p * p <= n:
        if prime[p]:
            
            # Mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)
    
    return res

if __name__ == "__main__":
    n = 35
    res = sieve(n)
    for ele in res:
        print(ele, end=' ')
    
    """
    
    """
    def powMod(x, n, M):
    res = 1

    # Loop until exponent becomes 0
    while n >= 1:
        
        # n is odd, multiply result by current x and take modulo
        if n % 2 == 1:
            res = (res * x) % M
            
            # Make n even
            n -= 1 
        else:
            
            # n is even, square the base and halve the exponent
            x = (x * x) % M
            n //= 2

    return res

if __name__ == "__main__":
    x, n, M = 3, 2, 4
    print(powMod(x, n, M))
    """
    