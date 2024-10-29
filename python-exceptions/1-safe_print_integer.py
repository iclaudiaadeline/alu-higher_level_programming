#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Attempt to format the value as an intiger
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If there's an error , return False
        return False
