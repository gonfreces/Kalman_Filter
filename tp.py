# importing the required module
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = '''

def trees(n):
    m = 0
    l = n[1]
    w = 0
    k = 0

    for i in range(len(n)):
        if n[i] >= m:
            m = n[i]
        else:
            if n[i] <= l:
                l = n[i]
            w += 1
            k += 1
            if n[i] > l:
                w = 0
                break
            if i >= 2:
                if n[i] == n[i-2]:
                    w += 1

    if k == 0:
        print("Len " ,len(n))
    else:
        print("W: " ,w)

li = list(range(1,100001))
#print(li)
trees(li)
'''


# timeit statement
print (timeit.timeit(setup = mysetup,
stmt = mycode,
number = 10000) )
