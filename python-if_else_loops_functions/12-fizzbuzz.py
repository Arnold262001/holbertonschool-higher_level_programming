#!/usr/bin/python3
def fizzbuzz():
    str = ''
    tmp = ''

    for i in range(1, 101):
        if (i % 3 == 0) & (i % 5 ==0):
            str ='FizzBuzz'
        elif i % 5 == 0:
            str = 'Buzz'
        elif i % 3 == 0:
            str = 'Fizz'
        else:
            str = i
    
        tmp = "{0} {1} ".format(tmp, str)

    print(tmp)
