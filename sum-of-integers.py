def calculate(min, max):
    sum = 0
    n = min
    while n <= max:
        sum = sum + n
        n = n + 1
    print(sum)

calculate(1, 3)
calculate(4, 8)
