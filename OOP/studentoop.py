class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    #getter
    @property
    def house(self):
        return self._house
    
    #setter
    @house.setter
    def house(self, house):
        if house not in ["gryffindor","Hufflepuff", "slytherin", "ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house 
        
    #getter 
    @property
    def name(self):
        return self._name
    
    #setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Value")
        self._name = name
        
        

def main():
    student = get_student()
    print(student)
    
    
    
    
def get_student():
    name = input("Name: ")
    house = input("House: ") 
    return Student(name, house)
if __name__ == "__main__":
    main()