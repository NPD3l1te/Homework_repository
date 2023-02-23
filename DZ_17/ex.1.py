class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone,
            'address': self.address
        }

    def call(self, phone_number):
        print(f'{self.phone} вызывает абонента {phone_number}')


piople1 = Human('Jonh', 'Williams', 23, +380999999999, 'city. Odessa, street. Govorova')
piople2 = Human('Steave', 'Grant', 30, +380777777777, 'city. Kiev, street. Khreshchatyk')
piople3 = Human('Tony', 'Stark', 57, +380333333333, 'city. New York, streetю Wall Street')

print(piople1.get_info())
print(piople2.get_info())
print(piople3.get_info())

