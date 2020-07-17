from Documentation import documents, directories


def user_number_doc():
    global number
    number = input('Введите номер документа ')
    return number

def username_by_doc(document):
    username = 0
    for person in documents:
        if number == person['number']:
            username = (person['name'])
            break
        elif number not in person['number']:
            username = ('Проверьте наличие пробела между серией и номером паспорта, если пробел есть, тогда такого человека нет в списке')
    print(f' Человек, которому принадлежит документ: {username}')

def shelf_number_by_doc(directory):
    new_shelf_number = 0
    for key, velue in directories.items():
        if number in velue:
            new_shelf_number = key
            break
        elif number not in velue:
            new_shelf_number = ('Проверьте наличие пробела между серией и номером паспорта, если пробел есть, тогда такого документа нет на полках')
    print(f' Номер полки, на которой хранится документ {new_shelf_number}')
    return new_shelf_number

def add_new_user(document, directory):
    new_type = input('Введите тип документа латинскими буквами ')
    new_name = input('Введите имя и фамилию ')
    shelf_number = input('Укажите номер полки ')
    dict_doc = []
    for document in documents:
        dict_doc = [{'type': new_type, 'number': number, 'name': new_name}]
    print(f'Список с добавленным документом {documents + dict_doc}')
    while True:
        if shelf_number not in directories.keys():
            print('Такой полки не существует')
        break
# К заданию на исключения, просто очень не нравится, что код падает на несуществующей полке
    try:
        directories[shelf_number].append(number)
        print(f'Вы добавили документ нового пользователя на полку: {directories}')
    except KeyError:
        print(f'Сначала добавьте эту полку, исключение KeyError')
# К заданию на исключения, просто очень не нравится, что код падает на несуществующей полке

def list_all_doc(document):
    for document in documents:
        print(document['type'], document['number'], document['name'])

def add_new_shelf(directory):
    new_shelf_number = input('Укажите номер полки, которую добавляете ')
    while True:
        if new_shelf_number in directories.keys():
            print('Такая полка уже есть')
        break
    directories.setdefault((new_shelf_number), [])
    print(f'Список всех полок: {directories}')

def del_user_list(document):
    for person in documents:
        if number != person['number']:
            continue
        elif number == person['number']:
            documents[:] = [person for person in documents if person.get('number') != number]
        print(f'Список с удаленным документом {documents}')
        return (documents)
    print('Вы пытаетесь удалить документ, которого нет в списке')

# К заданию на исключения, тут оно правда актуально
def del_user_shelf(directory):
    try:
        shelf = shelf_number_by_doc(directories)
        directories[shelf[0]].remove(number)
        print(f'Список всех полок без удаленного документа: {directories}')
    except KeyError:
        print(f'Сначала добавьте такой документ на полки, исключение KeyError')
# К заданию на исключения, тут оно правда актуально

# К заданию на исключения, но не поняла, зачем тут ловить KeyError
def list_all_names(document):
    list = []
    for document in documents:
        list.append(document['name'])
        print(document['name'])
    return list


def user_service():
    while True:
        user_input = input('Введите команду ')
        if user_input == 'p':
            user_number_doc()
            username_by_doc(documents)
            print('\n')
        elif user_input == 's':
            user_number_doc()
            shelf_number_by_doc(directories)
            print('\n')
        elif user_input == 'l':
            list_all_doc(documents)
            print('\n')
        elif user_input == 'a':
            user_number_doc()
            add_new_user(documents, directories)# дополнила отловом KeyError к заданию на исключения
            print('\n')
        elif user_input == 'as':
            add_new_shelf(directories)
            print('\n')
        elif user_input == 'd':
            user_number_doc()
            del_user_list(documents)
            del_user_shelf(directories)# дополнила отловом KeyError к заданию на исключения
            print('\n')
        elif user_input == 'ln':# К заданию на исключения, но не поняла, где тут ловить KeyError
            list_all_names(documents)
            print('\n')
        elif user_input == 'q':
            break
if __name__ == '__main__':
    user_service()