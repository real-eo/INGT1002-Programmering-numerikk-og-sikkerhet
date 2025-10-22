def foroverdifferanse(f, x, h):
    return (f(x + h) - f(x)) / h

def bakoverdifferansen(f, x, h):
    return (f(x) - f(x - h)) / h

def senterdifferanse(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def trapesintegrasjon(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n): integral += f(a + i * h)
    
    return integral * h