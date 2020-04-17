user_string = input("enter string") 
r = "" 


for item in range(len(user_string)- 1, -1, -1):
    r += user_string[item]


print(r)
