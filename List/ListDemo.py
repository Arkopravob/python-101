a = [12,3,5,6,8,10,12]
"""indexing of list"""
print(a[3])
"""slicing"""
print(a[0:3])

"""traverasing"""
for i in range(len(a)):
    print(a[i])

#2nd way direct value
for i in a:
    print(i)

"""list method"""
#append

a.append(20)
print(a)

#insert
a.insert(4,11)
print(a)
