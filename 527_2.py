def add(aaa):
    x=0
    for a in z:
        x=x+a
    return x

def mul(aaa):
    x=1
    for a in z:
        x=x*a
    return x
    
def callall(value, func):
    return func(value)

#z = [1, 2, 4]
#funcs = [add, mul]
#for f in funcs:
#    print(callall(z, f))
def square(x):
    return x**2

#輸入3 輸出[1,2,3]
print(callall(10, square))
print(callall(10, lambda x: x**2))

aa = lambda x: x**2
print(callall(10, aa))


b = lambda x:list(range(1,x+1))
print(callall(3, b))




