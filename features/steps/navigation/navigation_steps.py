from behave import given


@given("I am in login page")
def go_to_login_page(context):
    context.navigation.go_to("login")
