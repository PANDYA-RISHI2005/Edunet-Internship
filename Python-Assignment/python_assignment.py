
# 1. LIST METHODS (5)
print("\n1. LIST METHODS")

fruits = ["Apple", "Banana", "Orange"]

print("Original List:", fruits)

fruits.append("Mango")
print("append():", fruits)

fruits.insert(1, "Grapes")
print("insert():", fruits)

fruits.remove("Orange")
print("remove():", fruits)

fruits.sort()
print("sort():", fruits)

fruits.pop()
print("pop():", fruits)


# 2. DICTIONARY METHODS (5)
print("\n2. DICTIONARY METHODS")

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print("Original Dictionary:", student)

print("keys():", student.keys())

print("values():", student.values())

print("items():", student.items())

student.update({"city": "Ahmedabad"})
print("update():", student)

student.pop("age")
print("pop():", student)


# 3. TUPLE METHODS (5 Demonstrations)
print("\n3. TUPLE METHODS")

numbers = (10, 20, 30, 20, 40)

print("Tuple:", numbers)

print("count(20):", numbers.count(20))

print("index(30):", numbers.index(30))

print("Length:", len(numbers))

print("Maximum:", max(numbers))

print("Minimum:", min(numbers))


# 4. SET METHODS (5)
print("\n4. SET METHODS")

colors = {"Red", "Blue", "Green"}

print("Original Set:", colors)

colors.add("Yellow")
print("add():", colors)

colors.remove("Blue")
print("remove():", colors)

colors.update(["Black", "White"])
print("update():", colors)

removed = colors.pop()
print("pop(): Removed ->", removed)
print("After pop():", colors)

colors.clear()
print("clear():", colors)


# 5. IF STATEMENT
print("\n5. IF STATEMENT")

age = 20

if age >= 18:
    print("Eligible to vote.")


# 6. IF-ELSE
print("\n6. IF-ELSE")

number = 15

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 7. IF-ELIF-ELSE
print("\n7. IF-ELIF-ELSE")

marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)

# 8. NESTED IF-ELSE
print("\n8. NESTED IF-ELSE")

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")


# 9. FOR LOOP
print("\n9. FOR LOOP")

for i in range(1, 6):
    print("Iteration:", i)


# 10. WHILE LOOP

print("\n10. WHILE LOOP")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


# 11. BREAK
print("\n11. BREAK")

for i in range(1, 10):
    if i == 6:
        break
    print(i)


# 12. CONTINUE
print("\n12. CONTINUE")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 13. PASS
print("\n13. PASS")

for i in range(1, 4):
    if i == 2:
        pass
    print(i)


# 14. INPUT METHOD
print("\n14. INPUT METHOD")
print("Example:")
print('name = input("Enter your name: ")')


# 15. RANGE FUNCTION
print("\n15. RANGE FUNCTION")

print(list(range(1, 11)))


# 16. LEN FUNCTION
print("\n16. LEN FUNCTION")

language = "Python Programming"

print("Length:", len(language))


# 17. TYPE FUNCTION
print("\n17. TYPE FUNCTION")

value = 25.5

print("Value:", value)
print("Type:", type(value))

