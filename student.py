from person import Person

class Student(Person):
    pass

    # Method Overriding
    def set_email(self):
        self.email = "student." + self.name + "@ahorizoncolumbus.org"