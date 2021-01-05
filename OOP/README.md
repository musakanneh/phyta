# Object Oriented Programming (OOP)
procedure-oriented way of programming - is centered on block of statement which manipulates data
## OOP General Concept
- Classes and objects are the two main aspects of object oriented programming.
    - A class creates a new type
    -  objects are instances of the class
- Objects can store data using ordinary variables that belong to the object.
- Variables that belong to an object or class are referred to as fields.
- Objects can also have functionality by using functions that belong to a class.
    - Such functions are called methods of the class.
- Collectively, the fields and methods can be referred to as the attributes of that class.
- Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself.
    - They are called instance variables and class variables respectively.
 ## The self
 Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.