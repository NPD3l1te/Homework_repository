with open('data.txtex6', 'r') as f:
    numbers = f.read().split()
    numbers = list(map(int, numbers))
    summ = sum(numbers)

print(f'Сумма >>>> {summ}')