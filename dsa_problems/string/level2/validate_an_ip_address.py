"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-to-validate-an-ip-address/

Author: Nathan Lutala (nlutala)
"""


def is_valid_ip(ip_address: str) -> str:
    """
    A function that validates an IPv4 Address.\n

    According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal
    notation, which consists of four decimal numbers, each ranging from 0 to 255,
    separated by dots, e.g., 172.16.254.1\n

    :param - ip_address (a string denoting an ip address)\n

    returns "Valid" if the ip_address is valid and "Not valid" if otherwise.
    """
    ip_bits = ip_address.split(".")

    if len(ip_bits) != 4:
        return "Not valid"

    for bit in ip_bits:
        try:
            if int(bit) >= 0 and int(bit) < 255:
                continue
            else:
                return "Not valid"
        except ValueError:
            return "Not valid"

    return "Valid"
