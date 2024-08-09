import re
import sys
def main():
    txt = input("INput: ")
    print(count(txt))


def count(um):
    matches = re.findall(r"\bum\b", um, re.IGNORECASE)
    return len(matches)
    
if __name__ == "__main__":
    main()
    