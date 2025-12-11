##
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   result = (x+y) // 2
   return result

# takes two numbers from keyboard
n1 = int(input())
n2 = int(input())

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')