import datetime
# from datetime import date

def librarian_menu():
    print("Press 1- Sign in \nPress 2- Register \nPress 3- Quit")
    while True:
        try:
            choice=int(input("Enter option:"))
            if choice<=3:
                break
            else:
                raise ValueError:
            except ValueError:
                print('Entry invalid,please try again')
            return choice

    def librarian_sign_in():
        email=input("Enter mail id: ")
        password=input("Enter password: ")
        return email,password

    def librarian_register_view():
        name=input('Enter name: ')
        email=input('Enter email: ')
        password=input('Enter password: ')
        phone=int(input('Enter phone number:'))
        return name,email,password,phone

    def list_librarian_function():
        menu='''Select \n1-Insert books\n2- List books \n3- update book title \n4- update book company\n5 delete books'''
        choice=int(input(menu))
        return choice

    def capture_book_details_to_insert():
        title=input('Enter book name:')
        author=input('Enter author name:')
        company=input('Enter company name:')
        date=datetime.date.today()
        rented_user=input('Enter rented user:')
        return [title,author,company,date,rented_user]



