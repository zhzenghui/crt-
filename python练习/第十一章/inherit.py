#-*-coding:UTF-8-*-
#Filename : inherit.py
#继承

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name = name
        self.age  = age
        print '(Initialized SchoolMember: %s)'%self.name
        
    def __del__(self):
        '''Tell my details.'''
        print 'Name: "%s" Age:"%s"'%(self.name,self.age)
        
class Teacher:
    '''Repressents a teacher'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print '(Initialized Teacher: %s)'%self.name
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "%d"' %self.salary
        
class Student:
    '''Repressents a Student'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print '(Initialized Student: %s)'%self.name
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "%d"' %self.marks
        
        
t = Teacher('Mrs.Shrividya',40,30000)
s = Student('Yang.xiao',25,100)

print #prints a blank line

members = [t,s]
for member in members:
    members.tell() #works for both Teachers and Students