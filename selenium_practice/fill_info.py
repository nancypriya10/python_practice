from selenium import webdriver
from selenium.webdriver.support.select import Select

from pytest_bdd_practice.utils.constants import CHROME_PATH


class FillInfo:
    driver = webdriver.Chrome(executable_path=CHROME_PATH)

    driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
    assert driver.find_element_by_xpath('//*[@id="Blog1"]/div/article/div/div/h3').text == 'Selenium Practice Form'

    # fills first name
    driver.find_element_by_name('firstname').send_keys('Joseph')
    # fills last name
    driver.find_element_by_name('lastname').send_keys('Albert')
    # selects male as gender
    driver.find_elements_by_name('sex')[0].click()
    # selects exp as 5
    driver.find_element_by_id('exp-4').click()
    # selects date
    driver.find_element_by_id('datepicker').send_keys('05/07/2021')
    # selects profession as automation tester
    driver.find_element_by_id('profession-1').click()
    # selects automation tool as selenium
    driver.find_element_by_id('tool-2').click()

    # selects Asia Dropdown
    drp = Select(driver.find_element_by_name("continents"))
    drp.select_by_visible_text('Asia')
    # clicks the submit button
    driver.find_element_by_name('submit').click()
