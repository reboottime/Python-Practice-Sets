# OOP

## reusable models

- 对象，属性（状态和行为），关系, 动态-》抽象出类
- context: boundary & limitation

## OOP in Python

### Declare a class

Guide note comes from [Python Fundamental For FastApi](https://claude.ai/chat/d23d6cca-f2ca-4b1f-b72e-4511df7e0515)

Class is an abstraction of an object.

```python
class Dog:
    species = 'Canis familaris' # similar to static property on Class in TypeScript
    # constructor
    def __init__(self, name, breed, age):
        self.name = name      # Instance attribute
        self.breed = breed    # Instance attribute
        self.age = age        # Instance attribute
        # _ annotate private property(include state and methods)
        self._secret = 'I do not want to tell you my secret, buddy'
    
    # self points to current object reference, it is similar to this in javascript 
    # but you have to explicitly declare it
    de bark(self):
        return f"{self.name} says wang wang wang"


# Create objects with data, there is no keyword `new`
buddy = Dog("Buddy", "Golden Retriever", 3)
max_dog = Dog("Max", "Bulldog", 5)

print(buddy.name)    # "Buddy"
print(max_dog.breed) # "Bulldog"
```

### Inheritance

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        # keyword: super
        super().__init__(name, "Canis familiaris")  # Call parent constructor
        self.breed = breed
    
    # override parent behavior
    def make_sound(self):  # Override parent method
        # f creates f-string ( formatted string literal)in Python. Which allows you to embed expression directly inside of the string
        # similar to javascripr template string in es6
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

### Polymorphism

To consolidate understanding of solid principle, please refer to [solid principle](./solid-principle.md)

## Recap on keywords

- `self`
- `__init__`
- `_` mark a property (state & method) as private
- `f""` template string