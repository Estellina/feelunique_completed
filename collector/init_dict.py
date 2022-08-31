#!/usr/bin/env python
"""Dictionary initializer.

Initializes the required dictionaries and returns them to collect_data.py.""" # TODO -> docstring 

import time


def init_url_dict():
    # TODO -> ???
    url_dict = {
        'product_url': None,
        'n_reviews': None,
        'product_name': None,
        'product_price': None,
        'mean_rating': None
    }
    # TODO -> ???
    return url_dict


def init_product_dict():
    # TODO -> ???
    product_dict = {
        'product_name': None,
        'product_information': None,
        'category': None,
        'sub_category': None,
        'sub_sub_category': None,
        'mean_rating': None,
        'product_price': None,
        'n_reviews': None,
        'product_url': None,
        'collect_date': str(time.strftime("%Y_%m_%d"))
    }
    # TODO -> ???
    return product_dict


def init_reviews_dict(): # init_review_dict
    # TODO -> ???
    reviews_dict = {
        'review_rating': None,
        'review_title': None,
        'review_author': None,
        'category': None,
        'sub_category': None,
        'sub_sub_category': None,
        'review_date': None,
        'review_text': None,
        'collect_date': str(time.strftime("%Y_%m_%d"))
    }
    # TODO -> ???
    return reviews_dict
