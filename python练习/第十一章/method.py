#-*- coding:UTF-8 -*-

#Filename : method.py
#使用对象方法
import sys
class Person:
    def sayHi(self):
        print 'Hello, how are you?'
        
p = Person()
p.sayHi()

# This short example can also be written as Person().sayHi()