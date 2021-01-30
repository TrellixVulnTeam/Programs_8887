import sqlite3
import argparse

connectionObject = sqlite3.connect('ContactBookDatabase.db')
cursorObject = connectionObject.cursor()


class ContactBook:
    print('''
        Используйте название = ContactBook() для создания книги.
        Используйте название.instructions для просмора комманд.''')

    def myinstructions(self):
        print('''

        Используйте название.seeAllbook() для просмотра всех контактов.

        Используйте название.addnewContact('имя','адрес','номер телефона','эл. почта') для добавления контакта.
        Внимание! Все значения, указанные в скобках, должны быть в кавычках!

        Используйте название.redactbook(порядковый номер контакта,порядковый номер данных,'новые данные')
        для редактироания ваших контактов.

        Используйте название.deletecon(Порядковый номер контакта), чтобы удалить контакт.

        Используйте название.clearbook(), чтобы полностью очистить книгу.

        Используйте название.sortbook(), чтобы отсортировать контакты в порядке ASCII.
        ''')

    def __init__(self):
        self.book = []
        print('Контактная книга успешно создана.')
        cursorObject.execute("create table if not exists contacts(name, address, phonenumber, mail)")
        connectionObject.commit()

    def addnewContact(self, name, address, phonenumber, mail):
        data = (name, address, phonenumber, mail)
        self.book.append([name, address, phonenumber, mail])
        print('''
     Ваш контакт был сохранен под номером''', len(self.book))
        cursorObject.execute("INSERT INTO contacts(name, address, phonenumber, mail) VALUES (?,?,?,?)", data)
        connectionObject.commit()

    def seeAllbook(self):
        # Проверка на наличие контактов
        if self.book == []:
            # Если контактов нет, соответствующий вывод
            print('Контакты не обнаружены')
        else:
            # Если все нормально, то вывод контактов с помощью вложенного цикла
            for i in range(len(self.book)):
                print(i + 1, end='. ')
                for j in range(len(self.book[i])):
                    print(self.book[i][j])

    def redactbook(self, contactNumber, propertyNumber, NewProperty):
        # Замена элемента в списке, исходя из введенных данных
        try:
            if propertyNumber == 1:
                name = self.book[contactNumber - 1][propertyNumber - 1]
                newName = NewProperty
                cursorObject.execute("UPDATE contacts SET name=? WHERE name=?", [name, newName])
            elif propertyNumber == 2:
                address = self.book[contactNumber - 1][propertyNumber - 1]
                newAdress = NewProperty
                cursorObject.execute("UPDATE contacts SET address=? WHERE address=?", [address, newAdress])
            elif propertyNumber == 3:
                phonenumber = self.book[contactNumber - 1][propertyNumber - 1]
                newPhonenumber = NewProperty
                cursorObject.execute("UPDATE contacts SET phonenumber=? WHERE phonenumber=?",
                                     [phonenumber, newPhonenumber])
            elif propertyNumber == 4:
                mail = self.book[contactNumber - 1][propertyNumber - 1]
                newMail = NewProperty
                cursorObject.execute("UPDATE contacts SET mail=? WHERE mail=?", [mail, newMail])
            self.book[contactNumber - 1][propertyNumber - 1] = NewProperty
            connectionObject.commit()
            print('Данные были успешно изменены.')
        except IndexError:
            print('Такого контакта или строки в нем не существует')

    def deletecon(self, contactNumber):
        # Небольшая проверка на случай ошибочного ввода
        UserInput = int(input('Введите 1 для подтверждения или что угодно для отклонения.'))
        if UserInput == 1:
            name = self.book[contactNumber - 1][0]
            address = self.book[contactNumber - 1][1]
            phonenumber = self.book[contactNumber - 1][2]
            mail = self.book[contactNumber - 1][3]
            cursorObject.execute("DELETE FROM contacts WHERE name=?", [name])
            cursorObject.execute("DELETE FROM contacts WHERE address=?", [address])
            cursorObject.execute("DELETE FROM contacts WHERE phonenumber=?", [phonenumber])
            cursorObject.execute("DELETE FROM contacts WHERE mail=?", [mail])
            # Удаление через del
            del self.book[contactNumber - 1]
            connectionObject.commit()
            print('Контакт удален')
        else:
            print('Удаление отклонено, контакт не удален')

    def clearbook(self):
        # Еще одна проверка
        UserInput = int(input('Введите 1 для подтверждения или что угодно для отклонения.'))
        if UserInput == 1:
            # Поочередное удаление контактов через цикл
            for i in range(len(self.book)):
                del self.book[-1]
            cursorObject.execute('DROP table contacts')
            cursorObject.execute("create table if not exists contacts(name, address, phonenumber, mail)")
            connectionObject.commit()
            print('Книга удалена')
        else:
            print('Удаление отклонено, книга не удалена')

    def sortbook(self):
        # Проверка на наличие контактов
        if self.book == []:
            # Если контактов нет, соответствующий вывод
            print('Контакты не обнаружены')
        else:
            # Обычная сортировка пузырьком
            data = ()
            for i in range(len(self.book)):
                for j in range(len(self.book) - 1):
                    if self.book[j][0] > self.book[j + 1][0]:
                        buf = self.book[j + 1]
                        self.book[j + 1] = self.book[j]
                        self.book[j] = buf
            print('Проведена сортировка в порядке ASCII.')