#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            # Initialize the variables for division
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            result.append(num1 / num2)
        
        except IndexError:
            # If either list is too short
            print("out of range")
            result.append(0)

        except TypeError:
            # If either element is not an integer or float
            print("wrong type")
            result.append(0)

        except ZeroDivisionError:
            # If there is an attempt to divide by zero
            print("division by 0")
            result.append(0)

        finally:
            # This block can be used for any cleanup or logging if needed
            pass
    
    return result
