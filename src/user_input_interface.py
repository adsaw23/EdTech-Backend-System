from instructor_class import Instructor
from learner_class import Learner
from user_class import User
from course_class import Course
from enrollment_class import Enrollment
from EdTechBackend_class import SLTechBackend
import time

def user_input_interface():
    backend = SLTechBackend()

    while True:
        print("\n1. Add User")
        print("2. Add Course")
        print("3. Enroll Learner in Course")
        print("4. Remove Learner from Course")
        print("5. Assign Instructor to Course")
        print("6. Remove Instructor from Course")
        print("7. List Learners in Course")
        print("8. List Courses by Learner")
        print("9. Get Instructor of Course")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_type = input("Enter user type (learner/instructor): ")
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")

            if user_type == 'learner':
                user = Learner(user_id, name, email, password)
            elif user_type == 'instructor':
                user = Instructor(user_id, name, email, password)
            else:
                print("Invalid user type.")
                continue

            backend.add_user(user)
            print(f"{user_type.capitalize()} added successfully.")

        elif choice == '2':
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            course = Course(course_id, course_name)
            backend.add_course(course)
            print("Course added successfully.")

        elif choice == '3':
            learner_id = input("Enter learner ID: ")
            course_id = input("Enter course ID: ")
            enrollment = backend.enroll_learner_in_course(learner_id, course_id)
            if enrollment:
                print("Learner enrolled successfully.")
            else:
                print("Enrollment failed. Check learner and course IDs.")

        elif choice == '4':
            learner_id = input("Enter learner ID: ")
            course_id = input("Enter course ID: ")
            success = backend.remove_learner_from_course(learner_id, course_id)
            if success:
                print("Learner removed from course successfully.")
            else:
                print("Failed to remove learner. Check learner and course IDs.")

        elif choice == '5':
            instructor_id = input("Enter instructor ID: ")
            course_id = input("Enter course ID: ")
            success = backend.assign_instructor_to_course(instructor_id, course_id)
            if success:
                print("Instructor assigned successfully.")
            else:
                print("Assignment failed. Check instructor and course IDs.")

        elif choice == '6':
            instructor_id = input("Enter instructor ID: ")
            course_id = input("Enter course ID: ")
            success = backend.remove_instructor_from_course(instructor_id, course_id)
            if success:
                print("Instructor removed successfully.")
            else:
                print("Removal failed. Check instructor and course IDs.")

        elif choice == '7':
            course_id = input("Enter course ID: ")
            learners = backend.retrieve_enrolled_learners(course_id)
            if learners:
                print("Enrolled learners:", ", ".join(learners))
            else:
                print("No learners enrolled in this course or invalid course ID.")

        elif choice == '8':
            learner_id = input("Enter learner ID: ")
            courses = backend.retrieve_courses_by_learner(learner_id)
            if courses:
                print("Courses enrolled by learner:", ", ".join(courses))
            else:
                print("No courses found for this learner or invalid learner ID.")

        elif choice == '9':
            course_id = input("Enter course ID: ")
            instructor = backend.retrieve_instructor_of_course(course_id)
            print("Instructor of the course:", instructor)

        elif choice == '10':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Call the user input interface to start the interactive session
user_input_interface()