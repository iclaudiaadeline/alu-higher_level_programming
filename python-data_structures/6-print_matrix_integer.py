#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for k, j in list(enumerate(i)):
            print("{:d}".format(j), end=" " if k < len(i) - 1 else "")
        print()
