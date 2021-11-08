# Slightly pulled from here: https://stackoverflow.com/a/43453890

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os, os.path
from pathlib import Path

GOOGLE_SEARCH_URL_TEMPLATE = "https://www.google.co.in/search?q=+{}+&source=lnms&tbm=isch"
IMG_OUT_DIR_TEMPLATE = "query_images/{}/"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
VALID_IMG_EXTS = {"jpg", "jpeg", "png", "gif"}

IMGS_PER_SCROLL = 400
SCROLLS_TO_REACH_MORE_IMGS_BUTTON = 10

def init_selenium(query):
    driver = webdriver.Firefox()
    query_url = GOOGLE_SEARCH_URL_TEMPLATE.format(query)
    driver.get(query_url)

    return driver

def get_num_images_we_already_have_for_query(query):
    query_dir = IMG_OUT_DIR_TEMPLATE.format(query)
    Path(query_dir).mkdir(parents=True, exist_ok=True)

    return len(os.listdir(query_dir))
    

def get_and_write_n_images_to_disk(driver, start_img_idx, end_img_idx):
    num_imgs = end_img_idx - start_img_idx + 1
    num_scrolls = num_imgs // IMGS_PER_SCROLL

    for _ in num_scrolls:
        scroll_to_load_more_imgs_button(driver)
        save_imgs_to_disk_from_scroll(driver, query)
        click_more_imgs_button(driver)

def scroll_to_load_more_imgs_button(driver):
    for _ in Range(SCROLLS_TO_REACH_MORE_IMGS_BUTTON):
        driver.execute_script("window.scrollBy(0, 1000000)")
        time.sleep(0.2)

def click_more_imgs_button(driver):
    driver.find_element_by_xpath("//input[@value='Show more results']").click()

def save_imgs_to_disk_from_scroll(driver, query):
    pass

def generate_image_name(query, img_idx):
    return "{}_{}.png".format(query, img_idx)

def main():
    query = "cheese"
    tot_imgs = 100000

    num_imgs_of_of_query_on_disk = get_num_images_we_already_have_for_query(query)

    try:
        # driver = init_selenium(query)
        get_and_write_n_images_to_disk(driver, num_imgs_of_of_query_on_disk, tot_imgs)

    finally:
        driver.close()

main()