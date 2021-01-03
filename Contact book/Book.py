class ContactBook:
    print('''
        Используйте x = ContactBook() для создания книги, где x - название этой книги.
        Используйте x.comands для просмора комманд.''')

    def comands(self):
        print('''
        Используйте x.seeallcontact() для просмотра всех контактов.

        Используйте x.addcontact() для добавления контакта.
        В скобках укажите имя, адрес, номер телефона, адрес электронной почты.
        Внимание! Все значения, указанные в скобках, должны быть в ковычках!''')

    def __init__(self):
        self.book = []

    def addcontact(self, name, address, phonenumber, mail):
        self.book.append([name, address, phonenumber, mail])
        print('''
     Ваш контакт был сохранен под номером''', len(self.book))

    def seeallcontact(self):
        for i in range(len(self.book)):
            print(i + 1, end='. ')
            for j in range(len(self.book[i])):
                print(self.book[i][j])

