def solution(X, Y, A):
    N = len(A)
    result = -1
    v = 0
    k = 0
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        if A[i] == Y:
            nY += 1
#if nX == nY > 1:
#result = i
        if nX == nY :
            #v += 1
            k = i

#return result
    print(k)
print(solution(1, 50, [3, 2, 1, 50]))
