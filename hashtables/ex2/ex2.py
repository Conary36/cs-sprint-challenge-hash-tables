#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    Dict_tickets = {}
    for ticket in tickets:
        Dict_tickets[ticket.source] = ticket.destination
    route = []
    s = Dict_tickets['NONE']
    route.append(s)
    while s != 'NONE':
        s = Dict_tickets[s]
        route.append(s)

    return route
