from instructor_class import Instructor
from learner_class import Learner
from user_class import User
from course_class import Course
from enrollment_class import Enrollment
import time

class SLTechBackend:
    def __init__(self):
        self.users = {}
        self.courses = {}
        self.enrollments = []

    def add_user(self, user):
        self.users[user.user_id] = user

    def add_course(self, course):
        self.courses[course.course_id] = course

    def enroll_learner_in_course(self, learner_id, course_id):
        learner = self.users.get(learner_id)
        course = self.courses.get(course_id)
        if learner and course and isinstance(learner, Learner):
            enrollment = Enrollment(learner, course)
            self.enrollments.append(enrollment)
            learner.enroll_course(course)
            enrollment.set_enroll_date()
            return enrollment
        return None

    def remove_learner_from_course(self, learner_id, course_id):
        learner = self.users.get(learner_id)
        course = self.courses.get(course_id)
        if learner and course and isinstance(learner, Learner):
            learner.drop_course(course)
            return True
        return False

    def assign_instructor_to_course(self, instructor_id, course_id):
        instructor = self.users.get(instructor_id)
        course = self.courses.get(course_id)
        if instructor and course and isinstance(instructor, Instructor):
            instructor.add_course(course)
            return True
        return False

    def remove_instructor_from_course(self, instructor_id, course_id):
        instructor = self.users.get(instructor_id)
        course = self.courses.get(course_id)
        if instructor and course and isinstance(instructor, Instructor):
            instructor.remove_course(course)
            return True
        return False

    def retrieve_enrolled_learners(self, course_id):
        course = self.courses.get(course_id)
        if course:
            return course.list_learners()
        return []

    def retrieve_courses_by_learner(self, learner_id):
        learner = self.users.get(learner_id)
        if learner and isinstance(learner, Learner):
            return [course.course_name for course in learner.enrolled_courses]
        return []

    def retrieve_instructor_of_course(self, course_id):
        course = self.courses.get(course_id)
        if course:
            return course.get_instructor()
        return "Course not found"