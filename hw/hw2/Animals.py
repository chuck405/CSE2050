class Animal:
    def __init__(self, name):
        """
        Initializer method for the Animal class
        """
        # Defines instance variable for name
        self.name = name

    def reply(self):
        """
        Method for reply()
        """
        # Returns the animal's relevant speak
        return self.speak()

class Mammal(Animal):
    def __init__(self, name):
        """
        Initalizer method for the Mammal class
        """
        # Calls the initializer of the Animal superclass
        super().__init__(name)

    def speak(self):
        """
        Method for speak()
        """
        # returns a string giving the name and an appropriate sound
        return str(self.name) + " says [Mammal Noise]!"

class Cat(Mammal):
    def __init__(self, name):
        """
        Initializer method for the Cat class
        """
        # Calls the initializer of the Mammal superclass
        super().__init__(name)

    def speak(self):
        """
        Method for speak()
        """
        # returns a string giving the name and an appropriate sound
        return str(self.name) + " says Meow!"

class Dog(Mammal):
    def __init__(self, name):
        """
        Initializer method for the Dog class
        """
        # Calls the initializer of the Mammal superclass
        super().__init__(name)

    def speak(self):
        """
        Method for speak()
        """
        # returns a string giving the name and an appropriate sound
        return str(self.name) + " says Woof!"

class Primate(Mammal):
    def __init__(self, name):
        """
        Initializer method for the Primate class
        """
        # Calls the initializer of the Mammal superclass
        super().__init__(name)

    def speak(self):
        """
        Method for speak()
        """
        # returns a string giving the name and an appropriate sound
        return str(self.name) + " says [Primate Noise]!"

class ComputerScientist(Primate):
    def __init__(self, name):
        """
        Initializer method for the ComputerScientist class
        """
        # Calls the initializer of the Primate superclass
        super().__init__(name)