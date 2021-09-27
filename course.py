class Course:
    def __init__(self, courseId, courseTitle, courseGrade):
        self._courseId = courseId
        self._courseTitle = courseTitle
        self._courseGrade = courseGrade 
    
    def setCourseId(self, courseId):
        self._courseId = courseId 
    
    def setCourseTitle(self, courseTitle):
        self._courseTitle = courseTitle 
    
    def setCourseGrade(self, courseGrade):
        self._courseGrade = courseGrade 
    
    def getCourseId(self):
        return self._courseId 
    
    def getCourseTitle(self):
        return self._courseTitle 
    
    def getCourseGrade(self):
        return self._courseGrade