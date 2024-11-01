"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/

Author: Nathan Lutala (nlutala)
"""


def get_itinerary(tickets: dict[str, str]) -> str:
    """
    Given a dictionary of tickets, find itinerary in order.\n

    :param - tickets (dictionary)\n

    returns the itinerary in order.
    """
    start = [place for place in tickets if place not in tickets.values()]
    start = start[0]

    itinerary = []

    while tickets.get(start) is not None:
        itinerary.append(f"{start}->{tickets.get(start)}")
        start = tickets.get(start)

    return ", ".join(itinerary)
