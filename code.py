# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)
def all_triangle_numbers(n):
    for i in range(1, n+1):   
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))

all_triangle_numbers(10) 
L = [ for i in range(10)]

# Create a function to test if a number is prime
# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greate than or equal to n

    
    """


# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]






