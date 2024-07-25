def get_student_details():
    student_list = []
    
    while True:
        try:
            num_students = int(input("Enter the no of student details to be created: "))
            if num_students <= 0:
                print("Invalid Input")
                if student_list:
                    print("Here's the list of student details:")
                    for student in student_list:
                        print(student)
                return

            for _ in range(num_students):
                name = input("Name: ")
                age = int(input("Age: "))
                if age <= 10 or age >= 80:
                    print("Invalid Input")
                    if student_list:
                        print("Here's the list of student details:")
                        for student in student_list:
                            print(student)
                    return
                student_list.append({"Name": name, "Age": age})

            while True:
                choice = int(input("Do you want to add more students' details to the list of dictionary? If yes, press 1, else press 0: "))
                if choice == 1:
                    break
                elif choice == 0:
                    print("Here's the list of student details:")
                    for student in student_list:
                        print(student)
                    
                    sorted_list = sorted(student_list, key=lambda x: x['Name'])
                    print("\nHere's the list of student details sorted with respect to name:")
                    for student in sorted_list:
                        print(student)
                    return
                else:
                    print("Invalid Input")
                    print("Here's the list of student details:")
                    for student in student_list:
                        print(student)
                    sorted_list = sorted(student_list, key=lambda x: x['Name'])
                    print("\nHere's the list of student details sorted with respect to name:")
                    for student in sorted_list:
                        print(student)
                    return
        except ValueError:
            print("Invalid Input")
            if student_list:
                print("Here's the list of student details:")
                for student in student_list:
                    print(student)
            return

# Run the function
get_student_details()
