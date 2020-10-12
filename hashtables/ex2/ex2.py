#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination




d = {}
def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    route = list()
    #iterate through tickets in tickets arr
    for i in range(length-1):
        # if tickets[i].source == "None":
        #     route.insert(0, tickets[i].destination)
        d[tickets[i].source] = tickets[i].destination
    #make source the key of the dict and destination the value of the dict
    #if key = None make that the 1st item in list
    #check value to see if it equals a key in the dict and append that value to the array

    index = 0
    curr_destination = "NONE"

    while index < length:
        curr_destination = d.get(curr_destination)
        route.append(curr_destination)
        index += 1

    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))
print(d)