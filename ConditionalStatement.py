#1
light = input("enter :")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Look")
elif(light == "green"):
    print("Go") 
else:
    print("light is broken")   

#2
marks1 = int(input("enter the 1st subject marks:"))    
marks2 = int(input("enter the 2nd subject marks:")) 
marks3 = int(input("enter the 3rd subject marks:"))     

sum = marks1 + marks2 + marks3
print(sum)
AverageMarks = sum/3
print(AverageMarks)

if(AverageMarks >= 90):
    Grade = "A"
elif(AverageMarks >= 60 and AverageMarks < 90):
    Grade = "B"
elif(AverageMarks >= 30 and AverageMarks < 60):
    Grade = "C"
else:
    Grade = "Fail"

print("the grade of student is:", Grade)   

#3
a = int(input("enter the num:"))
if(a % 2 == 0):
    num = "Even"
else:
    num = "Odd"

print("the num is:", num)   

#4
x = int(input("enter the 1st num:"))
y = int(input("enter the 2nd num:"))
z = int(input("enter the 3rd num:"))

if(x >= y and x >= z):
    print("x is largest")
elif(y >= x and y >= z):
    print("y is largest")
else:
    print("z is largest")

#5
num = int(input("enter the num:"))
if(num % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")            
