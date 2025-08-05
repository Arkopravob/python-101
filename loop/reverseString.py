a ="hi arko how goes your python?"
rev =""
for i in range(len(a)-1 ,-1,-1):
    rev = rev + a[i]
print(f"the reverse string is {rev}")