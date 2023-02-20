import pickle

my_list = [
    {'name': 'Jonh', 'phone_number': '+38056666565654'},
    {'name': 'Andrew', 'phone_number': '+380777777777'},
    {'name': 'Mark', 'phone_number': '+3803333333333'}
]

with open('my_list.pkl', 'wb') as f:
    pickle.dump(my_list, f)


f.close()
