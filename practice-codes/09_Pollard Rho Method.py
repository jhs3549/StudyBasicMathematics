# Pollard Rho Method for Integer Factorization
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f(x, n):
    return (x*x + 1) % n

def PollardRho(n):
	x_0 = random.randint(1, n-1)
	print(f"초기값: {x_0}")

	x_s = f(x_0, n)
	x_t = f(f(x_0, n), n)

	for i in range(int(n ** (1/4))+1):
		d = gcd((x_s-x_t)%n, n)
		
		if d > 1 and d < n:
			print(f"{d} is a factor of {n}")
			return
		elif d == n:
			print("Try another x_0")
			return
		elif d == 1:
			x_s = f(x_s, n)
			x_t = f(f(x_t, n), n)
		else:
			print("Wrong Code")
			return

# Example usage:
n = 36287  # Example composite number   
PollardRho(n)