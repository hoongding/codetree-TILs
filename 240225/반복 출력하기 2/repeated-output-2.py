n = int(input())

def printHello(n):
    if n > 1:
        printHello(n - 1)
    print('HelloWorld')

printHello(n)