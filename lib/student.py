# ./lib/student.py
class Student:
    all = []

    def __init__(self, name):
        self.name = name
        self._enrollments = []  # stores Enrollment objects
        self._grades = {}       # key: Enrollment, value: grade
        Student.all.append(self)

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        if not self._grades:
            return 0
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses
