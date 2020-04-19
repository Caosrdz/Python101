exlist1 = ["1", "2", "3"]
exlist2 = [1, 2, 3]
exlist3 = [2.3, 4.5, 6.7]
exlist4 = ["1", "2", "3"],  [1, 2, 3], [2.3, 4.5, 6.7]

print(list("hola"))

print(1 in exlist2)

print(exlist2[2])

print(exlist4[1][1])

print(exlist1[-1])

l = [1,2,3,4,5,6,7,8,9,0]

print(l[:4])
print(l[4:6])
print(l[6:])

l[4:6] = [6,5]
print(l)

del l[-1]

print(l)
l.remove(9)
print(l)

z = [2,2,3,3,4,4,5,5]
z.remove(2) #only removes the first instance
print(z)

#del elimina un inice y remove elimina un item de la lista
#append() agrega el item al final
z.append(9)
print(z)

z.insert(1,0)
print(z)

z.sort()

print(z)

y = ["a", "e","j","d"]
y.sort()

print(y)

y.sort(reverse=True)
print(y)

s = [False, True, -2, 3, 5, 10.09]
s.sort()
print(s)

w = ["A","b","c","Z","a","a","asdfa","QWER"]
w.sort()
print(w)
w.sort(key=str.lower)
print(w)
print(w.index("a"))
t = w.pop()
print(t)
print(w)
e = w.pop(4)
print(e)
print(w)