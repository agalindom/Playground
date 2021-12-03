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


def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        assert isinstance(numerator, float)
        assert isinstance(denominator, float)
    except AssertionError:
        logging.error("One or both input types are not float")
    try:
        assert denominator != 0
        logging.info("%d/%d", numerator, denominator)
        fraction_val = numerator / denominator
        return fraction_val
    except AssertionError:
        logging.error("Denominator cannot be zero")

    return None


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        assert isinstance(text, str)
        logging.info("%s", text)
        splited_words = len(text.split())
        return splited_words
    except AssertionError:
        logging.error("Text argument must be a string")

    return None


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(3, 5)
    divide_vals(3.4, 0)
    divide_vals(4.5, 2.7)
    divide_vals(-3.8, 2.1)
    divide_vals(1, 2)
    num_words(5)
    num_words('This is the best string')
    num_words('one')
