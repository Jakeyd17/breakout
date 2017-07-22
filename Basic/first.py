#! /usr/bin/python2

def printstring(cats):
    print(cats)

def hello():
    print('hello')

if __name__ == '__main__':
    print('Hey there')
    hello()

    # Variables
    # strings
    string1 = 'Test'
    string2 = 'Test2'

    printstring(string1)
    printstring(string2)

    # integers
    integer1 = 1
    integer2 = 5578
    printstring(integer1)
    printstring(integer2)


    # sequences
    # list
    list1 = ['string1', 'string2', 'string3']
    list2 = [string1, string2, integer1, integer2]
    list3 = [list1, list2]

    # loops
    print('\n\nLoops:')
    for frootloops in list1:
        printstring(frootloops)

    print()
    for pancakes in list2:
        printstring(pancakes)

    for waffles in list3:
        for bacon in waffles:
            print('bacon: {}'.format(bacon))



print('\n\noutofscope')


