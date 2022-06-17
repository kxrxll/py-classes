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

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return "Error"

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

    def average_grade_by_course(self, course):
        return sum(self.grades[course]) / len(self.grades[course])


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

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            return "Error"

    def average_grade(self):
        grade_sum = 0
        courses_number = 0
        for course in self.grades:
            courses_number += 1
            result = sum(self.grades[course]) / len(self.grades[course])
            grade_sum += result
        return grade_sum / courses_number

    def average_grade_by_course(self, course):
        return sum(self.grades[course]) / len(self.grades[course])


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
worst_student = Student('Ruby', 'Eman', 'your_gender')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
hot_lecturer = Lecturer('Some', 'Buddy')
hot_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 14)
cool_reviewer.rate_hw(best_student, 'Python', 18)

cool_reviewer.rate_hw(worst_student, 'Python', 2)
cool_reviewer.rate_hw(worst_student, 'Python', 4)
cool_reviewer.rate_hw(worst_student, 'Python', 10)

best_student.rate_lc(cool_lecturer, 'Python', 24)
best_student.rate_lc(cool_lecturer, 'Python', 36)
best_student.rate_lc(cool_lecturer, 'Python', 48)

best_student.rate_lc(hot_lecturer, 'Python', 48)
best_student.rate_lc(hot_lecturer, 'Python', 92)
best_student.rate_lc(hot_lecturer, 'Python', 1000000000)

print(best_student)
print(cool_reviewer)
print(cool_lecturer)
print(worst_student < best_student)
print(cool_lecturer > hot_lecturer)


def print_average_by_students(students_list, course):
    sum_of_grades = 0
    number_of_students = 0
    for student in students_list:
        if isinstance(student, Student):
            sum_of_grades += student.average_grade_by_course(course)
            number_of_students += 1
    average_grade = sum_of_grades / number_of_students
    print(f'Average grade by students for {course} is {average_grade}')

def print_average_by_lecturer(lecturers_list, course):
    sum_of_grades = 0
    number_of_lecturers = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer):
            sum_of_grades += lecturer.average_grade_by_course(course)
            number_of_lecturers += 1
    average_grade = sum_of_grades / number_of_lecturers
    print(f'Average grade by lecturers for {course} is {average_grade}')


print_average_by_students([best_student, worst_student], "Python")
print_average_by_lecturer([hot_lecturer, cool_lecturer], "Python")
