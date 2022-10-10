def input_matrix():
    matrix = []

    print(">>> Input order of matrix")
    row = int(input("Choose matrix rows and columns: "))
    column = row
    print(f"Matrix A: {row}x{column}")
    print("-" * 20)

    # Input elements of matrix A and B
    print(">>> Input elements of matrix")
    for i in range(row):
        matrix.append([])
        for j in range(column):
            matrix[i].append(int(input(f"A {i + 1}, {j + 1}: ")))
    print("-" * 20)

    return matrix


def inverse_matrix(matrix):
    # Find Determinant
    determinant = find_determinant(matrix)
    if determinant == 0:
        return print("Matrix is Singular! (Determinant = 0)")

    # Step 1: Generate Matrix of Minors
    column = len(matrix)
    matrix_2 = []
    for i in range(column):
        matrix_2.append([])
        for j in range(column):
            matrix_3 = []
            iter = 0
            for k in [x for x in range(column) if x != i]:
                matrix_3.append([])
                for l_ in [y for y in range(column) if y != j]:
                    matrix_3[iter].append(matrix[k][l_])
                iter += 1
            matrix_2[i].append(find_determinant(matrix_3))

    # Step 2: Generate the Matrix of Cofactors
    for i in range(column):
        for j in range(column):
            if ((i + j) % 2) == 1:
                matrix_2[i][j] *= -1

    # Step 3: Find the Adjugate/Adjoint
    matrix_3 = []
    for i in range(column):
        matrix_3.append([])
        for j in range(column):
            if i == j:
                matrix_3[i].append(matrix_2[i][j])
            else:
                matrix_3[i].append(matrix_2[j][i])

    # Step 4: Divide Adjugate by Determinant
    for i in range(column):
        for j in range(column):
            matrix_3[i][j] /= determinant

    return matrix_3


def find_determinant(matrix):
    column = len(matrix)
    if column > 2:
        final_determinant = 0
        for i in range(column):
            matrix_2 = []
            iter = 0
            for j in [x for x in range(column) if x != 0]:
                matrix_2.append([])
                for k in [y for y in range(column) if y != i]:
                    matrix_2[iter].append(matrix[j][k])
                iter += 1
            determinant = find_determinant(matrix_2)
            if (i % 2) == 0:
                final_determinant += matrix[0][i] * determinant
            else:
                final_determinant -= matrix[0][i] * determinant

        return final_determinant
    elif column == 1:
        return matrix[0][0]
    else:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        determinant = (a * d) - (b * c)
        return determinant


def print_matrix(matrix, text=""):
    column = len(matrix)
    print(f"{text}")
    for i in range(column):
        print("\t[", end=" ")
        for j in range(column):
            print(f"{round(matrix[i][j], 3)}", end=" ")
        print("]\n", end="")


def main():
    print("===== Inverse Matrix Calculator =====")
    while True:
        matrix = input_matrix()
        inv_matrix = inverse_matrix(matrix)
        print(">>> Calculation Results")
        print_matrix(matrix, "A:")
        print_matrix(inv_matrix, "A^-1:")
        print("-" * 20)
        pilihan = input(">>> Would you like to make another calculation? (y): ")
        if pilihan.lower() != "y":
            print("Thank you for using this program :)")
            break


if __name__ == "__main__":
    main()
