# You will need a few attributes as well:
#     tickets -> list
#     parkingSpaces -> list
#     currentTicket -> dictionary

        # self.tickets = []
        # self.parkingSpaces = [] 
        # self.currentTicket = {}
    


class parkingGarage():

    tickets= 10
    # parkingSpaces = 10
    currentTicket = {} #paid=true/false

    def __init__(self, tickets, parkingSpaces, currentickets):
        
        self.tickets = []
        self.parkingSpaces = 10
        self.currentTicket = {}

    def parkingSpaces(self):
        return self.parkingSpaces


    def takeTicket(self):
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
            self.currentTicket = True:
            print('thanks for paying, you have 15 minutes to leave')
    

    def leaveGarage(self):
        if payment:
            self.currentTicket = True
        print("Thank you have a nice a nice")



print('Have a nice day!')
