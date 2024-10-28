#!/usr/bin/pyhthon3
def safe_print_list(my_list=[], x=0

  count = 0
  try: 
  for i in range (x):
      print(my_list[i], end="")
      count += 1
      except IndexError:
          pass  # ignore the error when ex is greater than the length of my_list
      print() # print a newline at the end
      return count 
