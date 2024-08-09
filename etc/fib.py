def fibonacci(n):
    a = [0, 1]
    for i in range(2, n, 1):
        next_number = a[i - 1] + a[i - 2]
        a.append(next_number)
    return a


number = int(input("Number: "))
lst = fibonacci(number)

print(*lst)

#CSV file ke andar jo data hota hai vo string ki form mei save hota hai