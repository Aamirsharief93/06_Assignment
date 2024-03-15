# Gram schmedit procedure

import numpy as np

# Function to perform Gram-Schmidt procedure using orthonormal and orthogonal functions


def Grahm_Schmidt_procedure(*v, n):
    # Function call orthonromal_basis
    result2 = orthonromal_basis(*v, n=n)


# Function calculates orthonormal basis
def orthonromal_basis(*v, n):

    # orthogonal basis function call to calculate orthogonal basis
    result1 = orthogonal_basis(*v, n=n)

    # Initialize list to store orthonormal basis
    N = []
    print('\nOrthonormal basis of given vectors are:')

    # Iterate over the orthogonal vectors
    for i, q_i in enumerate(result1):

        # Calculate orthonormal vector
        N_i = q_i/np.sqrt(np.dot(q_i, q_i))

        # Appending orthonormal vectors to the list
        N.append(N_i)
        # Displaying the orthonormal vectors
        print(f'N{i + 1} is:\n{N_i}')
    return N


# Fuction calculates orthogonal basis
def orthogonal_basis(*v, n):

    # Initialzie list to store orthogonal basis
    q = [v[0]]
    print(f'\nOrthogonl basis of given vectors are:\nq1 is:\n{q[0]}')

    # Iterarte over the other vectors
    for i in range(1, n):

        # Initialize a zero vector to store the projections
        sum = [0]*n

        # Iterates over the orthogonal basis and given vectors
        for j in range(i):

            # Dot product of orthogonal basis
            dot_product_of_qi_qi = np.dot(q[j], q[j])
            # Dot product of orthogonal basis vectors and corresponding vector
            dot_product_of_qi_v = np.dot(v[i], q[j])
            # Scalar multiple of  above two
            scalar = dot_product_of_qi_v/dot_product_of_qi_qi
            # Summation of the projections
            sum += scalar * q[j]

        # Computing the orthogonal vectors
        q_i = v[i] - sum
        # Appending the orthogonal vectors to the list
        q.append(q_i)
        # Displaying the current orthogonal vector
        print(f'q{i + 1} is:\n{q_i}')

    return q


# Initialize empty list to store append differernt vectors
vector = []

# User prompt number of vectors
n = int(input('Enter the number of vectors:'))

# User prompt for elements of matrix
for i in range(n):
    print(f'Enter the elements of vector {i + 1}:')
    v = np.array([float(element) for element in input().split()])
    vector.append(v)
# Function call to perform Grahm Schmidt procedure
Grahm_Schmidt_procedure(*vector, n=n)
