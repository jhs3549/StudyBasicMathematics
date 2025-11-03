def LargeExponent(base, exponent, mod):
    result = 1
    exponent = int(exponent)  # Ensure exponent is an integer for bitwise operations

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
            result %= mod

        exponent >>= 1
        base **= 2
        base %= mod

    return result % mod

def ClassifyPseudoprime(n):
    result = LargeExponent(2, (n-1)/2, n)
    print(f"2^{(n-1)/2:.0f} mod {n} = {result}")
    
    if result != 1 and result != n - 1:
        return 'Pseudoprime'
    else:
        return 'Strong Probable Prime'
    
# Example usage:
n = 1387
classification = ClassifyPseudoprime(n)
print(f"The number {n} is classified as: {classification}")