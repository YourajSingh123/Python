tup = (1, 2, 9, "Hero", 6.7, 2)
print(tup)
print(tup[0])
print(tup[3])
print(type(tup))

#slicing
print(tup[0:3])
print(tup[:2])
print(tup[1:])

#Methods
print(tup.index(9))          #return index of first occurence
print(tup.count(5))          #count total occurence
print(tup.__contains__(1))   #check element existence