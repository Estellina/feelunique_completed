"""Data collectors.

Regroups all the collectors that collect data on the targeted pages.
Those collectors return the data in the form of dictionaries."""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from init_dict import (
    init_url_dict,
    init_product_dict,
    init_reviews_dict
)


##### --------------------------------------------------- #####
##### --------------------- URLS ------------------------ #####
##### --------------------------------------------------- #####

def collect_urls_data(driver, category_dict):
    """Collects the urls data on the page `category_dict['url_category']`.

    Args:
        driver (WebDriver): selenium webdriver.
        category_dict (dict): dictionary containing the category's URL and its arborescence.

    Returns:
        list: List of dictionaries with the urls data.
    """

    url_dicts = []
    time.sleep(5)
    products = driver.find_elements(
        By.CSS_SELECTOR, 'div[class="eba-component eba-product-listing"] div[class="Product"]')
    print("[LOG] Start collecting urls data.")

    for i, product in enumerate(products):
        # Initialising the url_dict
        url_dict = init_url_dict()

        # Product categories
        url_dict['category'] = category_dict['category']
        url_dict['sub_category'] = category_dict['sub_category']
        url_dict['sub_sub_category'] = category_dict['sub_sub_category']
        url_dict['url_category'] = category_dict['url_category']

        # Product name
        try:
            url_dict['product_name'] = product.find_element(By.CLASS_NAME, 'Product-summary').text

        except:
            pass

        # Product price
        try:
            product_prices = product.find_element(By.CLASS_NAME, 'Product-price')
            url_dict['product_price'] = product_prices.find_element(By.TAG_NAME, 'span').text

        except:
            pass

        # Mean rating
        try:
            url_dict['Mean_rating'] = product.find_element(By.CSS_SELECTOR, 'span[data-aggregate-rating]') \
                .get_attribute('data-aggregate-rating')
        except:
            pass

        # reviews count
        try:
            url_dict['n_reviews'] = int(product.find_element(By.CSS_SELECTOR, 'span[class="Rating-count"]') \
                .get_attribute('data-review-count').text.split(' ')[0])
            print(url_dict['n_reviews'])
        except:
            pass

        # product url
        try:
            url_dict['product_url'] = product.find_element(By.CSS_SELECTOR, 'a[class="Product-link thumb "]') \
                .get_attribute('href')
        except:
            pass

        # code sku
        try:
            url_dict['code_sku'] = product.get_attribute('data-sku')
        except:
            pass

        url_dicts.append(url_dict)

    return url_dicts


##### ------------------------------------------------------ #####
##### --------------------- PRODUCT ------------------------ #####
##### ------------------------------------------------------ #####

def collect_product_data(driver, category_dict):
    """Collects the data of the product on the page `category_dict['url']`.

    Args:
        driver (WebDriver): selenium driver
        category_dict (dict): dictionary containing the product's categories and its URL.

    Returns:
        dict: Dictionary with product data.
    """

    # Initialising the product dictionary and the list of dictionaries
    product_dict = init_product_dict()

    # Product url
    product_dict['url'] = category_dict['url']

    # Product categories
    product_dict['category'] = category_dict['category']
    product_dict['sub_category'] = category_dict['sub_category']
    product_dict['sub_sub_category'] = category_dict['sub_sub_category']

    # Product name
    try:
        product_dict['product_name'] = driver.find_element(
            By.CSS_SELECTOR, 'h1[class="fn"]').text
    except:
        pass

    # Product information
    try:
        product_dict['product_information'] = driver.find_element(
            By.CSS_SELECTOR, 'div[class="Layout-golden-main"]').text
    except:
        pass

    # Product price
    try:
        product_dict['product_price'] = driver.find_element(
            By.CSS_SELECTOR, 'span[class="Price"]').text
    except:
        pass

    # Review count
    try:
        product_dict['n_reviews'] = int(driver.find_element(
            By.CSS_SELECTOR, 'span[class="Rating-count"]').text.split(' ')[0])

    except:
        pass

    # Product brand
    try:
        product_dict['product_brand'] = driver.find_element(
            By.CSS_SELECTOR, 'p[class~="u-flush-v"] strong').text
    except:
        pass

    # code sku
    try:
        product_dict['code_sku'] = driver.find_element(
            By.CSS_SELECTOR, 'div[class="item"] >form [class="add-to-wishlist wishHeart"]').get_attribute('data-sku')
    except:
        pass

    # Product url
    try:
        product_dict['product_url'] = driver.current_url
    except:
        pass

    # mean rating
    try:
        product_dict['Mean_rating'] = driver.find_element(
            By.CSS_SELECTOR, 'span[class="Rating-average"]').get_attribute('data-aggregate-rating')
    except:
        pass

    return product_dict


