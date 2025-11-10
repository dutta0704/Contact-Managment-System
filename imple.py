# Program: Twin Primes and Permutations-Combinations
# Author: Your Name
# Description: Finds twin primes less than 1000 and calculates permutations and combinations.

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to print twin primes less than 1000
def print_twin_primes():
    print("Twin Primes less than 1000 are:")
    for num in range(3, 1000, 2):  # only odd numbers
        if is_prime(num) and is_prime(num + 2):
            print(f"({num}, {num + 2})")


# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


# Function to calculate permutations: P(n, r) = n! / (n - r)!
def permutation(n, r):
    return factorial(n) // factorial(n - r)


# Function to calculate combinations: C(n, r) = n! / (r! * (n - r)!)
def combination(n, r):
    return permutation(n, r) // factorial(r)


# Main Program
def main():
    print("\n--- Twin Primes Program ---\n")
    print_twin_primes()

    print("\n--- Permutations and Combinations ---")
    n = int(input("\nEnter value of n: "))
    r = int(input("Enter value of r: "))

    if r > n:
        print("Invalid input! r cannot be greater than n.")
    else:
        p = permutation(n, r)
        c = combination(n, r)
        print(f"\nP({n}, {r}) = {p}")
        print(f"C({n}, {r}) = {c}")


# Run the main program
if __name__ == "__main__":
    main()
