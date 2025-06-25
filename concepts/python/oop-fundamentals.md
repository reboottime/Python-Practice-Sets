# OOP

对象，属性（状态和行为），关系, 动态-》抽象出类

## Declare a class


Guide note comes from [Python Fundamental For FastApi](https://claude.ai/chat/d23d6cca-f2ca-4b1f-b72e-4511df7e0515)

Class is an abstraction of an object.

```python
class Dog:
    species = 'Canis familaris' # similar to static property in class
    # constructor
    def __init__(self, name, breed, age):
        self.name = name      # Instance attribute
        self.breed = breed    # Instance attribute
        self.age = age        # Instance attribute
        # _ annotate private property (include methods and )
        self._secret = 'I do not want to tell you my secret, buddy'
    
    # self points to current object reference, it is similar to this in javascript 
    # but you have to explicitly declare it
    de bark(self):
        return f"{self.name} says wang wang wang"


# Create objects with data
buddy = Dog("Buddy", "Golden Retriever", 3)
max_dog = Dog("Max", "Bulldog", 5)

print(buddy.name)    # "Buddy"
print(max_dog.breed) # "Bulldog"
```

## Inheritance

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Canis familiaris")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Felis catus")
        self.color = color
    
    def make_sound(self):
        return f"{self.name} meows: Meow!"

# there is no new to initiate an instance
buddy = Dog("Buddy", "Golden Retriever")
whiskers = Cat("Whiskers", "Orange")

print(buddy.make_sound())    # "Buddy barks: Woof!"
print(whiskers.make_sound()) # "Whiskers meows: Meow!"

```
