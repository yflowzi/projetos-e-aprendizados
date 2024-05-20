
def myfunction():
#creating the first set

    my1set ={"avocate","aligator","anthem","anthem"}
    print(my1set)

myfunction()

def myfunction2():
#Set items are unordered, unchangeable, and do not allow duplicate values.

#Set items are unchangeable, meaning that we cannot change the items after the set has been created.

#True and 1 is considered the same value:

    my2set = {True,1,2}

    print(my2set)

#False and 0 is considered the same value:

    my3set = {"False,1,0,0,0,0,0,0,0"}
    print(my3set)
    print(len(my3set))
myfunction2()


def myfunction():
    #A set can contain different data types:
    my4set = {False,True,2,"three",4.0}
    print(my4set)

    '''
    Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
    '''