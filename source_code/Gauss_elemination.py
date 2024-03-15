import numpy as np


def gaussian_elemination(a, b):
    # length of the system of equations
    n = len(a)

    # Elimination
    # k specifies the fixed rows that is the pivots from 0 to n-2
    for k in range(n-1):

        # Checks if pivot is very close to zero
        if abs(a[k, k]) < 1.0e-12:
            # Loop to find a row with a larger element in the same column to swap with
            for i in range(k+1, n):
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    # Swapping rows k and i
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
        # i is used to apply elemination below the fixed rows from k+1 to n-1
        for i in range(k+1, n):
            # checks if first element is zero and skip to next iteration of i
            if a[i, k] == 0:
                continue

            # calculates factor of a[k,k]/a[i,k]
            factor = a[k, k]/a[i, k]

            # updates element of Matrix A,each of the correspoding columns from k to n-1
            for j in range(k, n):
                a[i, j] = a[k, j]-a[i, j]*factor

            # Updates element of B from k to n-1
            b[i] = b[k]-b[i]*factor

    # Backward substitution
    # Solution vector
    x = [0.0]*n
    # Calculation of last variable
    x[n-1] = b[n-1]/a[n-1, n-1]

    # Iterates through the remaining variables in reverse order
    for i in range(n-2, -1, -1):
        sum_ax = 0
        # Computes the sum of products for variable x[i]
        for j in range(i+1, n):
            sum_ax += a[i, j]*x[j]
        # Compute the value of variable x[i]
        x[i] = (b[i]-sum_ax)/a[i, i]

    return a, x


def pivots(a):
    pivots = []
    for i in range(rows):
        if a[i, i] != 0:
            pivots.append(i)
    return pivots


# User prompt number of rows
rows = int(input('Enter the number of rows:'))

# User prompt elements for matrix of mentioned size
print('Enter elements of matrix:')
a = np.array([[float(element) for element in input().split()]
             for i in range(rows)])

print('Enter elements of B column:')
b = np.array([float(element) for element in input().split()])

result1, result2 = gaussian_elemination(a, b)
print(f'Resultant matrix is:\n{result1}\nSolution is:\n{result2}')
print(f'Pivot indexes are:\n{pivots(result1)}')
