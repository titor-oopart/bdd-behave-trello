from behave import given, when, then

from features.steps.login.login_page import LoginPage


@when("I ingress credentials")
def fill_credentials(context):
    context.login_page = LoginPage(context)
    context.login_page.fill_credentials_login()


@when("I logout")
def logout(context):
    context.login_page = LoginPage(context)
    context.login_page.logout()


@then("I should see the landing page")
def logout_validation(context):
    context.login_page.logout_validation()


@then("I can see the user on home page")
def user_home_page_validation(context):
    context.login_page.user_data_home_validation()


@then("I validate home page elements")
def home_page_elements_validation(context):
    context.login_page.home_page_elements_validation()
