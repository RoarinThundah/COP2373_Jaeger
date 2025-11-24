import numpy as np
import csv

# Configuration
FILE_NAME = 'grades.csv'
exam_names = ['Exam 1', 'Exam 2', 'Exam 3']
grades_list = []


# Load the data into a NumPy array using the CSV module
try:
    # Use 'with open' to ensure the file is properly closed after reading
    with open(FILE_NAME, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Skip the header row
        try:
            next(reader)
        except StopIteration:
            print("Error: The CSV file is empty.")
            exit()

        # Iterate through each student row
        for row in reader:
            # The grades are assumed to start at index 2
            # Convert the grade strings to floats
            try:
                grades = [float(grade) for grade in row[2:]]
                grades_list.append(grades)
            except ValueError:
                print(f"Skipping row due to non-numeric grade data: {row}")
                continue # Skip rows with invalid grade data

    # Convert the final list of lists into a NumPy array
    grades_array = np.array(grades_list)

except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found.")
    print("Please ensure the CSV file is in the same directory as this script.")
    exit()

# 2. Print the first few rows of the dataset
print("1. Data Loaded Directly from File & 2. First 5 Rows")
print("---------------------------------------------------------")
print(f"File: {FILE_NAME}")
print(f"NumPy Array Shape: {grades_array.shape}")
print("\nFirst 5 Rows:")
print(grades_array[:5])
print("---------------------------------------------------------")


# Calculate Exam-Specific Statistics
def calculate_exam_stats(data, exam_names):
    """Calculates and prints statistical summary for each exam (column)."""
    print("3. Statistics for Each Exam (axis=0)")
    print("---------------------------------------------------------")

    # NumPy calculations along axis=0 (down the rows, for each exam)
    means = np.mean(data, axis=0)
    medians = np.median(data, axis=0)
    stds = np.std(data, axis=0)
    mins = np.min(data, axis=0)
    maxs = np.max(data, axis=0)

    # Print results in a structured format
    print(f"{'Statistic':<15} | {'Exam 1':<8} | {'Exam 2':<8} | {'Exam 3':<8}")
    print("-" * 50)
    print(f"{'Mean (Avg)':<15} | {means[0]:<8.2f} | {means[1]:<8.2f} | {means[2]:<8.2f}")
    print(f"{'Median':<15} | {medians[0]:<8.2f} | {medians[1]:<8.2f} | {medians[2]:<8.2f}")
    print(f"{'Std Dev':<15} | {stds[0]:<8.2f} | {stds[1]:<8.2f} | {stds[2]:<8.2f}")
    print(f"{'Minimum':<15} | {mins[0]:<8.0f} | {mins[1]:<8.0f} | {mins[2]:<8.0f}")
    print(f"{'Maximum':<15} | {maxs[0]:<8.0f} | {maxs[1]:<8.0f} | {maxs[2]:<8.0f}")
    print("---------------------------------------------------------")

# Execute Function 1
calculate_exam_stats(grades_array, exam_names)


# Overall Statistics
print("4. Overall Statistics (All Grades Combined)")
print("---------------------------------------------------------")

# NumPy calculations on the entire array (treated as one set of data)
overall_mean = np.mean(grades_array)
overall_median = np.median(grades_array)
overall_std = np.std(grades_array)
overall_min = np.min(grades_array)
overall_max = np.max(grades_array)

print(f"Overall Mean Grade: {overall_mean:.2f}")
print(f"Overall Median Grade: {overall_median:.2f}")
print(f"Overall Standard Deviation: {overall_std:.2f}")
print(f"Overall Minimum Grade: {overall_min}")
print(f"Overall Maximum Grade: {overall_max}")
print("---------------------------------------------------------")


# Pass/Fail Analysis and Overall Percentage
def analyze_pass_fail(data, exam_names, passing_grade=60):

    # Use a boolean mask: True if grade >= 60, False otherwise
    passed_mask = data >= passing_grade

    # Pass/Fail Counts per Exam
    print(f"5. Pass/Fail Analysis (Passing Grade $\\geq$ {passing_grade})")
    print("---------------------------------------------------------")

    num_passed = np.sum(passed_mask, axis=0)
    total_students = data.shape[0]
    num_failed = total_students - num_passed

    # Print results in a structured format
    print(f"{'Exam':<8} | {'Passed':<8} | {'Failed':<8}")
    print("-" * 28)
    for i, exam in enumerate(exam_names):
        print(f"{exam:<8} | {num_passed[i]:<8} | {num_failed[i]:<8}")
    print("---------------------------------------------------------")

    # Overall Pass Percentage
    print("6. Overall Pass Percentage")
    print("---------------------------------------------------------")

    total_grades = data.size
    total_passed = np.sum(passed_mask)
    overall_pass_percentage = (total_passed / total_grades) * 100

    print(f"Total Grades Analyzed: {total_grades}")
    print(f"Total Grades Passed: {total_passed}")
    print(f"Overall Pass Percentage: {overall_pass_percentage:.2f}%")
    print("---------------------------------------------------------")

# Execute Function 2
analyze_pass_fail(grades_array, exam_names)