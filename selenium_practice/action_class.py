from selenium.webdriver import ActionChains
from selenium import webdriver

from pytest_bdd_practice.utils.constants import CHROME_PATH


class ActionClass:
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.get('https://testautomationpractice.blogspot.com/')

    # implicit wait
    driver.implicitly_wait(10)
    assert driver.title == 'Automation Testing Practice'

    # double click on the element
    element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
    actions = ActionChains(driver)
    actions.double_click(element).perform()

    # mouse hover on element
    element = driver.find_element_by_id('age')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()



