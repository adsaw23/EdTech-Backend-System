from instructor_class import Instructor
from learner_class import Learner
from user_class import User
from course_class import Course
import time

class Enrollment:
    def __init__(self, learner, course):
        self.learner = learner
        self.course = course
        self.enroll_date = None
        self.status = "enrolled"

    def set_enroll_date(self):
        self.enroll_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def update_status(self, status):
        self.status = status
