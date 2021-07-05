import time

from selenium.webdriver.support.select import Select
from selenium import webdriver

from pytest_bdd_practice.utils.constants import CHROME_PATH


class HandleAlerts:
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.get('https://testautomationpractice.blogspot.com/')

    #clicks on click me button
    driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
    time.sleep(5)
    # Accepts alert
    driver.switch_to.alert.accept()
    assert driver.find_element_by_id('demo').text == 'You pressed OK!'

    # clicks on click me button
    driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
    time.sleep(5)
    # Cancel alert
    driver.switch_to.alert.dismiss()
    assert driver.find_element_by_id('demo').text == 'You pressed Cancel!'
