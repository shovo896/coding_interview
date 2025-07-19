# inheritance_tool.py

class ExerciseBase:
    def run(self):
        raise NotImplementedError("Please override in derived class")


# 1. Basic Inheritance
class BasicInheritance(ExerciseBase):
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, student_id):
            super().__init__(name, age)
            self.student_id = student_id

        def show(self):
            print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

    def run(self):
        s = self.Student("Alice", 21, "S123")
        s.show()


# 2. Method Overriding
class MethodOverriding(ExerciseBase):
    class Animal:
        def speak(self):
            print("Animal speaks")

    class Dog(Animal):
        def speak(self):
            print("Dog barks")

    def run(self):
        d = self.Dog()
        d.speak()


# 3. Using super()
class SuperConstructor(ExerciseBase):
    class Vehicle:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

    class Car(Vehicle):
        def __init__(self, brand, model, max_speed):
            super().__init__(brand, model)
            self.max_speed = max_speed

        def show(self):
            print(f"Brand: {self.brand}, Model: {self.model}, Max Speed: {self.max_speed} km/h")

    def run(self):
        c = self.Car("Toyota", "Corolla", 180)
        c.show()


# 4. Multiple Inheritance
class MultipleInheritance(ExerciseBase):
    class Flyer:
        def fly(self):
            print("Duck is flying")

    class Swimmer:
        def swim(self):
            print("Duck is swimming")

    class Duck(Flyer, Swimmer):
        pass

    def run(self):
        d = self.Duck()
        d.fly()
        d.swim()


# Menu to select exercise
def main():
    exercises = {
        "1": BasicInheritance(),
        "2": MethodOverriding(),
        "3": SuperConstructor(),
        "4": MultipleInheritance(),
    }

    print("Python Inheritance Solver Tool")
    print("1. Basic Inheritance")
    print("2. Method Overriding")
    print("3. Using super()")
    print("4. Multiple Inheritance")

    choice = input("Select Exercise (1-4): ").strip()
    if choice in exercises:
        exercises[choice].run()
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
