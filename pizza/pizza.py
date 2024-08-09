import csv
import sys
from tabulate import tabulate
def main():
    line_argument()
    pizza = []
    # Table making
    try:
        with open(sys.argv[1], 'r') as file:
            read = csv.DictReader(file)
            for r in read:
                pizza.append(r)
        print(tabulate(pizza, headers="keys", tablefmt="grid"))
                                       
    except FileNotFoundError:
        sys.exit('No such file')

   
#ask for command line argument
def line_argument():
    if len(sys.argv) < 2:
        sys.exit(f'Too few arguments')
    if len(sys.argv) > 2:
        sys.exit(f'Too many line argument')
    if sys.argv[1].endswith('.csv') == False:
        sys.exit(f'Not a csv file')

if __name__ == "__main__":
    main()