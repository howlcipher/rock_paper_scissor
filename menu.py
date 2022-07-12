



from soupsieve import select


def menu_display():
    response = input('------\n-Menu-\n------\n\
        \n1. New User\
        \n2. Existing User\
        \nInput Choice: ')
    while response != 1 and response != 2:
        try:
            response = int(response)
        except:
            print('\n-----\nInvalid Choice, try again\n-----\n')
            continue
        if response == 1:
            new_user = input('Enter Username: ')
            print('New user', new_user, 'has been created')
            return new_user
        elif response == 2:
            existing_user = list_of_users()
            print(existing_user, 'has been chosen')
            return existing_user


def list_of_users():
    list_of_users = {1: 'test user 1', 2: 'test user 2', 3: 'test user 3'}

    for i in range((len(list_of_users))):
        print(list_of_users[i+1])

    select_user = ''
    
    while select_user not in list_of_users:
        select_user = input('Select a user: ')
        try:
            select_user = int(select_user)
        except:
            print('\n-----\nInvalid Choice, try again\n-----\n')
            continue
    return list_of_users[select_user ]

menu_display()