# task 1 

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# task 2 

students_approved = []
for i in range(len(students)):
    if grades[i] >= 80:
        print(students[i], grades[i], activities[i])
        students_approved.append(students[i])

# task 3

print("Students approved:", students_approved)

