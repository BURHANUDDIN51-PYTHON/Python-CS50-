from datetime import date
import re
import sys
import inflect

p = inflect.engine()
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
        
    def __sub__(self, other):
        year = other.year - self.year
        month = other.month - self.month
        day = other.day - self.day
        return Date(year, month, day)

    
   
        
        
def main():
    birth_date = input("Birth of Date: ")
    try:
        year, month, day = date_check(birth_date)
    except:
        sys.exit(f"Invalid date")
    date_of_birth = date(int(year), int(month), int(day))   
    present_date = date.today()
    diff = present_date - date_of_birth
    ouptut = diff.days * 24 * 60
    word =  p.number_to_words((ouptut),andword="")
    print(word.capitalize(), "minutes")
    
    
    
def date_check(date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",date):
        year, month, day = date.split("-")
        return year, month, day
    
        
if __name__ == "__main__":
    main()
