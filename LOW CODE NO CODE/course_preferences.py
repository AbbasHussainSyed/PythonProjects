# Import necessary libraries
import random

# Sample data for courses and students
courses = {
    "CSCI101": ["Alice", "Bob", "Charlie", "David"],
    "MATH201": ["Alice", "Eve", "Frank"],
    "PHYS301": ["Bob", "Charlie", "David", "Eve"]
}


# Function to match students based on course preferences
# BEGIN: ed8c6549bwf9
def match_students(course_preferences):
    matched_students = {}

    for course in course_preferences:
        students_in_course = courses.get(course, [])

        if students_in_course:
            # Randomly select a student from the list
            matched_student = random.choice(students_in_course)
            matched_students[course] = matched_student

    return matched_students
    matched_students = {}

    for course in course_preferences:
        students_in_course = courses.get(course, [])

        if students_in_course:
            # Randomly select a student from the list
            matched_student = random.choice(students_in_course)
            matched_students[course] = matched_student

    return matched_students


# Main program
if __name__ == "__main__":
    # Get user input for course preferences
    course_preferences = input("Enter your course preferences (comma-separated): ").split(",")

    # Match students based on course preferences
    matched_students = match_students(course_preferences)

    # Display matched students
    if matched_students:
        print("Matched Students:")
        for course, student in matched_students.items():
            print(f"Course: {course}, Student: {student}")
    else:
        print("No matches found.")