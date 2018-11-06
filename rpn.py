#!/usr/bin/python
import operator
from colorama import Fore, Back, Style


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(raw_input("rpn calc> "))
        print(Fore.BLUE + "Result: ")
        print(Fore.RED)
        print(result)

def randomfunc():
    x = 73
    random = x * 50

    if random == 20:
        print ("Wow!")

if __name__ == '__main__':
    main()
