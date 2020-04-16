example = "hello world" #global variable


def loc_ex():
    example = "goodbye!" #local variable
    return example



print(loc_ex())
print(example)


#Global variables can be accessed by code in the local scope
def printBar():
    print(var)


var = "variable local"
printBar()


def scope1():
    fruit = "apple"
    print(fruit)


def scope2():
    fruit = "banana"
    print(fruit)


fruit = "pear"
scope1()
scope2()
print(fruit)


def scope3():
    global fruta 
    fruta = "uva"

    print(fruta)


fruta = "sandia"
scope3()
print(fruta)

word = "hola mundo"


def hi_world():
    return word



print(hi_world())



def pi_returner():
    approx = 3.14
    return approx


print(pi_returner())