class ContactBook:
    print('''
        Используйте название = ContactBook() для создания книги.
        Используйте название.comands для просмора комманд.''')

    def comands(self):

        print('''

        Используйте название.seeAllcontacts() для просмотра всех контактов.

        Используйте название.addnewContact('имя','адрес','номер телефона','эл. почта') для добавления контакта.
        Внимание! Все значения, указанные в скобках, должны быть в кавычках!

        Используйте название.redactcontact(порядковый номер контакта,порядковый номер данных,'новые данные')
        для редактироания ваших контактов.

        Используйте название.deletecontact(Порядковый номер контакта), чтобы удалить контакт.

        Используйте название.clearcontactbook(), чтобы полностью очистить книгу
        ''')

    def __init__(self):
        self.book = []

    def addnewContact(self, name, address, phonenumber, mail):
        self.book.append([name, address, phonenumber, mail])
        print('''
     Ваш контакт был сохранен под номером''', len(self.book))

    def seeAllcontacts(self):
        if self.book == []:
            print('Контакты не обнаружены')
        else:
            for i in range(len(self.book)):
                print(i + 1, end='. ')
                for j in range(len(self.book[i])):
                    print(self.book[i][j])

    def redactcontact(self, contactNumber, propertyNumber, NewProperty):
        self.book[contactNumber - 1][propertyNumber - 1] = NewProperty

    def deletecontact(self, contactNumber):
        del self.book[contactNumber - 1]

    def clearContactbook(self):
        for i in range(len(self.book)):
            del self.book[-1]
