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

## The __ init __ method
- The __ init __ method is run as soon as an object of a class is instantiated (i.e. created)
- The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object.
## Class And Object Variables
### The data part
- The data part, i.e. fields, are nothing but ordinary variables that are bound to the namespaces of the classes and objects. 
- This means that these names are valid within the context of these classes and objects only. That's why they are called name spaces.
- There are two types of fields:
    - class variables: are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.
    - object variables: are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance. 
- The are classified depending on whether the class or the object owns the variables respectively.
- 