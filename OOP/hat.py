import random
class Hat:
    house = ["GRYFFINDOR", "HUFFLEPUFF", "RAVENCLAW", "SLYTHERIN"]
    
    
    @classmethod
    def sort(cls, name):
        return f"{name} is from the house {random.choice(cls.house)}"
    
    
print(Hat.sort(input("Name: ")))