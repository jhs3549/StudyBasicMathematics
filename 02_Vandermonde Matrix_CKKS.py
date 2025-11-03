import numpy as np

def ckks_vandermonde_matrix(n):
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

    return V, V_inv

def encode_vector(V_inv, vector):
    encoded_vector = np.dot(V_inv, vector) # 이 코드는 아래 코드와 동일합니다. 
    # poly_coeffs = np.matmul(V, vector)
    # poly_coeffs = V @ vector 
    print("Encoded Vector:")
    print(np.round(encoded_vector, 3))
    print()
    return encoded_vector

def decode_vector(V, encoded_vector):
    decoded_vector = np.dot(V, encoded_vector) # 이 코드는 아래 코드와 동일합니다.
    # original_vector = np.matmul(V_inv, encoded_vector)
    # original_vector = V_inv @ encoded_vector
    print("Decoded Vector (should match original vector):")
    print(np.round(decoded_vector, 3))
    print()
    return decoded_vector

# Example usage
n = 5
V, V_inv = ckks_vandermonde_matrix(n)
sample_vector = np.array([1, 2, 3, 4, 5], dtype=complex)
encoded_vector = encode_vector(V_inv, sample_vector)
decoded_vector = decode_vector(V, encoded_vector)
