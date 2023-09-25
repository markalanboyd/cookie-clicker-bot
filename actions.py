import utilities
from config_singleton import ConfigSingleton

config = ConfigSingleton().config
consent_button_css = config["selectors"]["consent_button_css"]
english_button_id = config["selectors"]["english_button_id"]
accept_cookies_css = config["selectors"]["accept_cookies_css"]
google_privacy_css = config["selectors"]["google_privacy_css"]
backup_dialog_css = config["selectors"]["backup_dialog_css"]
cookie_id = config["selectors"]["cookie_id"]


def consent_gdpr(driver):
    utilities.click_button(driver, consent_button_css)


def select_english(driver):
    utilities.click_button(driver, english_button_id, locator_type="id")


def accept_cookies(driver):
    utilities.click_button(driver, accept_cookies_css, javascript=True, wait_seconds=20)


def dismiss_google_privacy(driver):
    utilities.click_button(driver, google_privacy_css, wait_seconds=20)


def dismiss_backup_dialog(driver):
    utilities.click_button(driver, backup_dialog_css)


def click_cookie(driver):
    utilities.click_button(driver, cookie_id, locator_type="id")
