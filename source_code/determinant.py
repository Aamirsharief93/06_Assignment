# Function determinant computes the determinant of matrix
def determinant(matrix):
    n = len(matrix)
    # Base condition, if matrix is 1x1 return element
    if (n == 1):
        return matrix[0][0]
    else:
        # Initialze sign for cofactor expansion
        sign = 1

        # Initialize determinant as zero
        det = 0

        # Iteration through columns
        for col in range(n):
            # Initialize sub matrix for storing (n-1)x(n-1) matrix
            sub_matrix = []

            # Iteration over each row of the matrix from the second row
            for row in range(1, n):
                sub_row = []  # Initialize sub-row to store elements of the sub-row

                # Iterate over each element of the row
                for i in range(n):
                    if (i != col):  # Exclude the current column from the subrow

                        # Append the element to the sub-row if it's not in the current column
                        sub_row.append(matrix[row][i])

                # Append the sub-row to the sub-matrix
                sub_matrix.append(sub_row)
            # Compute determinant of the submatrix recursively
            det += sign*matrix[0][col]*determinant(sub_matrix)

            sign *= -1  # Chnage the sign for cofactor expansion

        return det


# User prompt number of rows
rows = int(input('Enter the number of rows:'))

# Empty list to store user input elements
A = []

# User prompt elements of matrix
print('Enter elements of matrix:')
for i in range(rows):
    row = [int(element) for element in input().split()]
    A.append(row)

# Function call to compute determinent
result = determinant(A)

# Dispaly output
print('Determinant of matrix is:\n', result)
