def hello():
    print("hello")

def helloParam(name):
    print('Hello ' + name)
    print(len(name))

def plusOne(num) :
    return num + 1

## print function return None value anf just prints the line on the consol
def printTest() :
    print()

## print function will always put new line character at the end and so the next word preinted on the ext line
def printTest2():
    print('Hello')
    print('world')
## O/P
# hello
# world

## If new line characters to be wipped out then this can be done by adding  end
def printNoNewLineCharac() :
    print('Hello',end='')
    print('World')
# O/P HelloWorld

## If words to be separated by ABC
def printSeparateWord() :
    print('Cat','Dog','Mouse') # O/p Cat Dog Mouse  // separated by space
    print('Cat', 'Dog', 'Mouse', sep='ABC')


hello()
helloParam("Amruta")
helloParam("Mukta")
newNumber = plusOne(10)
print(newNumber)
spam = printTest()
print(spam)
printTest2()
printNoNewLineCharac()
printSeparateWord()




