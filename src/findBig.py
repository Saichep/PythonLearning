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


def readAsList():
    inp = input('Enter all numbers (delimited with spaces: ')
    nums = inp.split(" ")
    list = []
    for s in nums:
        list.append(int(s))
    return(list)

def findBigUsingList():
    lst = readAsList()
    temp = -1
    for num in lst:
        if num >= temp:
            temp = num
    print("biggest number is {0}".format(temp))

def findBigUsingListBuiltIn():
    lst = readAsList()
    lst.sort(reverse=True)
    print("biggest number is {0}".format(list[0]))

findBigSimple()

