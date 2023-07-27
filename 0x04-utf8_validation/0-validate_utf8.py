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
    count = 0
    for num in data:
        if count == 0:
            match num:
                case _ if (num >> 5) == 0b110:
                    count = 1
                case _ if (num >> 4) == 0b1110:
                    count = 2
                case _ if (num >> 3) == 0b11110:
                    count = 3
                case _ if (num >> 7) != 0:
                    return False
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
