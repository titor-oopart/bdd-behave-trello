from selenium import webdriver


def get_driver():
    driver = webdriver.Firefox()
    return driver
