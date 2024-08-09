import sys
def main():
    Check_lines_argument()
    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
            len = 0
            for line in lines:
                if line.isspace() or line.startswith('#'):
                    pass
                else:
                    len += 1
            print(len)
    except FileNotFoundError:
        sys.exit('No such file')
    
    
    
        
def Check_lines_argument():
        if len(sys.argv) < 2:
            sys.exit(f'Two few Command line argument')
        if len(sys.argv) > 2:
            sys.exit(f'Too Many command line argument')
        if sys.argv[1][-3] != '.' and sys.argv[1][-2] != 'p' and sys.argv[1][-1] != 'y':
            sys.exit(f'Not a python a file')




if __name__ == "__main__":
    main()       