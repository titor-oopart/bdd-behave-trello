from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def find_element(context, locator, time=10):
    try:
        element = WebDriverWait(context.driver, time).until(
            EC.visibility_of_element_located(locator)
        )
        return element
    except TimeoutException:
        context.logger.error(f"Locator {locator[1]} was NOT found after {time}s.")
        assert False, f"❌ Element {locator[1]} was not found"


def click_element(context, locator, time=10):
    try:
        element = WebDriverWait(context.driver, time).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    except TimeoutException:
        context.logger.error(f"Locator {locator[1]} was NOT found after {time}s.")
        assert False, f"❌ Element {locator[1]} was not clickable"


def set_element_text(context, locator, text_value, time=10):
    element = find_element(context, locator, time)
    element.send_keys(text_value)


def get_element_text(context, locator, time=10):
    element = find_element(context, locator, time)
    return element.text
