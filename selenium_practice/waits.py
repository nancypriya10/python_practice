import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pytest_bdd_practice.utils.constants import CHROME_PATH


class ExplicitWait:
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.get('https://www.expedia.com/')

    # clicks on flight button
    driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[1]/button').send_keys('SFO')
    driver.find_element_by_xpath('//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]').click()

    driver.find_element_by_xpath('//*[@id="location-field-leg1-destination-menu"]/div[1]/button').send_keys('NYC')
    driver.find_element_by_xpath('//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]').click()

    driver.find_element_by_xpath('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button').click()

    # explicit wait
    wait = WebDriverWait(driver,10)
    element = wait.until(expected_conditions.element_to_be_clickable(driver.find_element_by_id('stops-0')))
    element.click()