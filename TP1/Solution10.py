# a/ write is_prime fuction
def is_prime(n):
    if n < 2 :
        return None
    d=2
    while d * d <=n:
        if n % d == 0:
            return False
        d += 1
    return True

# b. print all prime below 50 and count all prime 
print("primes below 50: ", end=" ")
for n in range(2,50):
    if is_prime(n):
        print(n,end=" ")
    
count = 0
for n in range(2, 100):
    if is_prime(n):
        count += 1
    
print("\nNumber of primes below 100 is ", count)

# c.Goldbach's conjecture
def goldbach(n):
    for p in range(2,n):
        q = n - p
        if is_prime(p) and is_prime(q):
            return p,q
    return None

for n in range(4,31,2):
    p,q = goldbach(n)
    print(f"{n} = {p} + {q}")
    
FACT = True

for n in range(4, 10001, 2):
    if goldbach(n) is None:
        FACT = False
        break

# Use a loop with break to check the conjecture for every even number from 4 to 10,000.
print(f"Goldbach holds for every even number from 4 to 10000: {FACT}")