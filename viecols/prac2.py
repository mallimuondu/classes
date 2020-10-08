class student:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
    def fulldecription(self):
        return "welcome {} {}".format(self.first,self.last)


class discription(student):
    def __init__(self,first,last,age = None,marks=None):
        student.__init__(self,first,last)
        if age is None and marks is None:
            self.age =  []
            self.marks =  []
        else:
            self.age = age  
            self.marks = marks  