mixed_case = "A Song of Ice and Fire"

print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.istitle())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.title())
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))

words = mixed_case.split(" ")

print(words)

print((" ".join(words)).isalpha())

