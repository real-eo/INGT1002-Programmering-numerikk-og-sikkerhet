def g(x):   
    return 2/(x+1)

def iterStep(x_n):
    return g(x_n)
    

def logIter(n, x_n):
    def calculateError(x_n): return g(x_n)
    
    print(f"[n = {n}] x_n = {x_n:>10.4f} \t\t (g(x_n) = {calculateError(x_n):>10.4f})")

X_0 = 0.8               

X_n = X_0                  # n = 0

logIter(0, X_n)

for n in range(1, 20):
    X_n = iterStep(X_n)     # Compute X_(n+1) using iterStep
    logIter(n, X_n)  # Log the results for this iteration