from utils.common import (
    find_element,
    get_element_text,
    set_element_text,
    click_element,
)

import features.steps.login.login_locators as loc


class LoginPage:
    def __init__(self, context):
        self.context = context

    def fill_credentials_login(self):
        set_element_text(self.context, loc.input_username, self.context.USER_NAME)
        click_element(self.context, loc.continue_button)
        set_element_text(self.context, loc.input_password, self.context.USER_PASSWORD)
        click_element(self.context, loc.continue_button)

    def user_data_home_validation(self):
        click_element(self.context, loc.user_avatar)
        actual = get_element_text(self.context, loc.avatar_email_text)
        expected = self.context.USER_NAME
        assert expected == actual

    def home_page_elements_validation(self):
        find_element(self.context, loc.trello_logo)
