class parkingGarage():

    tickets= 1
    parkingSpaces = 10
    currentTicket = {} 

    def takeTicket(self):
        if self.parkingSpaces == 0:
            print("Sorry we are full")

        else:
            print(f'We have {self.parkingSpaces} spaces available')
            print(f'Your ticket is ticket # {self.tickets}, please keep it safe in order to pay and leave the garage.')
            
            self.currentTicket[self.tickets] = {'paid': False}
            self.parkingSpaces -= 1
            self.tickets += 1


    def payForParking(self):
        #want to ask user what ticket they have, so they can continue payment, 
        currentTicket= int(input("What ticket are you paying for? "))
        payment = input("Enter payment amount:  ")
        if payment:
            self.currentTicket[currentTicket]['paid'] = True 
            print('thanks for paying, now head to the exit.')
 

    def leaveGarage(self):
        currentTicket= int(input("Insert ticket number: "))
        if not self.currentTicket[currentTicket]["paid"]:
            payment = input("Enter payment amount: ")
        else:
            print('thanks for paying, you have 15 minutes to leave')


garage = parkingGarage()
garage.takeTicket()
garage.payForParking()
garage.leaveGarage()

print('Have a nice day!')
