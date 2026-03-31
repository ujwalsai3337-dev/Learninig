def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        print("got it")
    return series

print(fibonacci(10))