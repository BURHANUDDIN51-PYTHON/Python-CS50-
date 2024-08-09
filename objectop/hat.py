import random
from student import Student
class Hat:
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    
    @classmethod
    def sort(cls, houses):
        print(f"{houses} is from the house {random.choice(cls.houses)}")

s = Student.get()
print(s)

        
