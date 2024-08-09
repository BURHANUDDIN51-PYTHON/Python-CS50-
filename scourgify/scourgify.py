import sys
import csv 
def main():
    check_line_argument()
    output = []
    try:
        with open (sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                splity= row['name'].split(',')
                output.append({"first":splity[1].rstrip(),'last':splity[0].strip(),'house':row['house'].strip()})

    except FileNotFoundError:
        sys.exit(f'No such file name {sys.argv[1]}')

    with open(sys.argv[2], 'a') as files:
        writer = csv.DictWriter(files, fieldnames=['f', 'l', 'h'])
        writer.writerow({'f': "first" , 'l': "last", 'h': "house"})
        for row in output:
            writer.writerow({"f": row["first"].lstrip(), 'l': row['last'], 'h': row['house']})
   




def check_line_argument():
    if len(sys.argv) < 3:
        sys.exit(f'Too few command line argument')
    if len(sys.argv) > 3:
        sys.exit(f'Too many commad line argument')
    if sys.argv[1].endswith('.csv') == False: 
        sys.exit(f'Not a csv file')
    if sys.argv[2].endswith('.csv') == False: 
        sys.exit(f'Not a csv file')


   

if __name__ == "__main__":
    main()
