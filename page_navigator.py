import random
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from data_collector import (
    collect_urls_data,
    collect_product_data,
    collect_reviews_data)
from utils import save_data


##### ------------------------------------------------ #####
##### ----------------- PRODUCTS PAGE ---------------- #####
##### ------------------------------------------------ #####
def save_products_page_data(driver, category_dict, paths_urls):
    """Collects and saves the data contained in the products-listing page `category_dict['url_category']`.

        :param driver: selenium webdriver.
        :param category_dict: dictionary containing the category's URL and its abores.
        :param paths_urls: path of the directory in which the urls will be saved.
    """
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

        except TimeoutException:
            print("[LOG] There isn't any more products to show.")
            break

        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            break

        except:
            break

            # Collect the printed products
        try:
            print("[LOG] Start collecting urls data.")

            # Collect urls data

            url_dicts = collect_urls_data(driver, category_dict)
            # Save the urls data
            save_data(paths_urls, url_dicts, 'urls_new')

            print("[LOG] {} urls have been collected.".format(len(url_dicts)))

        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            pass

        except:
            print("[LOG] There is an error for the current url.")
            pass


##### ------------------------------------------------ #####
##### ----------------- PRODUCT PAGE ----------------- #####
##### ------------------------------------------------ #####
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
        # collect all the reviews
        reviews_dicts = collect_reviews_data(driver, product_dict)
        # save reviews data
        save_data(path_reviews, reviews_dicts, 'reviews')
        print("[LOG] All the reviews on this page were collected.")

        # Clicking on the next slide button
        try:
            more_reviews_btn = WebDriverWait(driver, 10).until(ec.presence_of_element_located((
                By.CSS_SELECTOR, 'li[class*="buttons-item-next"] > a[class*="bv-content-btn-pages-active"]')))
            driver.execute_script("arguments[0].scrollIntoView(true);", more_reviews_btn)
            driver.execute_script("arguments[0].click();", more_reviews_btn)
            print("[LOG] Click on show more reviews button.")
            time.sleep(random.uniform(1, 5))

        except TimeoutException:
            print("[LOG] There isn't any more reviews to show.")
            break

        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            break

        except:
            break
    return product_dict, reviews_dicts


def save_products_search_page_data(driver, category_dict, path_urls_search):
    """Collects and saves the data contained in the products-listing page `category_dict['url_category']`.

            :param driver: selenium webdriver.
            :param category_dict: dictionary containing the category's URL and its abores.
            :param paths_urls_search: path of the directory in which the urls will be saved.
        """
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

        except TimeoutException:
            print("[LOG] There isn't any more products to show.")
            break

        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            break

        except:
            break

            # Collect the printed products
        try:
            print("[LOG] Start collecting urls data.")

            # Collect urls data

            url_dicts = collect_urls_data(driver, category_dict)
            # Save the urls data
            save_data(path_urls_search, url_dicts, 'urls_search')

            print("[LOG] {} urls have been collected.".format(len(url_dicts)))

        except KeyboardInterrupt:
            print("[LOG] The collect has been interrupted by the user.")
            pass

        except:
            print("[LOG] There is an error for the current url.")
            pass
