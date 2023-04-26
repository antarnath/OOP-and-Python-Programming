import keyboard



class Book:
    def __init__(self):
        self.book = []

    def open_book(self):
        file= open('Test.txt', 'r')
        self.lines = file.readlines()
        str = ''
        for line in self.lines:
            for i in range(len(line)):
                if line[i]=='-' and line[i+1]=='-':
                    self.book.append(str)
                    str = ''
                if line[i]=='-':
                    pass
                else:
                    str += line[i]
        self.book.append(str)
    
    def display(self):
        
        cnt = 0
        print(self.book[cnt])
        print('[enter - read more, press q to quit')
        skip_page = int(input('Enter a number to skip this page: '))
        if cnt+skip_page < len(self.book):
            cnt = cnt + skip_page
            print(self.book[cnt])
        else:
            print("This page is not available in the book")
        
        reverse_page = int(input("Enter a number to reverse this page: "))

        if cnt+reverse_page >= 0:
            cnt = cnt+reverse_page
            print(self.book[cnt])
        else:
            print("This page is not available in the book")

        while(keyboard.read_key()!='q'):
            cnt += 1
            if keyboard.read_key() == 'enter':               
                if cnt < len(self.book):
                    print(self.book[cnt])
                else:
                    cnt = len(self.book)
                    print('End of book')
                    return
            else:
                print('press a wrong key! please press a right key')
            print('[enter - read more, press q to quit')
       



physis = Book()
physis.open_book()
physis.display()

