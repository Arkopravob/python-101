#strings are immutable
import string

a ="harry"
print(len(a))
print(a.upper()) #upper case
b = "CODER"

print(b.lower())
c ="hello!!!!"
print(c.rstrip("!")) #rstrip() any trailling char
d = "amg####"
print(d.rstrip("#"))
# replace()

e = "hey coder buddy"
print(e.replace("buddy","Arko"))

print(e.split(" "))
#captilize for first letter in strings use .capwords()
print(string.capwords(e))
print(e.capitalize())

print(e.count("coder"))
print()

a = "Hello world!"
print(a)
#length

print("Hello" in a)

print(a.strip())
print(a.replace('H','j'))
