def calculate_task3(x, n):
    total = 0
    for i in range(1, n+1):
        total += (-1)**i / 5**2
    return total