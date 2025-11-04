from behave import given, when, then

from features.steps.navigation.navigation_page import NavigationPage
from features.steps.login.login_page import LoginPage


@given("I am on login page")
def redirect_login_page(context):
    nav = NavigationPage(context)
    nav.go_to("/login")


@when("I ingress credentials")
def fill_credentials(context):
    context.login_page = LoginPage(context)
    context.login_page.fill_credentials_login()


@then("I can see the user on home page")
def user_home_page_validation(context):
    context.login_page.user_data_home_validation()


@then("I validate home page elements")
def home_page_elements_validation(context):
    context.login_page.home_page_elements_validation()
