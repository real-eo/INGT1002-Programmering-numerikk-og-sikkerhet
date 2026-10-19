### a) 
Given

$$
\begin{align*}
g_1(x) = x-0.4x(x^2-1) \\
g_2(x) = x+0.4x(x^2-1)    
\end{align*}
$$

We find via the graph:
![graphs](res/oppgave%204/grafer.png)


that the fixed points are:
$$
p = \set{-1, 0, 1}
$$

### b)

Given the iteration of $x_{n+1}=g_1(x_n)$. 

A start value of $x_0 = -0.2$ would approach $x=-1$
```py
X_0 = -0.2 
```

a start value of $x_0 = 0$ would approach $x=0$
```py
X_0 = 0 
```

and a start value of $x_0 = 0.2$ would approach $x=1$
```py
X_0 = 0.2 
```

according to the following program.
```py
def g(x):   
    return x-0.4*x*(x**2-1)

def iterStep(x_n):
    return g(x_n)
    

def logIter(n, x_n):
    def calculateError(x_n): return g(x_n)
    
    print(f"[n = {n}] x_n = {x_n:>10.4f} \t\t (g(x_n) = {calculateError(x_n):>10.4f})")
              
x_n = X_0                   # n = 0

logIter(0, x_n)

for n in range(1, 20):
    x_n = iterStep(x_n)     # Compute x_(n+1) using iterStep
    logIter(n, x_n)         # Log the results for this iteration
```