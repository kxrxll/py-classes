class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAverage grade: {self.average_grade()}\nCourses in " \
               f"progress: {' '.join(self.courses_in_progress)}\nFinished courses: {' '.join(self.finished_courses)}\n"

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def average_grade(self):
        grade_sum = 0
        courses_number = 0
        for course in self.grades:
            courses_number += 1
            result = sum(self.grades[course]) / len(self.grades[course])
            grade_sum += result
        return grade_sum / courses_number


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAverage grade: {self.average_grade()}"

    def average_grade(self):
        grade_sum = 0
        courses_number = 0
        for course in self.grades:
            courses_number += 1
            result = sum(self.grades[course]) / len(self.grades[course])
            grade_sum += result
        return grade_sum / courses_number


class Reviewer(Mentor):
    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'


best_student = Student('Ruby', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lc(cool_lecturer, 'Python', 20)
best_student.rate_lc(cool_lecturer, 'Python', 30)
best_student.rate_lc(cool_lecturer, 'Python', 40)

print(best_student)
print(cool_reviewer)
print(cool_lecturer)
