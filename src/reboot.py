# -*- coding: utf-8 -*-
import logging
import yaml
from os.path import abspath, dirname, join
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def do_login(driver, url, username, password):
    # Open login page
    driver.get(f"{url}cgi-bin/cgi?req=twz")

    # Input username and password
    try:
        element = driver.find_element_by_name('airstation_uname')
        element.clear()
        element.send_keys(username)
        element = driver.find_element_by_name('airstation_pass')
        element.send_keys(password)
    except NoSuchElementException:
        return

    # Click login button
    element = WebDriverWait(driver, 10).until(visibility_of_element_located((By.CLASS_NAME, 'button_login')))
    element.click()


def do_reboot(driver, url):

    # Wait for finished login
    try:
        driver.find_element_by_id('panel_ADVANCED')
    except NoSuchElementException as e:
        logging.exception(e)
        print(driver.page_source)
        return

    # Open reboot page
    driver.get(f"{url}cgi-bin/cgi?req=frm&frm=advanced.html&CAT=ADMIN&ITEM=INIT")
    element = driver.find_element_by_id('content_main')
    driver.switch_to.frame(element)

    # Wait for visible of reboot button and click it
    element = WebDriverWait(driver, 10).until(visibility_of_element_located((By.NAME, 'reboot')))
    element.click()


def main():

    # Load settings
    with open(join(dirname(abspath(__file__)), 'settings.yaml')) as fp:
        settings = yaml.load(fp.read())

    # Chrome headless mode
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1280,768')
    driver = Chrome(options=options)
    driver.implicitly_wait(3)

    do_login(driver, settings['common']['url'], settings['common']['username'], settings['common']['password'])
    do_reboot(driver, settings['common']['url'])

    # Task finished
    driver.stop_client()


if __name__ == '__main__':
    main()
