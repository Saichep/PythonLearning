def fibonacci(n):
    result = []
    a = 0
    b = 1
    while b < n:
        result.append(b)
        a, b = b, a + b # b is assigned to a; a+b is assigned to b
    return result

def fibonacciWithDefaults(n, count, a=0, b=1):
    result = []
    while b < n and result.__len__() < count:
        result.append(b)        
        a, b = b, a + b # b is assigned to a; a+b is assigned to b
    return result

f100 = fibonacci(100)
print(f100)

f100Defaults = fibonacciWithDefaults(100, count=10)
print(f100Defaults)