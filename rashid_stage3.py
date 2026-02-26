name = input("Enter student name: ")

marks1 = float(input("Enter marks of Subject 1: "))
marks2 = float(input("Enter marks of Subject 2: "))
marks3 = float(input("Enter marks of Subject 3: "))

if marks1 < 0 or marks1 > 100 or \
   marks2 < 0 or marks2 > 100 or \
   marks3 < 0 or marks3 > 100:
    print("Error: Marks should be between 0 and 100.")
    exit()

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 65:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total:", total, "/300")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)