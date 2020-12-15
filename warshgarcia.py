size = 64
W = [0]*size
L = [0]*size
R = [0]*size
D = [0]*size
Q = [0]*size
V = [0]*size
t = 0
m = 0


def warshgarciamain(numericalData,size):
    n = size - 2
    for j in range(n):
        W[j] = m 
        L[j] = R[j] = -1
    m = n 
    t = 1
    Q[0] = 100000000000000
    Q[1] = W[0] 
    V[1] = 0
    
    for k in range(n+1):
        while (Q[t-1] <= W[k]):
             combi(t)
        t += 1
        Q[t] = W[k]
        V[t] = k 
    while (t > 1):
        combi(t) 
    
    mark(V[1], 0) 
    t = 0
    m = 2 * n
    build(1)
       

    

def combi( k):
    j = 0
    d = 0
    x = 0

    m += 1
    L[m] = V[k-1]
    R[m] = V[k]
    W[m] = x = Q[k-1] + Q[k]
    t -= 1
    
    j = k 
    for j in range(t + 1):
        Q[j] = Q[j+1]
        V[j] = V[j+1]
    
    j = k-2
    for j in range(Q[j] < x, -1):
        Q[j+1] = Q[j]
        V[j+1] = V[j]
    
    while (j > 0 & Q[j-1] <= x):
        d = t-j
        combi(j)
        j = t-d 
        
def mark( k, p):
    D[k] = p 
    if (L[k] >= 0):
        mark(L[k], p + 1)
    if (R[k] >= 0):
        mark(R[k], p + 1)


def build(b):
    j = m 
    if(D[t] == b):
        t += 1
        L[j] = t
    else:
        m -= 1
        L[j] = m 
        build(b + 1)

    if (D[t] == b):
        t += 1
        R[j] = t
    else:
        m -= 1
        R[j] = m 
        build(b + 1)



    

