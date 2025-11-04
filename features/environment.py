import os
import datetime
import allure
import logging
from dotenv import load_dotenv
from driver.driver_factory import DriverFactory
from features.steps.navigation.navigation_page import NavigationPage
from features.hooks.hooks_driver import HOOK_REGISTRY

import importlib
import pkgutil
import features.hooks

for modules_names in pkgutil.iter_modules(features.hooks.__path__):
    module_name = modules_names[1]
    importlib.import_module(f"features.hooks.{module_name}")


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

    browser = os.getenv("BROWSER")
    is_headless = os.getenv("HEADLESS")
    windows_size = os.getenv("WINDOW_SIZE")
    context.driver = DriverFactory.get_driver(browser, is_headless, windows_size)
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


def after_step(context, step):
    if step.status == "failed":
        name = f"{context.scenario.name} - {step.name}_{int(datetime.datetime.now().timestamp())}.png"
        os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
        path = os.path.join("screenshot", name)
        context.driver.save_screenshot(path)
        allure.attach.file(
            path,
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )


def before_tag(context, tag):
    hook = HOOK_REGISTRY["before"].get(tag)
    if hook:
        hook(context)


def after_tag(context, tag):
    hook = HOOK_REGISTRY["after"].get(tag)
    if hook:
        hook(context)
