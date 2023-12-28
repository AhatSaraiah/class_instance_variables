class Shark:
    # Class variables
    animal_type = "fish"
    location = "ocean"

 # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def main():
    # First object, set up instance variables of constructor method
    sammy = Shark("Sammy", 5)

    # Print out instance variable name
    print(sammy.name)

    # Print out class variable location
    print(sammy.location)

    # Second object
    stevie = Shark("Stevie", 8)
# Print out instance variable name
    print(stevie.name)

    # Print out class variable animal_type
    print(stevie.animal_type)

if __name__ == "__main__":
    main()


