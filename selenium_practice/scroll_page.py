import time

from selenium.webdriver.support.select import Select
from selenium import webdriver

from pytest_bdd_practice.utils.constants import CHROME_PATH


class ScrollPage:
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.get("https://www.britannica.com/games/Word-Search")

    # scrolls down page by pixel
    driver.execute_script("window.scrollBy(0,1000)","")

    # scrolls untill load more button is displayed
    load_more = driver.find_element_by_id('__paginatedBrowseLoadMore')
    driver.execute_script("argument[0].scrollIntoView();",load_more)
