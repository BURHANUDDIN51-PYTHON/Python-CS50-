from validator_collection import validators, checkers, errors
import re
import sys
def main():
    email = input("Email: ").strip()
    print(is_email(email))
    

def is_email(email):
    try:
        if email_address := validators.email(email):
            if checkers.is_email(email_address):
                return f'Valid'  
    except:
        sys.exit(f'Invalid')
        
        

     
if __name__ == "__main__":
    main()     

    