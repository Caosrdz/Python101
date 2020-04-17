s = "North Dakota"

print(s.ljust(17) + "'")
print(s.rjust(17,"*"))

center_plus = s.center(16, "+")

print(center_plus)
print(center_plus.lstrip("+North"))
print(center_plus.rstrip("+"))
print(center_plus.replace("North", "South"))