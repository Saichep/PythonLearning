def total(init=5, *numbers, **keywords):
    totalSum = init 
    for number in numbers:
        totalSum += number
    
    for key in keywords:
        totalSum += keywords[key]
    return totalSum

#print("Total Sum = " + total(1, 2, 3, veg=50, fruits=100))



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
factVariable = int(input('Enter a number: '))
print("Factorial of {0} = {1}".format(factVariable, factorial(factVariable)))