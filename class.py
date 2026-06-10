class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! You are now {self.age} years old." 
    def change_name(self, new_name):
        self.name = new_name
        return f"Your name has been changed to {self.name}."
# Example usage:
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person1.have_birthday())  # Output: Happy birthday! You are now 31 years old.
print(person1.change_name("Bob"))  # Output: Your name has been changed to Bob.