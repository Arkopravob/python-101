a = int(input("Tell the number : "))
copy = a
rev =0
while(a > 0):
    rev = ((rev * 10)+( a % 10))
    a = a // 10
if copy == rev:
    print("its a palindrome number")
else:
    print("Its not a plaindrom number")