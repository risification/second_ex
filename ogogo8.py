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

'''def pocupatel(his_money, eat):
    eat_1 = int(catalogue[eat])
    his_money1 = int(his_money)
    c = his_money1 - eat_1
    print(c)


his_money1 = str(input('введите сколько у вас деняг: '))
eat1 = input("введите что вы хотите купить: ")
pocupatel(his_money1, eat1)
'''


def count_eat(change: int):
    count = int(input("сколько еды вы хотите купить: "))
    while count < change:
        his_money1 = input('сколько у вас деняг: ')
        change_food = input('веберите какую еды вы хотите купить: ')
        change_food1 = int(change_food)
        his_money = int(his_money1)
        again = input('вы хотите еще что то купить?: ')
        if again == "да":
            count += 1
count_eat(3)