example = "hello world" #global variable


def loc_ex():
    example = "goodbye!" #local variable
    return example


print(example)
print(loc_ex())