superPowers = ['flight', 'cool cape', '20/20 vision', 'Coding Skillz']
print(superPowers)
print(superPowers[3])
print(superPowers[2])
print(len(superPowers))
print(*superPowers)
#deleting
del superPowers[2]
print(*superPowers)
#insert element
print(superPowers.insert(2,"meat"))
print(*superPowers)
#pop method
superPowers.pop(1)
print(superPowers)
superPowers.reverse()
print(*superPowers)


