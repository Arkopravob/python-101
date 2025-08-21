l =[12,23,190,10,13,28]
largest =l[0]
index = 0
for i in range(len(l)):
    # print(l[i])
    if l[i] >largest:
        largest = l[i]
        index = i
print(f"the largest value of l is: {largest},at the index of  {index} ")