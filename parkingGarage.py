class parkingGarage():

    tickets= 1
    parkingSpaces = 10
    currentTicket = {} 


    def parkingSpaces(self):
        return self.parkingSpaces


    def takeTicket(self):
        if self.parkingSpaces == 0:
            print("Sorry we are full")

        else:
            print(f'We have {self.parkingSpaces} spaces available')
            print(f'Your ticket is ticket # {self.tickets}, please keep it safe in order to pay and leave the garage.')
            
            self.currentTicket[self.ticket] = {'paid': False}
            self.parkingSpaces -= 1
            self.tickets += 1


    def payForParking(self):
        payment = input("Enter payment amount:  ")
        if payment:
            self.currentTicket[self.ticket]['paid'] = True 
            print('thanks for paying, you have 15 minutes to leave')
 


    def leaveGarage(self):
        if not self.current_ticket["paid"]:
            payment = input("Enter payment amount: ")
            if payment:
                self.current_ticket["paid"] = True
                print('thanks for paying, you have 15 minutes to leave')
        


print('Have a nice day!')
