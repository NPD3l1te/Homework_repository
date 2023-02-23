N = int(input("Введите число N: "))

numbers = []
for i in range(N):
    number = input(f"Введите число {i + 1}: ")
    numbers.append(number)

# запись чисел в файл numbers.txt через пробел
with open("numbers.txt", "w") as file:
    file.write(" ".join(numbers))
