This folder is a submission of my first task for the Django-Rwanda bootcamp.

MRO Analysis:   If you were to create a DigitalBook class that inherits from 
both Book and a hypothetical Software class( explanation using the C3 Linearization algorithm).
This algorithm follows 3 main principles: 
-Children before Parents: Python always looks at the child class before checking its parents.
-Left to Right: If a class inherits from multiple parents, Python checks them in the order 
they were listed in the class definition.
-No duplicates: even if a class appears multiple times in the inheritance tree, it only
appears once in the MRO.

The Inheritance Structure
Suppose we have the following class hierarchy:
Book: The base class for physical attributes.
Software: A class for digital/executable attributes.
DigitalBook(Book, Software): The child class inheriting from both.

The MRO Path
If you call a method on an instance of DigitalBook, Python follows this specific search order:
1) DigitalBook: Checks the child class first.
2) Book: Checks the first parent listed in the definition (left-to-right).
3) Software: Checks the second parent listed.
4) object: The ultimate base class for all Python objects
