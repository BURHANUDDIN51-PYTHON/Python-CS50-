import re
import sys
def main():
    url = input("HTML: ")
    print(parse(url))
    
    
    
def parse(url):
    if matches := re.search(r"(https?)://(?:www\.)?youtube\.com/embed/(.{11})", url, re.IGNORECASE):
       return f"{matches.group(1)}://youtu.be/{matches.group(2)}"
            
    
if __name__ == "__main__":
    main()