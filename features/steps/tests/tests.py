from behave import given, when, then
from utils.common import find_element
from features.steps.tests import locators as loc


@given("steps 1")
def step_impl1(context):
    context.driver.get(context.BASE_URL)
    find_element(context, loc.example_css)


@when("steps 2")
def step_impl2(context):
    pass


@then("steps 3")
def step_impl3(context):
    pass
