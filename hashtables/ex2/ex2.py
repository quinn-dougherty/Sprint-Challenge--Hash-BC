#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    assert (len(tickets) == length)

    for ticket in tickets:

        if ticket.source=="NONE":
            # The ticket for your first flight has a destination with a source of NONE
            route[0] = ticket.destination
        if ticket.destination=="NONE":
            route[-2] = ticket.source
            route[-1] = "NONE"

        hash_table_insert(hashtable, ticket.source, ticket.destination)

    source = route[0]
    for i in range(1, length-2):
        route[i] = hash_table_retrieve(hashtable, source)
        source = route[i]
    return route
