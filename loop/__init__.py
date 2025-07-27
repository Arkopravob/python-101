num =input()
fact = 1
if num < 0:
    print("its negetive")
else:
    for i in range (1 , num+1):
        fact = fact * i
print("factorial of the number is ", fact)