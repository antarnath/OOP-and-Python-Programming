class Star_Cinema:
    __hall_list = []
    def entry_hall(self, object):
        self.__hall_list.append(object)
    
        

class Hall(Star_Cinema):

    _all_seats = {}
    _all_shows = []
    _all_hall_no = {}
    _all_row_col = {}

    def __init__(self, rows, cols, hall_no):

        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    
        self.entry_hall(self)
        

    def entry_show(self, id, movie_name, time):

        self.id = id
        self.movie_name = movie_name
        self.time = time



        self.show_list.append((self.id, self.movie_name, self.time))
        self._all_shows.append((self.id, self.movie_name, self.time))
        self._all_row_col[self.id] = [self.rows,self.cols]

        self.build_set = [[True]*self.cols]*self.rows
        self.seats[self.id] = self.build_set
        self._all_hall_no[self.id]=self.hall_no 

        self.char = []
      
        for i in range(self.rows):
            self.ant  = []
            for j in range(self.cols):
                self.ant.append(str(chr(i+65))+str(j))
            self.char.append(self.ant)
        self.seats[self.id] = self.char
        self._all_seats[self.id] = self.char


    def view_show_list(self):
        print("_"*100)
        print()
        for id, movie, time in self._all_shows:
            print("MOVIE NAME: ",movie,end="\t\t")
            print("SHOW ID: ",id,end="\t\t")
            print("TIME: ",time)
        print("_"*100)
        print("\n")


    def book_seats(self, name, phone_number, id):
        self.name = name
        self.phone_number = phone_number
        self.show_id = id
        

    def view_available_seats(self, id):
        self.show_id_1 = id
        flag = False
        for tup in self._all_shows:
            if self.show_id_1 in tup:
                flag = True
        if flag:
            aaa = self._all_seats[id]
            for id, movie, time in self._all_shows:
                if self.show_id_1 == id:
                    print("MOVIE NAME: ", movie, end='\t\t')
                    print("TIME: ",time)
            print("X for already booked seats")
            print("_"*100)
            print()
            for aa in aaa:
                for a in aa:
                    print(a,end="\t\t")
                print()
            print("_"*100)
            print("\n")
        else:
            # print("THIS SHOW ID IS INVALID. PLEASE ENTER THE RIGHT SHOW ID")
            # print()
            # id = input("ENTER SHOW ID: ")
            # self.view_available_seats(id)
            print("_"*50,"\n")
            print("Id didn't match with any show!")
            print("_"*50,"\n")


    def book_ticket(self):
        name = input("ENTER CUSTOMER NAME: ")
        phone = input("ENTER CUSTOMER PHONE NUMBER: ")
        this_id = input("ENTER SHOW ID: ")
        flag = False
        for tup in self._all_shows:
            if this_id in tup:
                flag = True
        if flag:
            number_of_ticket = int(input("ENTER NUMBER OF TICKETS: "))

            tickets = []
            for i in range(number_of_ticket):
                tik = input("ENTER SEAT NO: ")
                if tik in tickets:
                    # print("THIS SEAT IS ALREADY BOOKED")
                    print("_"*50,"\n")
                    print("THESE SEATS WERE BOOKED -",tik)
                    print("_"*50,"\n")
                else:

                    antar_list = self._all_seats[this_id]

                    # booked ticket check
                    check = False
                    
                    if len(tik)==1:
                        print("_"*50,"\n")
                        print("INVALID SEAT NO -",tik,". TRY AGAIN!")
                        print("_"*50,"\n")
                        continue
                    if len(tik)>2:
                        print("_"*50,"\n")
                        print("INVALID SEAT NO -",tik,". TRY AGAIN!")
                        print("_"*50,"\n")
                        continue
                    if ("A"<=tik[0]>="Z")or("0"<=tik[1]>="9"):
                        print("_"*50,"\n")
                        print("INVALID SEAT NO -",tik,". TRY AGAIN!")
                        print("_"*50,"\n")
                        continue

                    i = ord(tik[0])-65
                    j = int(tik[1])
                    
                    a, b = self._all_row_col[this_id]
                    

                    if i>=a or j>=b:
                        print("_"*50,"\n")
                        print("INVALID SEAT NO -",tik,". TRY AGAIN!")
                        print("_"*50,"\n")
                        continue
                    else:
                        if antar_list[i][j]=='X':
                            check = True        
                    if check:
                        print("_"*50,"\n")
                        print("THESE SEATS WERE BOOKED -",tik)
                        print("_"*50,"\n")
                        continue    
                    else:
                        # invalid seat check
                        flag = False
                        for aa in antar_list:
                            if tik in aa:
                                tickets.append(tik)
                                flag = True
                        if flag==False:
                            print("_"*50,"\n")
                            print("INVALID SEAT NO -",tik,". TRY AGAIN!")
                            print("_"*50,"\n")
                            continue
            if len(tickets)==0:
                return                    
            list = self._all_seats[this_id]
            for ticket in tickets:
                for a in list:
                    for i in range(len(a)):
                        if a[i] == ticket:
                            a[i] = "X"
            print("#"*8," TICKET BOOKED SUCCESSFULLY!! ","#"*8)
            print("_"*100)
            print()
            print("NAME: ",name)
            print("PHONE NUMBER: ", phone)
            print()
            for id, movie, time in self._all_shows:
                if this_id == id:
                    print("MOVIE NAME: ", movie,end="\t\t\t")
                    print("MOVIE TIME: ", time)
            print("TICKETS: ",end="")
            for ticket in tickets:
                print(ticket,end=" ")
            print()
            print("HALL", self._all_hall_no[id])
            print("\n")
            print("_"*100)
            print()
        else:
            # print('\n')
            # print("THIS SHOW ID IS INVALID. PLEASE ENTER THE RIGHT SHOW ID")
            # print()
            # self.book_ticket()
            print("_"*50,"\n")
            print("Id didn't match with any show!")
            print("_"*50,"\n")


    def main(self):
        while True:
            print("1. VIEW ALL SHOWS TODAY")
            print("2. VIEW AVAILABLE SEATS")
            print("3. BOOK TICKET")

            option = int(input("ENTER OPTION: "))

            if option == 1:
                print()
                self.view_show_list()
            elif option == 2:
                id = input("ENTER SHOW ID: ")
                self.view_available_seats(id)
            elif option == 3:
                self.book_ticket()
            else:
                print("THERE IS NO OPTION PLEASE CHOSE RIGHT OPTION")


    




bonoful = Hall(4, 5, "A10")
bonoful.entry_show("ae123", "Black Adam", "Oct 26 2022 10:00 PM")

jumur = Hall(5, 6, "B10")
jumur.entry_show("ae50", "Superman" ,"Oct 26 2022 08:00 PM")



jumur.main()