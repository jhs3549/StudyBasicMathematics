# Fast Computation of Large Exponent: 999^179 mod 1763

def fast_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Update base if it's more than or equal to modulus

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if (exponent % 2) == 1:
            result = (result * base) % modulus
        
        # exponent must be even now
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % modulus  # Square the base

    return result

# Given values
base = 999
exponent = 179
modulus = 1763
# Calculate 999^179 mod 1763
result = fast_exponentiation(base, exponent, modulus)
print(f"999^179 mod 1763 = {result}")