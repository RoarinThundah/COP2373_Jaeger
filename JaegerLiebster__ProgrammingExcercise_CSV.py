import csv
import os  # Using this just to make one of the error messages a bit nicer


def get_integer_input(prompt):

    # utility function to safely get an integer from user. Will loop until valid int is recieved
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def create_grades_file():

    # allows the instructor to enter student data and writes it to grades.csv.

    print("Create New Grades File:")

    # Get the number of students
    num_students = get_integer_input("How many students do you want to enter? ")

    header = ['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3']

    #  Use 'with' to open the file for writing
    #    'w' mode overwrites the file if it exists (or creates it)
    #    newline='' is important for the csv module to handle line endings correctly
    try:
        with open('grades.csv', mode='w', newline='') as file:
            # Create a csv.writer object
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(header)

            print("\nPlease enter data for each student.")

            # Loop for each student
            for i in range(num_students):
                print(f"\nStudent {i + 1}")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")

                # Use the helper function for robust integer input
                exam1 = get_integer_input("Enter Exam 1 grade: ")
                exam2 = get_integer_input("Enter Exam 2 grade: ")
                exam3 = get_integer_input("Enter Exam 3 grade: ")

                # Write the student's record as a new row
                writer.writerow([first_name, last_name, exam1, exam2, exam3])

        print(f"\nSuccessfully created and saved data to grades.csv")

    except IOError as e:
        print(f"Error writing to file: {e}")


def read_and_display_grades():

   # Reads grades.csv file using 'with' keyword and displays data in a formatted, tabular way

    print("Displaying Student Grades:")

    try:
        # Use 'with' to open the file for reading ('r' mode)
        with open('grades.csv', mode='r') as file:

            # Create a csv.reader object
            reader = csv.reader(file)

            # Read first row
            try:
                header = next(reader)
            except StopIteration:
                print("Error: The file is empty.")
                return

            #    Print the header with formatting
            #    {:<15} means left-align within 15 spaces
            #    {:>8} means right-align within 8 spaces
            print(f"\n{header[0]:<15} {header[1]:<15} {header[2]:>8} {header[3]:>8} {header[4]:>8}")
            print("-" * 60)  # Print a separator line

            #    Loop through the rest of the rows in the file
            for row in reader:
                # Print each student's data using the same formatting
                print(f"{row[0]:<15} {row[1]:<15} {row[2]:>8} {row[3]:>8} {row[4]:>8}")

            print("\nEnd of Report")

    except FileNotFoundError:
        print("\nError: 'grades.csv' not found.")
        print("Please run option 1 to create the file first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main part of script to run functions
if __name__ == "__main__":
    while True:
        print("\n Student Gradebook:")
        print("1. Create/Overwrite grades.csv")
        print("2. Display grades.csv")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            create_grades_file()
        elif choice == '2':
            read_and_display_grades()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
