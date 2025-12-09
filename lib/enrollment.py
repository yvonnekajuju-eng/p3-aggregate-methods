from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}  # key: Enrollment instance, value: numeric grade

    def enroll(self, course):
        if not isinstance(course, Course):
            raise TypeError("course must be an instance of Course")
        enrollment = Enrollment(self, course)
        self._enrollments.append(enrollment)
        course.add_enrollment(enrollment)

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        """Returns the number of courses this student is enrolled in."""
        return len(self._enrollments)

    def aggregate_average_grade(self):
        """Returns the average grade across all enrollments."""
        if not self._grades:
            return 0
        total = sum(self._grades.values())
        return total / len(self._grades)


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if not isinstance(enrollment, Enrollment):
            raise TypeError("enrollment must be an instance of Enrollment")
        self._enrollments.append(enrollment)

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []

    def __init__(self, student, course):
        if not isinstance(student, Student) or not isinstance(course, Course):
            raise TypeError("Invalid types for student and/or course")
        self.student = student
        self.course = course
        self._enrollment_date = datetime.now()
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        """Returns a dictionary with counts of enrollments per date."""
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
