#!/usr/bin/python3
"""
A method that determines if a given data set represents \
    a valid UTF-8 encoding.
"""


def validUTF8(data):
    """_summary_

    Args:
        data (list): a list of integers

    Returns:
        boolean: True if data is a valid UTF-8 encoding
     """
    con = 0
    for i in data:
        if con == 0:
            match i:
                case _ if (i >> 5) == 0b110:
                    con = 1
                case _ if (i >> 4) == 0b1110:
                    con = 2
                case _ if (i >> 3) == 0b11110:
                    con = 3
                case _ if (i >> 7) != 0:
                    return False
        else:
            if (i >> 6) != 0b10:
                return False
            con -= 1
    return con == 0
