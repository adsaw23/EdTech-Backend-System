from user_class import User

class Instructor(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.courses_taught = []

    def add_course(self, course):
        if course not in self.courses_taught:
            self.courses_taught.append(course)
            course.set_instructor(self)

    def remove_course(self, course):
        if course in self.courses_taught:
            self.courses_taught.remove(course)
            course.remove_instructor()