##### ------------------------------------------------------ #####
##### --------------------- REVIEWS ------------------------ #####
##### ------------------------------------------------------ #####

def collect_reviews_data(driver, product_dict):
    """Collects the data contained in the displayed reviews in the product page.

     Args:
         driver (WebDriver): selenium driver.
         product_dict (dict): dictionary with the product information.

     Returns:
         list: List of dictionaries with reviews data.
     """

    # List of dictionary of reviews
    reviews_data = []

    try:
        reviews = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((
            By.CSS_SELECTOR, 'ol[class*="bv-content-list-reviews"] > li')))

    except KeyboardInterrupt:
        exit("[LOG] The collect has been interrupted by the user.")

    except TimeoutException:
        print("[LOG] There aren't any reviews on the current page.")
        pass

    except Exception as e:
        print(e)
        pass

    for _, review in enumerate(reviews):

        # Initialising the reviews dict
        review_dict = init_reviews_dict()

        review_dict['product_name'] = product_dict['product_name']
        review_dict['product_brand'] = product_dict['product_brand']
        review_dict['category'] = product_dict['category']
        review_dict['sub_category'] = product_dict['sub_category']
        review_dict['sub_sub_category'] = product_dict['sub_sub_category']
        review_dict['url_product'] = product_dict['url']

        # Review rating
        try:
            review_dict['review_rating'] = review.find_element(
                By.CSS_SELECTOR, 'meta[itemprop="ratingValue"]').get_attribute('content')
        except:
            pass

        # Review title
        try:
            review_dict['review_title'] = review.find_element(
                By.CSS_SELECTOR, 'h3[class="bv-content-title"]').text
        except:
            pass

        # Review author
        try:
            review_dict['writer_pseudo'] = review.find_element(
                By.CSS_SELECTOR, 'span[class="bv-author"]').text
        except:
            pass

        # Review content
        try:
            review_dict['review_text'] = review.find_element(
                By.CSS_SELECTOR, 'div[class="bv-content-summary-body-text"]').text
        except:
            pass

        # Review date
        try:
            review_dict['review_date'] = review.find_element(
                By.CSS_SELECTOR, 'meta[itemprop="datePublished"]').get_attribute('content')
        except:
            pass

        # review text strengths
        try:
            review_dict['review_text_strengths'] = []
            elements = review.find_elements(
                By.CSS_SELECTOR, 'li[class="bv-popup-histogram-ratings-bar"] > span > span:last-child')
            for element in elements:
                review_dict['review_text_strengths'].append(element.text)
        except:
            pass

        # writer's recommendation
        try:
            review_dict['writer_recommendation'] = review.find_element(
                By.CSS_SELECTOR, 'div[class="bv-content-data-recommend-yes"] > div[class="bv-content-data-value"] > '
                                 'span:last-child').text
        except:
            pass

        # verified purchase
        try:
            review_dict['verified_purchase'] = review.find_element(
                By.CSS_SELECTOR, 'span[class="bv-badge-label"]').text
        except:
            pass

        reviews_data.append(review_dict)
    print("[LOG] Saving all the reviews data.")
    return reviews_data
