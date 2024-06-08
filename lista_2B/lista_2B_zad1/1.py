def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Macierze mają różne rozmiary")
        return
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[i]))] for i in range(len(matrix1))]

def sub_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Macierze mają różne rozmiary")
        return
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[i]))] for i in range(len(matrix1))]

def mul_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Macierze mają nieodpowiednie rozmiary do mnożenia")
        return
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[i]))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

def read_matrix():
    matrix = []
    while True:
        try:
            row = input().split()
            if not row:
                break
            matrix.append([int(x) for x in row])
        except ValueError:
            print("Zły format danych. Wprowadź macierz ponownie.")
    return matrix

def print_matrix(matrix):
    if matrix is not None:
        for row in matrix:
            print(" ".join(str(x) for x in row))

def main():
    print("Wprowadź pierwszą macierz:")
    matrix1 = read_matrix()
    print("Wprowadź drugą macierz:")
    matrix2 = read_matrix()
    print("Dodawanie:")
    print_matrix(add_matrices(matrix1, matrix2))
    print("Odejmowanie:")
    print_matrix(sub_matrices(matrix1, matrix2))
    print("Mnożenie:")
    print_matrix(mul_matrices(matrix1, matrix2))

if __name__ == "__main__":
    main()
