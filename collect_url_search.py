#!/usr/bin/env python
"""Urls collector.
Collects product urls by gathering all urls matching the search keywords."""


import os
import urllib.parse

from selenium import webdriver

from page_navigator import save_products_search_page_data

from const import SEARCH_KEYWORDS

from const import OPTIONS

PATH_URLS_NEW_SEARCH = os.path.join(os.curdir, 'urls_search')

PATH_DRIVER = os.path.join(os.curdir, 'chromedriver')


def main():
    for keyword in SEARCH_KEYWORDS :
        category_dict = {
            'url_category': 'https://us.feelunique.com/search?q=' + urllib.parse.quote(keyword),
            'category': None,
            'sub_category': None,
            'sub_sub_category': None,
            'sub_sub_sub_category': None,
        }
        # Set the driver
        driver = webdriver.Chrome(PATH_DRIVER, options=OPTIONS)

        _ = save_products_search_page_data(driver, category_dict,
                                           PATH_URLS_NEW_SEARCH)


if __name__ == "__main__":
    main()