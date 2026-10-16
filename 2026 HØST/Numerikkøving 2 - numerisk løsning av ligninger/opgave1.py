def f(x):   
    return x**2 + x - 12    # = 0

def iterA(x_n):
    return 12 / (x_n + 1)

def iterB(x_n):
    return 12 - x_n**2

def logIter(n, x_nA, x_nB):
    def calculateError(x_n): return f(x_n)
    
    print(f"[n = {n}] X_nA = {x_nA:>10.4f}  |  X_nB = {x_nB:>10.4f} \t\t (f(X_nA) = {calculateError(x_nA):>10.4f}  |  f(X_nB) = {calculateError(x_nB):>10.4f})")

X_0 = 16/5                  

X_nA = X_0                  # n = 0
X_nB = X_0                  # n = 0

logIter(0, X_nA, X_nB)

for n in range(1, 4+1):
    X_nA = iterA(X_nA)      # Compute X_(n+1) using iterA
    X_nB = iterB(X_nB)      # Compute X_(n+1) using iterB
    logIter(n, X_nA, X_nB)  # Log the results for this iteration