#1
movies = []
mov1 = input("enter 1st movie:")
mov2 = input("enter 2nd movie:")
mov3 = input("enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#2
num = [1, 2, 1]
copyList = num.copy()
copyList.reverse()

if(copyList == num):
    print("Pallindrome")
else:
    print("Not palindrome")    

#3
Grade = ("C", "D", "A", "A", "B", "B", "A")
print(Grade.count("A"))

Grade = ["C", "D", "A", "A", "B", "B", "A"]
Grade.sort()
print(Grade)