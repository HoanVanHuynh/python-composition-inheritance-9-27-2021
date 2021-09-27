"""
Main Program
Composition example in Python 
""" 

from student import Student
from course import Course 

def printInfo(student):
    print("Student Id", student.getStudentId())
    print("Student Name", student.getName())
    print("Student Grade", student.getGrade())
    
    # print("Course Id",      student.getCourse().getCourseId())
    # print("Course Title: ", student.getCourse().getCourseTitle())
    # print("Course Grade: ", student.getCourse().getCourseGrade())
        
    # print("Course Id",      student.getCourse(0).getCourseId())
    # print("Course Title: ", student.getCourse(0).getCourseTitle())
    # print("Course Grade: ", student.getCourse(0).getCourseGrade())

    for i in range(len(student.getCourses())):
        print("Course Id",      student.getCourse(i).getCourseId())
        print("Course Title: ", student.getCourse(i).getCourseTitle())
        print("Course Grade: ", student.getCourse(i).getCourseGrade())

def main():
    student = Student(1111, 'Jill', 'Freshman', 'PY101', 'Python 101', 'A')
    printInfo(student)

    course = Course('Jv202', 'Java 1', 'B+') 
    student.setCourse(course) 
    print('-'*20)
    printInfo(student)

    # student.getCourse().setCourseGrade('A+')
    student.getCourse(0).setCourseGrade('A-')

    print('-'*20)
    printInfo(student)


# Start program here
main() 
