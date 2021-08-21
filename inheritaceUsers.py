import random
class User:
    def __init__(self,fName,lName,email,password,phoneNO,balance):
        self.fname = fName
        self.lname = lName
        self.email = email
        self.balance = balance
        self.password = password
        self.phoneNO = phoneNO
        self.confirmRandom = random.randint(100,1000)
        print('\nthis is your confirmation password: ', self.confirmRandom , '\n')
        self.confirm(input('enter your email here again to confirm: '),input('enter your password here again to confirm: '))
    def confirm(self,Email,Password):
        confirmPass = int(input('enter the password which we send to you: '))
        while self.email != Email and self.password != Password and confirmPass != self.confirmRandom:
            print('your email or password is incorrect. please rewrite them here: ')
            Email = input('your email: ')
            Password = input('your password: ')
            confirmPass = input('enter the password which we send to you: ')
    def pay(self):
        money = int(input('enter the number you want to add to your account: '))
        self.balance += money
        print(f'{money}$ added to your balance successfully!\n')
    def choices(self):
        menu()
        uchoice = int(input('enter the number of the choice you want to make: '))
        while int(uchoice) != 5 :
            if int(uchoice) > 5 or int(uchoice) < 1 :
                print('invalid choice!')
                menu()
                uchoice = int(input('enter the number of the choice you want to make: '))
                uchoice = int(input('enter the number of the choice you want to make: '))
            if int(uchoice) == 1 :
                print('ok here you can add a new user: ')
                u1 = User(input('enter your name here: '),input('enter your lastname here: '),input('enter your email here: '),input('enter your password here: '),input('enter your phone number here: '),int(input('enter the amount of money that you want to add to your balance here: ')))
                users.append(u1)
                print('new user added successfully!\n')
                menu()
                uchoice = int(input('enter the number of the choice you want to make: '))
            if int(uchoice) == 2 :
                self.pay()
                menu()
                uchoice = int(input('enter the number of the choice you want to make: '))
            if int(uchoice) == 3 :
                if int(input('if you are sure to buy enter 1 : ')) == 1 and self.balance >= 50:
                    self.balance -= 50
                    print('you bought what you want successfully!\n')
                    menu()
                    uchoice = int(input('enter the number of the choice you want to make: '))
                else :
                    print('either you didnt want to buy nor your balance is not enough!')
                    menu()
                    uchoice = int(input('enter the number of the choice you want to make: '))
            if int(uchoice) == 4 :
                opinions.append(input('we are really glad of you writing us your ideas. write your opinion here please:'))
                print('thak you for your opinion. *-*\n')
                menu()
                uchoice = int(input('enter the number of the choice you want to make: '))
        if uchoice == 5 :
            print('\nvisit us agian soon >-<')
            print(f'\nGoodbye {self.fname} {self.lname} ^-^\n')
def menu():
    print('\n\n1)add a new user\n2)add money to account balance\n3)buy\n4)write opinion\n5)exit\n\n')
u2 = User(input('enter your name here: '),input('enter your lastname here: '),input('enter your email here: '),input('enter your password here: '),input('enter your phone number here: '),int(input('enter the amount of money that you want to add to your balance here: ')))
users = []
users.append(u2)
opinions = []
u2.choices()