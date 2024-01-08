# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def is_prime(n:int) ->bool:
  if n<2:
    return False
  if n in [2,3,5]: 
    return True
  if n%2 == 0:
    return False
  r = 3
  while r*r <=n:
    if n%r == 0:
      return False
    r += 2
  return True


# Find the prime numbers
def prime_list(LIMIT = 10) -> [int]:
    prime_numbers = []
    for i in range(2,LIMIT):
        if(is_prime(i)):
            prime_numbers.append(i)
    return prime_numbers

print(prime_list(20))
# Sum of primes below 20
print(sum(prime_list(20)))

# sum of primes below 2 million
print(sum(prime_list(2000000)))