from _funcs import foroverdifferanse

def f(x):
    return x**2 + 2*x + 1


x = 0
h = 0.1

print(foroverdifferanse(f, x, h))
print(foroverdifferanse(f, x, h/2))

# ! hehhhh??
