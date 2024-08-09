house = set()
for student in students:
    house.add(student[house])
    
for houses in sorted(house):
    print(houses)