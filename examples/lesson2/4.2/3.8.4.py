# -*- encoding: utf-8 -*-
"""
Экземпляры
"""

#Just pretend that the class object is a 
#parameterless function that returns a new instance of the class.

class MyClass:
    "A simple example class" 
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()

# creates a new instance of the class and assigns this object to the local variable x.