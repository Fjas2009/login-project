user1 = ['bilal' , '1234']
user2:list[str] = ['hasan' , 'bilal']

user1_tasks = ['1.wake up' , '2.eat breakfast' , '3.go to school']
user2_tasks = ['1.wake up' , '2.eat break fast']
def login_of_users():

    x1=input("Enter your user name: ")
    print(f'hi {x1}')
    x2=input("Enter your password: ")
    if x1 == user1[0] and x2 == user1[1]:
        print(f'user 1 is logged in')
        see_tasks1 = input('Do u want to see your tasks Y/N: ')
        print(see_tasks1)
        if see_tasks1 == 'n' :
            print('ok')
        if see_tasks1 == 'y':
            print(*user1_tasks)
    if x1 in user2[0] and x2 in user2[1]:
        print('the user 2 is logged in')
        see_tasks2 = input('Do u want to see your tasks Y/N: ')
        if see_tasks2 != 'n' and not 'no' :
            pass
            print('ok')
        if see_tasks2 == 'y'or 'yes':
            print(*user2_tasks)
        if x1 or x2 is None:
            print("invalid user name or password")
    add_tasks = input("what task do u want to add ")

login_of_users()

