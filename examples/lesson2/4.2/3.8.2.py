# -*- encoding: utf-8 -*-
"""
Класс с конструктором
"""

class Worker:
    def __init__(self, name, pay):            
        self.name = name                      
        self.pay  = pay

    def lastName(self):
        return self.name.split(  )[-1]        

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent )          

bob = Worker('A', 50000)              
sue = Worker('B', 60000)              
print bob.lastName(  )                        
print sue.lastName(  )                        
sue.giveRaise(.10)                            
print sue.pay