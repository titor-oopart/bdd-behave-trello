from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(context, locator, time=10):
    try:
        element = WebDriverWait(context.driver, time).until(
            EC.presence_of_element_located(locator)
        )
    finally:
        print("the locator was not found")
    return element
