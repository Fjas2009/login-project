user1 = ['bilal' , '1234']
user2 = ['hasan' , 'bilal']

user1_tasks = ['1.wake up' , '2.eat breakfast' , '3.go to school']
user2_tasks = ['1.wake up' , '2.eat break fast']


def login_of_users() :
    print("\033[1;34;40m Bright Blue \033[0m 1;34;40m \033[0;34;47m Blue ")
    x1 = input("Enter your user name: ")
    print(f'hi {x1}')
    x2 = input("Enter your password: ")
    if x1 == user1[ 0 ] and x2 == user1[ 1 ] :
        print(f'user 1 is logged in')
        see_tasks1 = input('Do u want to see your tasks Y/N: ')
        if see_tasks1 == 'n' or 'no' :
            print('ok')
        if see_tasks1 == 'yes' or 'y' :
            print(*user1_tasks)
    elif x1 == user2[ 0 ] and x2 == user2[ 1 ] :
        print('the user 2 is logged in')
        see_tasks2 = input('Do u want to see your tasks Y/N: ')
        if see_tasks2 != 'n' and not 'no' :
            print('ok')
        if see_tasks2 == 'y' or 'yes' :
            print(*user2_tasks)
    elif x1 or x2 == "" :
        print("invalid user name or password")
    else:
        print('Error')

    login_of_users()

match input("Do you want to sign up or login: "):
    case 'sign in':
        login_of_users()
    case 'login':
        login_of_users()
    case 'sign up':
        print('coming soon')
    case "":
        print('type something')
    case _:
        print("invalid input")
