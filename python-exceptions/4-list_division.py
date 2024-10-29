#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    for i in range(list_length):
        try:
            # Check if the current index is within the bounds of the lists
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            
            # Attempt the division
            result.append(num1 / num2)
        
        except IndexError:
            # If any list is too short
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
    
    return result
