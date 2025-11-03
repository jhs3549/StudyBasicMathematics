def LargeExponent(base, exponent, mod):
    result = 1

    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
            result %= mod
        
        exponent >>= 1
        base **= 2
        base %= mod

    return result % mod

def ClassifyComposite(n):
    result = LargeExponent(2, n-1, n)
    print(f"2^({n}-1) mod {n} = {result}")

    if result != 1:
        return 'Composite'
    else:
        return 'Probable Prime'
    
# Example usage:
n = 1763
classification = ClassifyComposite(n)
print(f"The number {n} is classified as: {classification}")