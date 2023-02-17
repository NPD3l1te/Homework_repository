d = []

with open('data.txtex1') as f:
    file_data = f.read().split()
    for i in file_data:
        try:
            d.append(int(i))
        except:
            pass
print(d)
