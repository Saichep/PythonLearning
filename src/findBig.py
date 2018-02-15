def findBigSimple():
    num1 = float(input('Enter First Number:'))
    num2 = float(input('Enter Second Number:'))
    if num1 > num2:
        print(num1)    
    else:
        print(num2)

def findBigSimpleUsingTernary():
    num1 = float(input('Enter First Number:'))
    num2 = float(input('Enter Second Number:'))
    print( num1 if ( num1 > num2 ) else num2 )

def __readAsList__():
    inp = input('Enter all numbers (delimited with single space): ')
    nums = inp.split(" ")
    lst = []
    for s in nums:
        lst.append(int(s))
    return(lst)

def findBigUsingList():
    lst = __readAsList__()
    print(("length of {0} = {1}".format("lst", lst.__len__())).capitalize())
    temp = -1
    for num in lst:
        if num >= temp:
            temp = num
    print(("biggest number in {0} is {1}".format(lst, temp)).capitalize())

def findBigUsingListBuiltIn():
    lst = __readAsList__()
    lst.sort(reverse=True)
    print(("biggest number in {0} is {1}".format(lst, lst[0])).capitalize())

#findBigSimpleUsingTernary()
findBigUsingList()