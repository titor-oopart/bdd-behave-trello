import os
from dotenv import load_dotenv
from driver import driver

load_dotenv()


def before_all(context):
    context.driver = driver.get_driver()
    context.driver.fullscreen_window()
    context.USER_NAME = os.getenv("USER_NAME")
    context.USER_PASSWORD = os.getenv("USER_PASSWORD")
    context.BASE_URL = os.getenv("BASE_URL")
    context.API_KEY = os.getenv("API_KEY")
    context.API_TOKEN = os.getenv("API_TOKEN")


def after_all(context):
    context.driver.close()
