def common_method(polynomial, x, n):
    multiplication_count = 0
    addition_count = 0
    result = polynomial[n]
    x_power = x
    
    for i in range(n-1, -1, -1):
        result += polynomial[i] * x_power
        multiplication_count += 1
        addition_count += 1
        x_power *= x
        multiplication_count += 1

    multiplication_count -= 1  # Adjust for the last unnecessary multiplication
    
    return result, multiplication_count, addition_count

def horners_method(polynomial, x, n):
    multiplication_count = 0
    addition_count = 0

    result = 0
    result += polynomial[0]

    for i in range(1, n+1):
        result = result * x + polynomial[i]
        multiplication_count += 1
        addition_count += 1

    return result, multiplication_count, addition_count

# Example usage:
poly = [2, -6, 2, -1]  # Represents 2x^3 - 6x^2 + 2x - 1
x_value = 3
n = len(poly) - 1
common_result, common_mults, common_adds = common_method(poly, x_value, n)
horner_result, horner_mults, horner_adds = horners_method(poly, x_value, n)

print(f"Common Method: Result = {common_result}, Multiplications = {common_mults}, Additions = {common_adds}")
print(f"Horner's Method: Result = {horner_result}, Multiplications = {horner_mults}, Additions = {horner_adds}")
