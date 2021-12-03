"""
Module for computing integer sum

Author: AlexGM
Date: Nov, 2021
"""

import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def sum_vals(int_1, int_2):
    '''
    Args:
        int_1: (int)
        int_2: (int)
    Return:
        int_1 + int_2 (int)
    '''
    try:
        assert isinstance(int_1, int)
        assert isinstance(int_2, int)
        logging.info("Input types are correct!")
    except AssertionError:
        logging.error("Only integers allowed!")
    return int_1 + int_2


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(3.4, 5)
    sum_vals(4, 5)
