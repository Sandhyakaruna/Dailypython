
def read_employee_data(file_path):
    employees = []
    with open(file_path, 'r') as file:
        for line in file:
            name, age, department, salary = line.strip().split(', ')
            employees.append({
                'name': name,
                'age': int(age),
                'department': department,
                'salary': float(salary)
            })
    return employees

def calculate_average_salaries(employees):
    department_salaries = {}
    for employee in employees:
        department = employee['department']
        salary = employee['salary']
        if department not in department_salaries:
            department_salaries[department] = []
        department_salaries[department].append(salary)
    
    average_salaries = {dept: sum(salaries) / len(salaries) for dept, salaries in department_salaries.items()}
    return average_salaries


def get_highest_average_salary_department(average_salaries):
    return max(average_salaries, key=average_salaries.get)


def write_results_to_file(average_salaries, highest_salary_dept, output_file):
    with open(output_file, 'w') as file:
        file.write("Average Salaries by Department:\n")
        for dept, avg_salary in average_salaries.items():
            file.write(f"{dept}: {avg_salary:.2f}\n")
        file.write("\n")
        file.write(f"Department with the highest average salary: {highest_salary_dept}\n")


def main():
    input_file = 'employees.txt'
    output_file = 'salary_report.txt'
    
    employees = read_employee_data(input_file)
    average_salaries = calculate_average_salaries(employees)
    highest_salary_dept = get_highest_average_salary_department(average_salaries)
    
    write_results_to_file(average_salaries, highest_salary_dept, output_file)
    print("Results have been written to", output_file)

# Run the main function
if __name__ == "__main__":
    main()
