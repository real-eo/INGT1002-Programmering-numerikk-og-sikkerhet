## Fixed-point iteration

### General

1. **Rewrite the equation as $x = g(x)$** *(there are many possible choices of $g$)*
2. **Pick a start value $x_0$**
3. **Iterate $x_{n+1} = g(x_n)$**
4. **After each step, compute the error against the original equation written in standard form: $error = equation$** *(in standard form)*
5. **Stop when the $error \le tolerance$, and count the steps $n$**
6. **Convergence check: it converges near $x*$ if $|g'(x*)| < 1$, and diverges if $> 1$**

##### Example: $2x = cos(x)$

1. Rewrite as x = g(x): $g(x) = cos(x)/2$
2. Pick a start value: $x_{0} = 0$
3. Iterate: $x_{n+1} = cos(x_n)/2$
4. After each step, compute the error $|2x_n - cos(x_n)|$
5. Stop when the $error \le tolerance$, and count the steps $n$
6. Convergence check: $|g'(x*)| = |sin(x*)/2| < 1 \checkmark$


## Newton's method

**General**

1. **Rewrite the equation in standard form: $f(x) = 0$** *(everything on one side)*
2. **Find $f'(x)$**
3. **Pick a start value $x_0$**
4. **Iterate $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$**
5. **Stop when the $error \le tolerance$, and count the steps $n$**
6. **Safety check: it fails if $f'(x_n) \approx 0$, or if you start too far from the root** *(like $x^{\frac{1}{3}}$, where it diverges)*

##### Example: $2x = cos(x)$

1. Move everything to one side: $f(x) = 2x - cos(x)$ *(the earlier $g = cos(x)/2$ gives identical iterates as: $f = g - x$ which gives $f = \frac{cos(x)}{2} - x = x - \frac{cos(x)}{2}$, and because scaling $f$ doesn't change Newton's method)*
2. Differentiate: $f'(x) = 2 + sin(x)$
3. Pick a start value: $x_0 = 0$
4. Iterate: $x_{n+1} = x_n - (2x_n - cos(x_n)) / (2 + sin(x_n))$
5. Stop when the error $|2x_n - cos(x_n)| \le tolerance$, and count the steps $n$
6. Safety check: $f'(x)$ is never $0$ (it is between $1$ and $3$), so it can't blow up


## The one difference to remember
- **Fixed-point** needs a function $g$ where the solution satisfies $g(x) = x$. The step is $x \leftarrow g(x)$.
- **Newton** needs a function $f$ where the solution satisfies $f(x) = 0$. The step is $x \leftarrow x - \frac{f}{f'}$. It's also trivially easy to go from the fixed-point method to Newton's method $(f(x)=g(x)-x)$, but not the other way around.
