import re 
email = input('Email: ')
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')