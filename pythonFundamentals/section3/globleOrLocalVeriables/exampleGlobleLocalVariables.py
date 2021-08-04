spam = 'This is a global Variable'

def test() :
    spam = 'This is a local variable'
    print('Inside local scope')
    print(spam)

test()
print('Inside global scope')
print(spam)

## Code in global scope can not use local variables
## Code in local scope can access global variables
def testScop() :
    eggs = 10

testScop()
# print(eggs)   ## Do you know why coce does not get compile? :)

## Code in one functions local scope can not be used in another functions local scope
def oneFucntion() :
    testResult = 100
    result()
    print(testResult)   ## 100

def result() :
    testResult = 200

oneFucntion()


## Code in local scope can access global variables
## Assignment statement == local variable
## No Assignment statement == global variable

count = 0

def testCount() :
    global count
    count = 10