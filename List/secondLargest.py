l =[12,23,190,10,13,28]
largest = l[0]
secondlargest = l[0]

for i in l:
    if i > largest:
        largest = secondlargest
        largest = i
    elif i > secondlargest:
        secondlargest =i
print(f"the second largest number is {secondlargest}")