import sys
import re
def main():
    ip = input('IPv4 Address: ').strip()
    print(validate(ip))
    
        
    
#validation of ipaddress
def validate(ip):
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip, re.IGNORECASE):
        d1 = int(matches.group(1))
        d2 = int(matches.group(2))
        d3 = int(matches.group(3))
        d4 = int(matches.group(4))
        if d1 <= 255 and d2 <= 255 and d3 <= 255 and d4 <= 255:
            return True
        else:
            return False    
    else:
        return False
       
      
    

if __name__ == "__main__":
    main()