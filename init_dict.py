#!/usr/bin/env python
"""Dictionary initializer.

Initializes the required dictionaries and returns them to collect_data.py."""

import time


def init_url_dict():
    """Initializes the dictionary with the information of a product url
       Returns:
          dict: Dictionary with the product url data.
       """
    url_dict = {
        'product_url': None,
        'n_reviews': None,
        'product_name': None,
        'product_price': None,
        'mean_rating': None,
        'code-sku': None,
    }
    return url_dict


def init_product_dict():
    """Initializes the dictionary with the product data.
       Returns:
           dict: Dictionary with the product data.
       """

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
        'code_sku': None,
        'collect_date': str(time.strftime("%Y_%m_%d"))
    }
    return product_dict


def init_reviews_dict():
    """Initializes the dictionary with the review data.
       Returns:
           dict: Dictionary with the review data.
       """
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
    return reviews_dict
