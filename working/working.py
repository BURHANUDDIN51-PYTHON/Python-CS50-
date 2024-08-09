import re
import sys
def main():
    time = input('Hours: ').strip()
    print(convert(time))
    
    
    
def convert(time):
    if matches :=re.search(r"(.+) to (.+)", time, re.IGNORECASE):
        first = matches.group(1)
        second = matches.group(2)
        if PM_first := re.search(r"(.+):(.+) PM", first):
            if PM_second := re.search(r"(.+):(.+) PM", second):
                return f"{int(PM_first.group(1))+12}:{PM_first.group(2)} To {int(PM_second.group(1))+12}:{PM_second.group(2)}"
            if PM_second := re.search(r"(.+):(.+) AM", second):
                return f"{int(PM_first.group(1))+12}:{PM_first.group(2)} To {PM_second.group(1)}:{PM_second.group(2)}"
        if AM_first := re.search(r"(.+):(.+) AM", first):
            if AM_second := re.search(r"(.+):(.+) AM", second):
                return f"{AM_first.group(1)}:{AM_first.group(2)} To {AM_second.group(1)}:{AM_second.group(2)}"
            if AM_second := re.search(r"(.+):(.+) PM", second):
                return f"{AM_first.group(1)}:{AM_first.group(2)} To {int(AM_second.group(1))+12}:{AM_second.group(2)}"
            
           
        

if __name__ == "__main__":
    main()