import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
# TODO -> saut de ligne
from data_collector import (
    collect_urls_data,
    collect_product_data,
    collect_reviews_data)
from collector.utils import save_data # TODO -> par ordre alphabétique


##### ------------------------------------------------ #####
##### ----------------- PRODUCTS PAGE ---------------- #####
##### ------------------------------------------------ #####
# TODO -> saut de ligne
def save_products_page_data(driver, category_dict, paths_urls):
    """Collects and saves the data contained in the products-listing page `category_dict['url_category']`.

        :param driver: selenium webdriver.
        :param category_dict: dictionary containing the category's URL and its abores.
        :param paths_urls: path of the directory in which the urls will be saved.
    """
    # TODO -> saut de ligne
    # Load the url
    print("[LOG] Loading the page...")
    driver.get(category_dict['url_category'])
    print("[LOG] Current url: {}.".format(category_dict['url_category']))
    time.sleep(random.uniform(1, 5))

    try:
        cookie_btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located((
            By.ID, 'notice-ok')))
        cookie_btn.click()
        print("[LOG] Click on the cookies button.")
        time.sleep(random.uniform(1, 5))
    except:
        pass

    while True:
        try:
            more_products_btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located((
                By.CSS_SELECTOR, '#fullcolumn > div.eba-component.loadMoreContainer > div.loadMore > a')))
            driver.execute_script('arguments[0].scrollIntoView(true);', more_products_btn)
            driver.execute_script('arguments[0].click();', more_products_btn)
            print("[LOG] Click on show more products button.")
            time.sleep(random.uniform(1, 5))
        # TODO -> saut de ligne ?
        except TimeoutException:
            print("[LOG] There isn't any more products to show.")
            break
        # TODO -> saut de ligne ?
        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            break
        # TODO -> saut de ligne ?
        except:
            break

            # Collect the printed products # TODO ???
        try:
            print("[LOG] Start collecting urls data.")

            # Collect urls data
            # TODO -> saut de ligne ?
            url_dicts = collect_urls_data(driver, category_dict)
            # TODO -> saut de ligne ?
            # Save the urls data
            save_data(paths_urls, url_dicts, 'urls_new')
            # TODO -> saut de ligne ?
            print("[LOG] {} urls have been collected.".format(len(url_dicts)))
        # TODO -> saut de ligne ?
        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            pass
        # TODO -> saut de ligne ?
        except:
            print("[LOG] There is an error for the current url.")
            pass


##### ------------------------------------------------ #####
##### ----------------- PRODUCT PAGE ----------------- #####
##### ------------------------------------------------ #####
# TODO -> saut de ligne ?
def save_product_page_data(driver, category_dict, path_products, path_reviews):
    """Collects the data contained in the product page `category_dict['url']`.

    Args:
        driver: selenium driver
        category_dict (dict): dictionary containing the product's categories and its URL.
        path_products (str): path of the directory in which the products will be saved.
        path_reviews (str): path of the directory in which the reviews will be saved.

    Returns:
        tuple[dict, list]:
            dict: Dictionary with the product data.
            list: List of dictionaries with the review data.
    """

    # Load the url
    print("[LOG] Loading the page...")
    driver.get(category_dict['url'])
    print("[LOG] Current url:", category_dict['url'])
    time.sleep(random.uniform(1, 5))

    # Close the cookies pop up
    try:
        cookie_btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located((
            By.CSS_SELECTOR, 'button[id="didomi-notice-agree-button"]')))
        cookie_btn.click()
        print("[LOG] Click on the cookies button.")
        time.sleep(random.uniform(1, 5))
    except:
        pass

    print("[LOG] Start collecting product data.")
    # Collect the product data
    product_dict = collect_product_data(driver, category_dict)

    # Save the product data
    save_data(path_products, product_dict, 'products')

    print("[LOG] Start collecting reviews data.")
    while True:
        # collect all the reviews -> # TODO -> Collect reviews data
        reviews_dicts = collect_reviews_data(driver, product_dict)
        # save reviews data # TODO -> Save reviews data
        save_data(path_reviews, reviews_dicts, 'reviews')
        print("[LOG] All the reviews on this page were collected.") # TODO -> "All the reviews have been collected"

        # Clicking on the next slide button
        try:
            more_reviews_btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located((
                By.CSS_SELECTOR, 'li[class*="buttons-item-next"] > a[class*="bv-content-btn-pages-active"]')))
            driver.execute_script("arguments[0].scrollIntoView(true);", more_reviews_btn)
            driver.execute_script("arguments[0].click();", more_reviews_btn)
            print("[LOG] Click on show more reviews button.")
            time.sleep(random.uniform(1, 5))
        # TODO -> saut de ligne ?
        except TimeoutException:
            print("[LOG] There isn't any more reviews to show.")
            break
        # TODO -> saut de ligne ?
        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            break
        # TODO -> saut de ligne ?
        except:
            break
    # TODO -> saut de ligne ?
    return product_dict, reviews_dicts
