def is_even_with_return(i):
    print('with return')
    remainder = i % 2
    return remainder == 0

print(is_even_with_return(132))

def is_even(i):
    return i % 2 == 0

print("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")

def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(z):
    print('inside func_c')
    return z()

print(func_c(func_a))

def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val)
