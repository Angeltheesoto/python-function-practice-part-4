# Function 1
def max_num(*num):
 for x in range(len(num)):
  # return num[x]
  # return max(num[x]), max(num[x])
  largest_integer = max(num[x])
  num[x].remove(largest_integer)
  second_largest_integer = max(num[x])
  num[x].remove(second_largest_integer)
  third_largest_integer = max(num[x])
  return largest_integer, second_largest_integer, third_largest_integer

print(max_num([23, 53, 2, 123, 5])) # returns (123, 53, 23)

# Function 2
def multi_list(num):
 result = 1
 for x in range(0, len(num)):
  result = result * num[x]
 return result

print(multi_list([4, 3, 2, 1])) # returns 4 * 3 * 2 * 1 = (24)

# Function 3
def rev_string(num):
 new_list = num[::-1] # this reverses the list/ or tuplets
 return new_list

print(rev_string([4, 3, 2, 1])) # returns (1, 2, 3, 4)

# Function 4 - Im not sure i understand what the question is asking for.
def num_within(num):
 if num[0] > num[1] and num[1] < num[2]:
  return True
 else:
  return False

print(num_within([3, 2, 4])) # returns True
print(num_within([3, 1, 3])) # returns True
print(num_within([10, 2, 5])) # returns False

# Function 5
# Formula for nCr
'''
nCr = n! / ((n-r)! r!)
n! = n(n-1)(n-2)
'''
# factorial function from Pythons built in math module.
from math import factorial
def pascal(numRows):
 for x in range(numRows):
  # loop to get leading spaces
  for y in range(numRows - x + 1):
   print(end="")

  # loop to get elements of row x
  for y in range(x + 1):
   # nCr = n!/((n-r)!*r!)
   print(factorial(x)//(factorial(y)*factorial(x - y)), end=" ")

   # print each row in a new line
   print("/n")

pascal(1)
pascal(3)
pascal(5)

'''
output: (1)
1
'''

'''
output: (5)
1
11
121
1331
14641
'''

