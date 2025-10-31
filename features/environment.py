import os
from dotenv import load_dotenv
from driver import driver
from features.steps.navigation.navigation_page import NavigationPage
import logging

load_dotenv()


def before_all(context):
    logger_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(
        filename="bdd-behave-trello.log",
        level=logging.INFO,
        datefmt="%a, %d %b %Y %H:%M:%S",
        format=logger_format,
    )
    logger = logging.getLogger(__name__)

    context.driver = driver.get_driver()
    context.driver.fullscreen_window()
    context.USER_NAME = os.getenv("USER_NAME")
    context.USER_PASSWORD = os.getenv("USER_PASSWORD")
    context.BASE_URL = os.getenv("BASE_URL")
    context.API_URL = os.getenv("API_URL")
    context.API_KEY = os.getenv("API_KEY")
    context.API_TOKEN = os.getenv("API_TOKEN")
    context.navigation = NavigationPage(context)

    logger.info("=== Test session started ===")
    context.logger = logger


def after_all(context):
    context.driver.close()
    context.logger.info("=== Test session finished ===")
