from selenium.webdriver.common.by import By

input_username = (By.CSS_SELECTOR, 'input[data-testid="username"]')
continue_button = (By.ID, "login-submit")
input_password = (By.CSS_SELECTOR, 'input[data-testid="password"]')
trello_logo = (By.CSS_SELECTOR, 'div[data-testid="team25-header-logo"]')
user_avatar = (By.ID, "header-member-menu-avatar")
avatar_email_text = (
    By.CSS_SELECTOR,
    '[data-testid="account-menu-account-section"] div[class="RpQsLvDvZmhbBg"]',
)
