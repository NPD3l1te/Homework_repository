def change(list):
    list = ['fgdg', 3, 5, 'jifjfhf', 7, 'gg']
    print(list)
    list[0], list[-1] = list[-1], list[0]
    print(list)


change(list)
