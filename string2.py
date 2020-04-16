print("hola".rjust(10, "*"))
print("hola".ljust(10, "*"))
print("hola".center(10, "*"))

x ="*******1*2*3*4*5*6*7*8*9*0*"

print(x.strip("*7"))
print(x.rstrip("*7890"))
print(x.lstrip("*"))

print(x.replace("*",""))