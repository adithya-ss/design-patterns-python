class Person:
    def __init__(self):
        self.name = None
        self.position = None
    
    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}"
    
    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()
    
    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self

if __name__ == "__main__":
    pb = PersonJobBuilder()
    person = pb.called("John").works_as_a("Software Engineer").build()
    print(person)