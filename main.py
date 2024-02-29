def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')

    while (choice!=8):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            find_by_lastname(phone_book,last_name)
        elif choice==3:
            number=input('number ')
            find_by_number(phone_book,number)
        elif choice==4:
            last_name=input('lastname ')
            new_number=input('new  number ')
            change_number(phone_book,last_name,new_number)
        elif choice==5:
            lastname=input('lastname ')
            firstname=input('firstname ')
            number=input('number ')
            description=input('description ')
            add_contact(phone_book,lastname,firstname,number,description)
        elif choice==6:
            lastname=input('lastname ')
            delete_by_lastname(phone_book,lastname)
        elif choice==7:
            write_txt('phonebook.txt',phone_book)
        choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить номер абонента\n"
          "5. Добавить абонента в справочник\n"
          "6. Удалить по фамилии\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')

def print_result(book):
    for i in range(len(book)):
        for j in book[i]:
            print('{}: {}'.format(j, book[i][j]))

def find_by_lastname(book, surname):
    for i in range(len(book)):
        if surname in book[i]['Фамилия']:
            for j in book[i]:
                print('{}: {}'.format(j, book[i][j]))

def find_by_number(book, num):
    for i in range(len(book)):
        if num in book[i]['Телефон']:
            for j in book[i]:
                print('{}: {}'.format(j, book[i][j]))

def change_number(book, surname, new_num):
    for i in range(len(book)):
        if book[i]['Фамилия'] == surname:
            book[i]['Телефон'] = new_num
            for j in book[i]:
                print('{}: {}'.format(j, book[i][j]))

def add_contact(book, surname, name, num, info):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    line = (f'{surname}, {name}, {num}, {info}')
    record = dict(zip(fields, line.split(',')))
    book.append(record)

def delete_by_lastname(book, surname):
    for i in range(len(book)):
        if surname in book[i]['Фамилия']:
            j = i
    book.pop(j)

work_with_phonebook()