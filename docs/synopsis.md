# Project Synopsis: EdTech Backend System

## Project Overview
The SL Tech Backend System is a modular backend solution designed for SL Tech, an edtech platform that offers a variety of technical and functional training programs. The system manages learners, instructors, and courses, providing features for user authentication, course enrollment, and instructor assignments. It also facilitates dynamic interactions through an interactive command-line interface.

## Objectives
 1. Design and implement a backend system to manage user credentials, course enrollments, and instructor assignments.
 2. Create modular components that manage users, courses, and enrollments separately, supporting a clean and scalable design.
 3. Provide an interactive interface to allow administrators to perform backend operations, such as adding/removing learners and instructors, enrolling  learners in courses, and managing course details.


## Key Features

 1. User Management:

   - Users can be either learners or instructors, each inheriting from the base User class.
   - Learners can enroll in courses, while instructors can manage courses they teach.
   - Users can update their email, password, and validate their login credentials.

 2. Course Management:

   - The Course class manages course details and tracks the learners and instructors associated with each course.
   - Learners can be added or removed from courses, and instructors can be assigned or removed.

 3. Enrollment Management:

   - The Enrollment class tracks which learners are enrolled in which courses, along with the date of enrollment.
   - It supports dynamic timestamping of enrollment events using Python's time module.

 4. Interactive CLI:

   - An interactive command-line interface allows administrators to:
       - Add learners and instructors.
       - Create new courses.
       - Enroll or remove learners from courses.
       - Assign or remove instructors from courses.
       - List learners and instructors associated with courses.

 5. Modular Design:

   - The system is broken down into individual Python modules for better organization and maintainability. Each class resides in its own script for a clean and scalable structure.

## File Structure
The project follows a modular structure, with each component organized into its own script:
```bash
SLTech-Backend-System/
│
├── src/
│   ├── user_class.py           # Contains the User class
│   ├── learner_class.py        # Contains the Learner class
│   ├── instructor_class.py     # Contains the Instructor class
│   ├── course_class.py         # Contains the Course class
│   ├── enrollment_class.py     # Contains the Enrollment class
│   ├── EdTechBackend.py        # SLTechBackend class
│   ├── user_input_interface.py # Contains the main program logic
│
├── docs/
│   └── README.md               # Overview and usage
│   └── synopsis.md             # Detailed project synopsis
```
## Technologies Used
   - Python: The project is developed using Python for its simplicity, versatility, and strong support for object-oriented programming.
   - Modular Design: The code is organized into separate modules to enhance maintainability and scalability.

## Conclusion
The SL Tech Backend System is a well-structured, modular solution to manage the backend for an edtech platform. Its modularity ensures future scalability, while the interactive CLI allows administrators to easily manage users, courses, and enrollments. By separating classes and functionalities into their own scripts, the system remains clean, maintainable, and adaptable for future enhancements.

