from behave import given

from features.steps.navigation.navigation_page import NavigationPage


@given('I am on "{path}" page')
def go_to_login_page(context, path):
    nav = NavigationPage(context)
    nav.go_to(path)
