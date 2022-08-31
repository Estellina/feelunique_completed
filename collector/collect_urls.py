#!/usr/bin/env python
"""URLs collector.

Crawls the categories list and sends the category URL to the page navigator.""" # TODO -> revoir docstring

import os

from selenium import webdriver

from page_navigator import save_products_page_data

from categories import CATEGORIES
from const import OPTIONS

PATH_URLS_NEW = os.path.join(os.curdir, 'urls_new')
PATH_DRIVER = os.path.join(os.curdir, 'chromedriver')


# TODO -> 2 espaces
def main():
    for category in CATEGORIES:
        category_dict = {
            'category': category[0],
            'sub_category': category[1],
            'sub_sub_category': category[2],
            'url_category': category[4]
        }

        driver = webdriver.Chrome(PATH_DRIVER, options=OPTIONS)

        # Collect urls data
        _ = save_products_page_data(driver, category_dict, PATH_URLS_NEW)

        driver.delete_all_cookies()
        driver.quit()


if __name__ == "__main__":
    main()
