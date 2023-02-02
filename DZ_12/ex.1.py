permission = {}
n = int(input())
for i in range(n):
    a = input().split()
    permission[a[0]] = set(a[1:])
for i in range(int(input())):
    perm, file = input().split()
    if perm == 'read':
        perm = 'R'
    if perm == 'write':
        perm = 'W'
    if perm == 'execute':
        perm = 'X'
    if perm in permission[file]:
        print('OK')
    else:
        print('Access denied')


"""
В примере использовались эти данные:

3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt
"""
