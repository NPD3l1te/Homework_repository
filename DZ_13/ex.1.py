def change(arr):
    arr = list(map(int, input('Enter whole numbers separated by spaces').split()))
    print(arr)
    k = -1

    for i in range(len(arr) // 2):
        print('\nbefore ', i, arr)
        arr[k], arr[i] = arr[i], arr[k]
        print('after ', arr)
        k -= 1


print(change(arr=list))
