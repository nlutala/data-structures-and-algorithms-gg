"""
A file tests the get_itinerary function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.find_itinerary_from_a_given_list_of_tickets import (
    get_itinerary,
)


def test_get_itinerary():
    """
    Example 1
    Input:
    "Chennai" -> "Banglore"
    "Bombay" -> "Delhi"
    "Goa"    -> "Chennai"
    "Delhi"  -> "Goa"

    Output:
    Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore
    """
    tickets = {
        "Chennai": "Banglore",
        "Bombay": "Delhi",
        "Goa": "Chennai",
        "Delhi": "Goa",
    }
    assert (
        get_itinerary(tickets)
        == "Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore"
    )
