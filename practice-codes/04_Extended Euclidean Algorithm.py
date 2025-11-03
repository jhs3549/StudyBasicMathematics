# Extended Euclidean Algorithm
# This algorithm not only computes the greatest common divisor (gcd) of two integers a and b,
# but also finds integers x and y such that ax + by = gcd(a, b).
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a%b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
    
# Example usage
a = 30 
b = 12
gcd, x, y = extended_gcd(a, b)
print(f"GCD of {a} and {b} is {gcd}")
print(f"Coefficients x and y are: {x}, {y}")