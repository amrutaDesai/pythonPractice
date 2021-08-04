def divide42By(devideBy) :
    try :
        return 42/devideBy
    except ZeroDivisionError :
        return 'Error you tried to divide by 0'

print(divide42By(2))
print(divide42By(4))
print(divide42By(0))
print(divide42By(1))