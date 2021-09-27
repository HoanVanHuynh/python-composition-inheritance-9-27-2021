from course import Course
class Student:
    def __init__(self, sId, sName, sGrade, cId, cTitle, cGrade):
        self._studentId = sId 
        self._name = sName 
        self._grade = sGrade 
        # self._course = Course(cId, cTitle, cGrade) #composition

        self._courses = [Course(cId, cTitle, cGrade)] 
    
    def setStudentId(self, studentId):
        self._studentId = studentId 
    
    def setName(self, name):
        self._name = name 
    
    def setGrade(self, grade):
        self._grade = grade 

    # def setCourse(self, course):
    #     self._course = course 
    
    def setCourse(self, course):
        self._courses.append(course)

    def getStudentId(self):
        return self._studentId 
    
    def getName(self):
        return self._name 

    def getGrade(self):
        return self._grade 

    # def getCourse(self):
    #     return self._course 

    def getCourses(self):
        return self._courses 

    def getCourse(self, index):
        return self._courses[index] 

