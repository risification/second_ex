catalogue = {'hot-dot': 50, 'hamburger': 120, 'shaurma': 150, 'naggets': 130, 'pizza': 930,
             'boso-lagman': 250, 'plov': 190, 'giro-lagman': 240, 'mantes': 160, 'rolls': 600,
             'garnir': 100, 'grechka': 70, 'pelmeni': 130, 'french meat': 400, 'fish': 500,
             't-bone': 870, 'Beijing duck': 5000, 'shashlyk assorti': 50000
             }

def auth(tries: int):
    count = 0
    while count < tries:
        name = input('введите имя: ')
        password = input('введите пароль: ')
        name = name.strip()
        password = password.strip()
        if 15 > len(name):
            if not name.isalpha():
                if not name.isdigit():
                    if 8 <= len(password) <= 16:
                        if not password.isdigit():
                            if not password.isalpha():
                                print(name, password)
                                break
                            else:
                                print('пароль состои только из букв')
                        else:
                            print('пароль состоит только из цифр')
                    else:
                        print('у пароля не правильная длина')
                else:
                    print('имя состоит только из цифр')
            else:
                print('имя состоит только из букв')
        else:
            print('у имени не правильная длина')
        count += 1

auth(2)



def pocupatel(money, price):
    if money < price:
        return 'no money'
    else:
        result = money - price
        return result


def choice(num_of_food):
    list1 = []
    for i in range(num_of_food):
        new_element = input()
        if new_element in catalogue:
            list1.append(new_element)
    return list1


def order():
    money = 1000
    list1 = choice(3)
    for food in list1:
        price = catalogue[food]
        if money >= price:
            money = pocupatel(money, price)
    print(money)


order()
