def sqrt(x):
     return x ** 0.5

def add_function(func, x):
    return func(x) + func(x)

print(sqrt(9))
print(add_function(sqrt, 9))