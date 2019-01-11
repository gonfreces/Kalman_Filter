# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"
# Hello test comment
# code snippet whose execution time is to be measured
mycode = '''
def solution(ranks):
    n = 0
    m = 0
    r = 0
    s = sorted(ranks)
    #print(s)
    for i in range(len(s)-1):
        d = s[i+1] - s[i]
        if d == 0:
            if i != (len(s)-2):
                n += 1
        elif d == 1:
            m += 1
        else:
            n = 0
    r = n + m
    print(r)
li = list(range(1,100))

#solution([3, 4, 3, 0, 2, 2, 3, 0, 0])
solution(li)
'''


# timeit statement
print (timeit.timeit(setup = mysetup,
stmt = mycode,
number = 10000) )
