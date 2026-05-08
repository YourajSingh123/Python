#Concatenation
str1 = input("enter your 1st name:")
str2 = input("enter your last name:")
print(str1 + str2)

#length of string
print(len(str1))
print(len(str2))

#Indexing
str3 = "Jay Shree Ram"
print(str3[0])
print(str3[3])
print(str3[8])
print(str3[11])

#Slicing --> ending index is not included
print(str3[1:4])
print(str3[:7])  #same as print(str3[0:7])
print(str3[4:])  #same as print(str3[4:len(str)])

print(str3[-4:-1])  #Neagative indexing
print(str3[-10:-6])

#some String Functions
str = "i am from Bihar"
print(str.endswith("ar"))
print(str.endswith("boy"))
print(str.startswith("i"))

print(str.capitalize())
print(str.replace("a", "o"))
print(str.replace("Bihar", "Delhi"))

print(str.find("B"))
print(str.find("from"))
print(str.find("x"))

print(str.count("r"))
print(str.count("am"))

print(str.split("from"))