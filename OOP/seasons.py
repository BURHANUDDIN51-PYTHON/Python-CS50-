from datetime import date
import sys
import re
import inflect
p = inflect.engine()
def main():
    year, month, day = ask_date()
    today_date = date.today()
    birth_date = date(int(year), int(month), int(day))
    time_lived = today_date - birth_date
    minutes = time_lived.days * 24 * 60
    minutes_in_words = p.number_to_words(minutes, andword="")
    print(f"{minutes_in_words.upper()},","\nTotal number of minutes you lived till now.")
    
def ask_date():
    date = input("Date of birth: ")
    if matches := re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", date):
        year = matches.group(1)
        month = matches.group(2)
        day = matches.group(3)
        return year, month, day
    else:
        sys.exit(f"write in the correct Format")
    
        
if __name__ == "__main__":
    main()