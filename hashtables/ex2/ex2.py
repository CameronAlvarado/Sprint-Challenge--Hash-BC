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
    route = [None] * (length - 1)

    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    # Start at the first element of the hashtable
    current = hash_table_retrieve(hashtable, "NONE")
    # Keep track of the index
    index = 0
    # Loop through the route array
    while current is not "NONE":
        route[index] = current
        # increase index count by 1 each loop
        index += 1
        current = hash_table_retrieve(hashtable, current)

    return route
