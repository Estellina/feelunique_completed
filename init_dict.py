#!/usr/bin/env python
"""Dictionary initializer.

Initializes the required dictionaries and returns them to collect_data.py."""

import time


##### --------------------------------------------------- #####
##### --------------------- URLS ------------------------ #####
##### --------------------------------------------------- #####

def init_url_dict():
    """Initializes the dictionary with the information of a product url

    Returns:
       dict: Dictionary with the product url data.
    """

    url_dict = {
        'product_name': None,
        'product_price': None,
        'code_sku': None,
        'category': None,
        'sub_category': None,
        'sub_sub_category': None,
        'product_url': None,
        'url_category': None,
        'country': 'us',
        'language': 'en',
        'industry': 'cosmetic',
        'collect_date': str(time.strftime("%Y-%m-%d"))

    }
    return url_dict


##### ------------------------------------------------------ #####
##### --------------------- PRODUCT ------------------------ #####
##### ------------------------------------------------------ #####

def init_product_dict():
    """Initializes the dictionary with the product data.

       Returns:
           dict: Dictionary with the product data.
       """

    product_dict = {
        'product_name': None,
        'product_brand': None,
        'Mean_rating': None,
        'n_reviews': None,
        'product_information': None,
        'product_price': None,
        'code_sku': None,
        'category': None,
        'sub_category': None,
        'sub_sub_category': None,
        'url': None,
        'source': 'feelunique_us',
        'country': 'us',
        'language': 'en',
        'industry': 'cosmetic',
        'collect_date': str(time.strftime("%Y-%m-%d"))
    }
    return product_dict


##### ------------------------------------------------------ #####
##### --------------------- REVIEWS ------------------------ #####
##### ------------------------------------------------------ #####

def init_reviews_dict():
    """Initializes the dictionary with the review data.

    Returns:
        dict: Dictionary with the review data.
    """

    reviews_dict = {
        'product_name': None,
        'product_brand': None,
        'category': None,
        'sub_category': None,
        'sub_sub_category': None,
        'writer_pseudo': None,
        'url_product': None,
        'writer_recommendation': False,
        'review_rating': None,
        'review_date': None,
        'review_title': None,
        'review_text': None,
        'review_text_strengths': None,
        'verified_purchase': False,
        'source': 'feelunique_us',
        'country': 'us',
        'language': 'en',
        'industry': 'cosmetic',
        'collect_date': str(time.strftime("%Y-%m-%d"))
    }
    return reviews_dict
