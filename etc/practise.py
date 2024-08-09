#swapping without any third variable

def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return (a, b)
    
print(swap(10, 20))