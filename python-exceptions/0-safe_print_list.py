#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Ignore the error if x is greater than the length of my_list
    print()  # Print a newline after all elements are printed
    return count
