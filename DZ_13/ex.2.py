def to_dict(lst):
    return {element: element for element in lst}


print(to_dict([1, 2, 3, 4]))
print(to_dict(['name', 'age', 'phone_number', 47]))

"""
Для решения использовал dict comprehension
"""