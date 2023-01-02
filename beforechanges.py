# You will need a few attributes as well:
#     tickets -> list
#     parkingSpaces -> list
#     currentTicket -> dictionary

        # self.tickets = []
        # self.parkingSpaces = [] 
        # self.currentTicket = {}
    


class parkingGarage():

    tickets= 1
    parkingSpaces = 10
    #paid=true/false
    currentTicket = {} 
#currentticket is constantly getting manipulated as people come in 

    def parkingSpaces(self):
        return self.parkingSpaces

#my garage = mine in parkinggarage, and is the self
    def takeTicket(self):
        if self.parkingSpaces == 0:
            print("Sorry we are full")

        else:
            print(f'We have {self.parkingSpaces} spaces available')
            print(f'Your ticket is ticket # {self.tickets}, please keep it safe in order to pay and leave the garage.')
            
            self.currentTicket[self.ticket] = {'paid': False}
            self.parkingSpaces -= 1
            self.tickets += 1

            # user comes in
            # takes ticket
            # ticket gets a number and variable of paid 
            #     spaces go down 1 
            #return self.tickets (how many are avail)

            #showCapacity()

        if parkingGarage.tickets == 10:
            print ('sorry no more tickets')

        ticket_number= len(self.tickets) + 1 #from garage list... creates a ticket number by adding 1 to the list (which starts off as 0 []), and will keep adding one (so ticket #2, and #3 and so on...) so when we Take Ticket, we can see #1/2/3... paid or not
        myticket = {
            "ticket number": ticket_number, 
            "paid": False}
        self.currentTicket = myticket 
        parkingGarage.parkingSpaces -= 1

        # parkingGarage.tickets += 1
        return self.tickets 
        


    def payForParking(self):
        payment = ()
        if payment:
            self.currentTicket = True
            print('thanks for paying, you have 15 minutes to leave')
    
    #turn ticket (which is currently a string) you need to turn it into an integer 
    # self.currentTicket[f'ticket number'][paid] = True
    #  
    def leaveGarage(self):
        if payment:
            self.currentTicket = True
        print("Thank you have a nice a nice")



print('Have a nice day!')
