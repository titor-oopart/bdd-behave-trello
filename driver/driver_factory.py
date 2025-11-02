from selenium import webdriver


class DriverFactory:
    _driver = None

    @classmethod
    def get_driver(cls, browser_name, is_headless, windows_size="1920,1080"):
        if browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options = cls._driver_options(options, is_headless)
            cls._driver = webdriver.Firefox(
                options=options,
            )
        elif browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options = cls._driver_options(options, is_headless)
            cls._driver = webdriver.Chrome(options=options)
        elif browser_name.lower() == "edge":
            options = webdriver.EdgeOptions()
            options = cls._driver_options(options, is_headless)
            cls._driver = webdriver.Edge(options)
        cls._driver = cls._driver_window(cls._driver, windows_size)
        return cls._driver

    @staticmethod
    def _driver_options(options, is_headless):
        if is_headless.lower() == "true":
            options.add_argument("--headless")
        return options

    @staticmethod
    def _driver_window(driver, windows_size):
        if "," in windows_size:
            windows_size = windows_size.split(",")
            width = windows_size[0]
            height = windows_size[1]
            driver.set_window_size(width, height)
        else:
            driver.maximize_window()
        return driver
