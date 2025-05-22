#comparison operator
a = 12
b = 13
print(a==b) #false
print (a < b) # true
print(a >= b) #false
print( a <= b)

#flow control
name = 'ram'
age = 90
if name == 'arko':
    print('hi' + name)
elif age < 12:
    print("hey u are not adult")
else:
    print("go back home too  old")

#loop while
# num = 5
# while num!=0:
#     print('its num 5')
#     break
spam = 0
while spam < 5:
    print("hey spammer")
    spam =spam+1

#annyoing while loop
name = ''
while name != 'your name':
    print('enter your name: ')
    name = input()
print("my name is " + name)