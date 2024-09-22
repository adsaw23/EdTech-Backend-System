from user_class import User

class Learner(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.enrolled_courses = []

    def enroll_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_learner(self)

    def drop_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            course.remove_learner(self)
