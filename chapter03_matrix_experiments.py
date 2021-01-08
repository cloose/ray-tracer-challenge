from core import (identity_matrix, inverse, multiply_matrix, multiply_tuple,
                  transpose, tuple_4d)


def main():
    print("What happens when you invert the identity matrix?")
    a = identity_matrix()
    print(inverse(a))

    print()
    print("What do you get when you multiply a matrix by its inverse?")
    a = identity_matrix()
    a[1][0] = 2
    a[0][3] = -5
    b = multiply_matrix(a, inverse(a))
    print(b)

    print()
    print(
        "Is there any difference between the inverse of the transpose of a matrix, and the transpose of the inverse?"
    )
    c = inverse(transpose(a))
    d = transpose(inverse(a))
    print(c)
    print(d)

    print()
    print(
        "Remember how multiplying the identity matrix by a tuple gives you the tuple, unchanged?"
    )
    t = tuple_4d(5, 4, 3, 1)
    i = identity_matrix()
    c = multiply_tuple(i, t)
    print(c)

    print()
    print(
        "Now, try changing any single element of the identity matrix to a different number, and then multiplying it by a tuple. What happens to the tuple?"
    )
    i[1][1] = 2
    i[2][2] = 3
    c = multiply_tuple(i, t)
    print(c)


if __name__ == "__main__":
    main()
