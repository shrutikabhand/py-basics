
# This program demonstrates polymorphism using different animal classes.
# Three classes Dog, Cat, and Cow are created, each having a speak() method.
# The speak() method produces a unique sound for every animal.
# Based on user input, the corresponding animal object is created.
# The program then calls the speak() method for each object in the given order.



class Dog:    
    def speak(self):
        print("Woof!")

class Cat:    
    def speak(self):
        print("Meow!")

class Cow:    
    def speak(self):
        print("Moo!")

N = int(input())
for _ in range(N):    
    animal = input()
    if animal == "Dog":
        obj = Dog()
    elif animal == "Cat":
        obj = Cat()
    elif animal == "Cow":
        obj = Cow()

    obj.speak()

