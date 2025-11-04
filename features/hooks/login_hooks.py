from features.hooks.hooks_driver import register_tag
from features.steps.login.login_page import LoginPage
from features.steps.navigation.navigation_page import NavigationPage


@register_tag("login", when="before")
def login_hook(context):
    navigation_page = NavigationPage(context)
    navigation_page.go_to("login")
    login_page = LoginPage(context)
    login_page.fill_credentials_login()
    login_page.home_page_elements_validation()


@register_tag("logout", when="after")
def logout_hook(context):
    context.login_page.logout()
