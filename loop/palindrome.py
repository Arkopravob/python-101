a = str(input())
b=""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
if b == a:
    print("its a palindrome string")
else:
    print("its not a palindrome")