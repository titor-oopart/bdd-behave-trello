from behave import given, when, then
from utils.common import find_element
from features.steps.tests import locators as loc
from features.steps.navigation.navigation_page import NavigationPage


@given("steps 1")
def step_impl1(context):
    nav = NavigationPage(context)
    nav.go_to(" ")
    find_element(context, loc.example_css)


@when("steps 2")
def step_impl2(context):
    pass


@then("steps 3")
def step_impl3(context):
    pass
