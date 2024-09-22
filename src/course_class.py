from instructor_class import Instructor
from learner_class import Learner
from user_class import User

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.learners = []
        self.instructor = None

    def add_learner(self, learner):
        if learner not in self.learners:
            self.learners.append(learner)

    def remove_learner(self, learner):
        if learner in self.learners:
            self.learners.remove(learner)

    def set_instructor(self, instructor):
        self.instructor = instructor

    def remove_instructor(self):
        self.instructor = None

    def list_learners(self):
        return [learner.name for learner in self.learners]

    def get_instructor(self):
        return self.instructor.name if self.instructor else "No instructor assigned"