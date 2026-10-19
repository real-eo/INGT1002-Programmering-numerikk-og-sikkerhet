from numpy import e

def F(x): return e**x + x - 3
def dF(x): return e**x + 1

def iterStep(x_n): return x_n - F(x_n) / dF(x_n)

def logIter(n, x_n):
    def calculateError(x_n): return F(x_n)
    print(f"[n = {n}] x_n = {x_n:>10.5f} \t\t (F(x_n) = {calculateError(x_n):>10.4f})")

X_0 = 0               
x_n = X_0                   # n = 0

logIter(0, x_n)

for n in range(1, 20):
    x_n = iterStep(x_n)     # Compute x_(n+1) using iterStep
    logIter(n, x_n)         # Log the results for this iteration