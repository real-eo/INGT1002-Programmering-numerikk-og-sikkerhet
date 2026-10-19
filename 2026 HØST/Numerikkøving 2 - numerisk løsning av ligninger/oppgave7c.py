from numpy import e

                                    # f(x)/f'(x) = (x^(1/3)) / (1/(3*x^(2/3))) = 3*x
def iterStep(x_n): return -2*x_n    # x_n+1 = x_n - 3*x_n 

def logIter(n, x_n):

    print(f"[n = {n}] x_n = {x_n:>10.5f} \t\t")

X_0 = 1               
x_n = X_0                   # n = 0

logIter(0, x_n)

for n in range(1, 20):
    x_n = iterStep(x_n)     # Compute x_(n+1) using iterStep
    logIter(n, x_n)         # Log the results for this iteration