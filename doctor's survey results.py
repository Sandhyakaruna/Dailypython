def find_non_working_doctors():
    try:
        # Input size of the first list
        n1 = int(input())
        if n1 <= 0:
            print("Invalid list size")
            return
        
        # Input elements for the first list
        first_list = []
        for _ in range(n1):
            doctor_id = int(input())
            if doctor_id <= 0:
                print("Invalid Id")
                return
            first_list.append(doctor_id)
        
        # Input size of the second list
        n2 = int(input())
        if n2 <= 0:
            print("Invalid list size")
            return
        
        # Input elements for the second list
        second_list = []
        for _ in range(n2):
            doctor_id = int(input())
            if doctor_id <= 0:
                print("Invalid Id")
                return
            second_list.append(doctor_id)
        
        # Convert lists to sets
        set_first = set(first_list)
        set_second = set(second_list)
        
        # Find non-working doctors
        non_working_doctors = [doctor_id for doctor_id in first_list if doctor_id in set_first and doctor_id not in set_second]
        
        # Output result
        if non_working_doctors:
            print("Not Working Doctors' IDs are:")
            for doctor_id in non_working_doctors:
                print(doctor_id)
        else:
            print("No non-working doctors")

    except ValueError:
        print("Invalid input")

# Call the function
find_non_working_doctors()
