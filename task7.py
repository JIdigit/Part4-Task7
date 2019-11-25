class Student:

    def __init__(self, name, age, lesson):
        self.name = name
        self.age = age
        self.major = lesson

    def output(self):
         return 'name: ', self.name, ' ', 'age: ', str(self.age), ' ', 'major: ', self.major

    
    

Steve = Student("Steven Schultz", 23, "English").output()
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")

print(''.join(Steve))