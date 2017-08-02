

print('Welcome to Python!')
# Set the variables to the values listed in the instructions!
"""
multi
line 
comment"""
print('processed multi line comment')

def learnVariables():
    my_int = 7
    my_float = 1.23
    my_bool = True
    print('value of my_int is =', my_int)
    print('value of my_float is =', my_float)
    print('value of my_bool is =', my_bool)
    print('value of my_bool negated is =', not my_bool)

# Indentation
def countEggs():
    eggs = 12
    return eggs

# math operations
def learnMathOperations():
    x = 10
    y = 3
    float = 0.5
    print(x, "plus", y, "=", x + y)
    print(x, "minus", y, "=", x - y)
    print(x, "multiplied by", y, "=", x * float)
    print(x, "divided by", y, "=", x / y)
    print(x, "to power of (exponential)", y, "=", x ** y)
    print(x, "modulus", y, "=", x % y)

print('count of eggs is =',countEggs())
learnVariables()
learnMathOperations()