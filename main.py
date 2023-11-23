from classLibrary import Manager,Smena,User,Pay,Coffe,Additional

def OpenSmena(manager:Manager.Manager):
    return Smena.Smena(manager)
def LoginManager(login,password):
    valLogin = '123'
    valPassword = '123'
    name = 'Алексей'
    phone = '8999123451'
    bonus = 100
    if valLogin == login and valPassword == password:
        manager = Manager.Manager(login,password,name,phone,bonus)
        return manager
    else:
        return None
_mainMenu:str
_buyMenu:str
_smenaMenu:str

while True:
    password = input('ведите пароль от кассы: ')
    if password == 'qwerty':
        login = input('Введите логин: ')
        passwordManager = input('Введите пароль: ')
        manager = LoginManager(login, passwordManager)
        if manager is None:
            break
        _mainMenu = f'{manager.getName()}\n 1 - открыть смену'
        choice = input(_mainMenu)
        if choice == '1':
            smena = OpenSmena(manager)
            _mainMenu = f'{manager.getName()}\n 2 - закрыть смену\n 2 - покупка'
            choice = input(_mainMenu)
            if choice == '2':
                while True:
                    _buyMenu = f'1 - Латте {' '*12} 4 - Oreo\n 2 - Капучино {' '*12} 5 - Пончик\n {' '*12} 3 - Американо {' '*12}'
                    choice = input(_buyMenu)
                    addtionals = []
                    coffees = []
                    if choice in ['1','2', '3']:
                        pass
                    elif choice in ['4', '5']:
                        if choice == '4':
                            count = int(input('Количество'))
                            for i in range(count):
                                addtionals.append(Additional.Additional('Oreo',  'N/A', 150))
                        elif choice == '5':
                            count = int(input('Количество'))
                            for i in range(count):
                                addtionals.append(Additional.Additional('Пончик', 'N/A', 100))

                    else:
                        continue
                    pay = Pay.Pay(eMoney=True,
                                  clien=User.User(bonus=100, name='Андрей', phone=''),
                                  additionals=addtionals,
                                  coffes=coffees)

        break
    else:
        continue