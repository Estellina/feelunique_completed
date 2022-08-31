# !/usr/bin/env python
"""Page collector.

Collects data from a single product page by sending the specified URL to the page navigator."""

import os


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from const import OPTIONS
from page_navigator import save_product_page_data

PATH_PRODUCT = os.path.join(os.curdir, 'product')
PATH_REVIEW = os.path.join(os.curdir, 'review')
PATH_DRIVER = os.path.join(os.curdir, 'chromedriver')


def main():
    # Select the url
    category_dict = {
        'url': 'https://us.feelunique.com/p/Lixir-Skin-Universal-Emulsion-100ml',
        'category': 'Skincare',
        'sub_category': 'Moisturisers',
        'sub_sub_category': 'Day Creams'
    }

    # Load the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=OPTIONS)

    # Collect product and reviews data
    _ = save_product_page_data(driver, category_dict, PATH_PRODUCT, PATH_REVIEW)

    driver.delete_all_cookies()
    driver.quit()


if __name__ == "__main__":
    main()
