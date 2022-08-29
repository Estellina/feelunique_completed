import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from page_navigator import save_products_page_data
import time
import os
import random
from categories import CATEGORIES
from init_dict import (
    init_url_dict)
from const import OPTIONS

PATH_URLS_NEW = os.path.join(os.curdir, 'urls_new')
PATH_DRIVER = os.path.join(os.curdir, 'chromedriver')


def main():
    for category in CATEGORIES:
        # Retrieve the values from the dictionary
        category_dict = {
            'category': category[0],
            'sub_category': category[1],
            'sub_sub_category': category[2],
            'url_category': category[4]
        }

        # Set the driver
        driver = webdriver.Chrome(PATH_DRIVER, options=OPTIONS)

        # Collect urls data
        _ = save_products_page_data(driver, category_dict, PATH_URLS_NEW)

        driver.delete_all_cookies()
        driver.quit()


if __name__ == "__main__":
    main()
