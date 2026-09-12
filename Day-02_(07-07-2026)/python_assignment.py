# Python Assignment
# Edunet Foundation Internship

# -------------------------------
# 1. LIST - 5 METHODS
# -------------------------------

my_list = [10, 20, 30]

my_list.append(40)          # Add item
my_list.insert(1, 15)       # Insert item
my_list.remove(20)          # Remove item
my_list.pop()               # Remove last item
my_list.sort()              # Sort list

print("List:", my_list)


# -------------------------------
# 2. DICTIONARY - 5 METHODS
# -------------------------------

student = {
    "name": "Rishi",
    "age": 21,
    "marks": 85
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student.update({"city": "Palanpur"})
print("Updated Dictionary:", student)

student.pop("age")
print("After pop:", student)


# -------------------------------
# 3. TUPLE - 5 OPERATIONS
# -------------------------------

my_tuple = (10, 20, 30, 20, 40)

print("Tuple:", my_tuple)
print("Length:", len(my_tuple))
print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))
print("First item:", my_tuple[0])


# -------------------------------
# 4. SET - 5 METHODS
# -------------------------------

my_set = {10, 20, 30}

my_set.add(40)
print("After add:", my_set)

my_set.remove(20)
print("After remove:", my_set)

my_set.discard(50)
print("After discard:", my_set)

my_set.update({50, 60})
print("After update:", my_set)

my_set.pop()
print("After pop:", my_set)


# -------------------------------
# 5. IF STATEMENT
# -------------------------------

age = 21

if age >= 18:
    print("You are eligible to vote")


# -------------------------------
# 6. IF-ELSE
# -------------------------------

number = 10

if number > 0:
    print("Positive number")
else:
    print("Negative number")


# -------------------------------
# 7. IF-ELIF-ELSE
# -------------------------------

marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 70:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
else:
    print("Grade C")


# -------------------------------
# 8. NESTED IF-ELSE
# -------------------------------

age = 20

if age >= 18:
    if age >= 21:
        print("Adult and eligible")
    else:
        print("Adult")
else:
    print("Minor")


# -------------------------------
# 9. BREAK
# -------------------------------

for i in range(1, 6):
    if i == 4:
        break
    print("Break:", i)


# -------------------------------
# 10. CONTINUE
# -------------------------------

for i in range(1, 6):
    if i == 3:
        continue
    print("Continue:", i)


# -------------------------------
# 11. PASS
# -------------------------------

for i in range(3):
    if i == 1:
        pass
    print("Pass:", i)


# -------------------------------
# 12. INPUT FUNCTION
# -------------------------------

name = input("Enter your name: ")
print("Hello", name)


# -------------------------------
# 13. RANGE FUNCTION
# -------------------------------

for i in range(1, 6):
    print("Range:", i)


# -------------------------------
# 14. LEN FUNCTION
# -------------------------------

text = "Python"

print("Length:", len(text))


# -------------------------------
# 15. TYPE FUNCTION
# -------------------------------

number = 10

print("Type:", type(number))


# -------------------------------
# 16. FOR LOOP
# -------------------------------

for i in range(1, 6):
    print("For Loop:", i)


# -------------------------------
# 17. WHILE LOOP
# -------------------------------

i = 1

while i <= 5:
    print("While Loop:", i)
    i = i + 1
