# Empty employee data at the start
employees = {}

# Function to display employee information
def show_info(key_name):
    data = employees[key_name]
    print(f"\nEmployee Information:")
    print(f"Name       : {data['name']}")
    print(f"Position   : {data['position']}")
    print("Experience :")
    for experience in data['experience']:
        print(f" - {experience}")

# Main application loop
while True:
    print('\nWelcome to the Employee Data Application')
    print('1. Check employee')
    print('1.5. View all employees')
    print('2. Add employee')
    print('3. Remove employee')
    print('0. Exit')

    choice = input('Please select an action: ').strip()

    # Option 1: Check employee
    if choice == '1':
        search_name = input("Enter the employee name to search (0 - to stop): ").strip().lower()
        while search_name != '0':
            if search_name in employees:
                show_info(search_name)
            else:
                print("\nEmployee not found.")
            search_name = input("Enter the employee name to search (0 - to stop): ").strip().lower()

    # Option 1.5: View all employees
    elif choice == '1.5':
        if employees:
            print("\n=== All Employees List ===")
            for key in employees:
                show_info(key)
        else:
            print("\nNo employee data yet.")

    # Option 2: Add new employee
    elif choice == '2':
        print('Please add a new employee')
        new_name = input("Name: ").strip().lower()
        new_position = input("Position: ").strip()

        new_experience = []
        total_experience = int(input("How many experiences do you want to add? "))

        for i in range(total_experience):
            exp = input(f"Experience #{i+1}: ").strip()
            new_experience.append(exp)

        employees[new_name] = {
            "name": new_name.title(),
            "position": new_position,
            "experience": new_experience
        }
        print("\nEmployee successfully added!")

    # Option 3: Remove employee
    elif choice == '3':
        print('Please remove an employee')
        remove_name = input("Enter the employee name to remove: ").strip().lower()
        if remove_name in employees:
            del employees[remove_name]
            print("Employee successfully removed.")
        else:
            print("Employee not found.")

    # Option 0: Exit the application
    elif choice == '0':
        print("Thank you for using the application.")
        break

    # Invalid option
    else:
        print("Invalid choice. Please try again.")
