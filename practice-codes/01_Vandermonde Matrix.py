import numpy as np

# Define the size of the Vandermonde matrix
n = 5
omega = np.exp(2j * np.pi / (2 * n))
x_points = [omega**(2*i+1) for i in range(n)]
print("x_points:", np.round(x_points, 3))
print()

# Construct the Vandermonde matrix
V = np.vander(x_points, N=n, increasing=True)
V_inv = np.linalg.inv(V)

print("Vandermonde Matrix V:")
print(np.round(V, 3))
print()
print("Inverse of Vandermonde Matrix V_inv:") 
print(np.round(V_inv, 3)) 
print()

# Verify the inversion
identity_check = np.dot(V, V_inv) # dot 함수는 행렬 곱셈을 수행합니다.
print("Product of V and V_inv (should be identity):")
print(np.round(identity_check, 3))
print()

# Encode a sample vector
sample_vector = np.array([1, 2, 3, 4, 5], dtype=complex)
encoded_vector = np.dot(V, sample_vector)
print("Encoded Vector:")
print(np.round(encoded_vector, 3))
print()

# Decode the encoded vector
decoded_vector = np.dot(V_inv, encoded_vector)
print("Decoded Vector (should match sample vector):")
print(np.round(decoded_vector, 3))
print()