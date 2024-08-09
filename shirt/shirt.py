import sys
from PIL import Image , ImageOps
from os.path import splitext
def main():
    check_command()
    editor()
    
    
    
    
    
def check_command():
    if len(sys.argv) < 3:
        sys.exit("Too few argument")
    if len(sys.argv) > 3:
        sys.exit("Too many argument")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if extension_check(file1[1]) == False:
        sys.exit("No such Extension")
    if extension_check(file2[1]) == False:
        sys.exit("No such extension for output")
    if file1[1] != file2[1]:
        sys.exit("Input and output have different extensions")
    
    
def extension_check(file):
    if file.lower() in[".jpg", ".jpeg", ".png"]:
        return True
    return False

def editor():
    try:
        mage = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        image1 = ImageOps.fit(mage, size)
        image1.paste(shirt , shirt)
        image1.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("no such file")
        
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()