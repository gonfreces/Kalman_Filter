# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''
def solution(ranks):
   # write your code in Python 3.6
   count = 0 #initialize counter for num of soldiers who can report to some superior
   n = sorted(ranks) #order the list example : 0 1 3 3 4 4
   for i in n: #take each item from the sorted list
       if i+1 in n: #check if a higher number which is one greater than i exists
           count += 1 #if true increment counter
   print(count)
   return count
   
#solution([4,4,3,3,1,0])
li = list(range(1,100))
solution(li)
#solution([3, 4, 3, 0, 2, 2, 3, 0, 0])
'''


# timeit statement
print (timeit.timeit(setup = mysetup,
stmt = mycode,
number = 10000) )
