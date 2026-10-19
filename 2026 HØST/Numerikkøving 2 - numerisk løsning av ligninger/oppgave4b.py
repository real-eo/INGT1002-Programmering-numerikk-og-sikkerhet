def g(x):   
    return x-0.4*x*(x**2-1)

def iterStep(x_n):
    return g(x_n)
    

def logIter(n, x_n):
    def calculateError(x_n): return g(x_n)
    
    print(f"[n = {n}] x_n = {x_n:>10.4f} \t\t (g(x_n) = {calculateError(x_n):>10.4f})")

X_0 = 0.2               

x_n = X_0                   # n = 0

logIter(0, x_n)

for n in range(1, 20):
    x_n = iterStep(x_n)     # Compute x_(n+1) using iterStep
    logIter(n, x_n)         # Log the results for this iteration