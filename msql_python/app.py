from db_operation import create_table,create_user,get_user,update_user,delete_user 
def menu():
    print('=== User Management System===')
    print('1.Create User')
    print('2.View Users')
    print('3.Update Users')
    print('4.Delete User')
    print('5.Exit')

create_table()

while True:
    menu()
    choice=input("enter your choice:")
    match choice:
        case '1':
            name=input('enter name:')
            email=input('enter email:')
            create_user(name,email)

        case'2':
            print('user list:')
            get_user()

        case '3':
            user_id=int(input('Enter user Id to update:'))
            new_name=input("enter new name:")
            new_email=input("enter new email:")
            update_user(user_id,new_name,new_email)

        case '4':
            user_id=int(input('enter user ID to delete:'))
            delete_user(user_id)

        case '5':
            print('project terminated')
            break
        case _:
            print("invaid choice.please try again.")