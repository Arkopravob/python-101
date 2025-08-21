# l =[12,23,190,10,13,28]
l = [10,12,13,14,15,18]
# first = l[i]
# last = len(l[i])+1
for i in range(len(l)-1):
    if l[i] < l[i]+1:
        continue
    else:
        print("its not sorted")
        break
else:
    print("your list is sorted")