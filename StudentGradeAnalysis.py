# Sample list of student dictionaries
students = [
    {"name": "Alice", "age": 20, "grades": [85, 92, 78]},
    {"name": "Bob", "age": 22, "grades": [79, 85, 88]},
    {"name": "Charlie", "age": 21, "grades": [90, 91, 92]},
    {"name": "David", "age": 23, "grades": [70, 75, 80]},
    {"name": "Eva", "age": 20, "grades": [88, 82, 85]}
]

def calculate_average(grades):
    return sum(grades) / len(grades)
for student in students:
    student['average_grade'] = calculate_average(student['grades'])

# Calculate the overall class average
class_average = calculate_average([student['average_grade'] for student in students])

# List of students with an average grade above the class average
above_average_students = [student['name'] for student in students if student['average_grade'] > class_average]

# Print results
print("Student Averages:")
for student in students:
    print(f"{student['name']}: {student['average_grade']:.2f}")

print(f"\nClass Average: {class_average:.2f}")

print("\nStudents above class average:")
for student in above_average_students:
    print(student)
