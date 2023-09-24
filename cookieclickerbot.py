import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CookieClickerBot:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as file:
            self.__config = json.load(file)

        self.__url = self.__config["url"]
        self.__consent_button_css = self.__config["selectors"]["consent_button_css"]
        self.__english_button_id = self.__config["selectors"]["english_button_id"]
        self.__accept_cookies_css = self.__config["selectors"]["accept_cookies_css"]
        self.__google_privacy_css = self.__config["selectors"]["google_privacy_css"]
        self.__backup_dialog_css = self.__config["selectors"]["backup_dialog_css"]
        self.__cookie_css = self.__config["selectors"]["cookie_css"]
        self.__upgrade_button_css = self.__config["selectors"]["upgrade_button_css"]

        self.LOCATOR_MAP = {
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "id": By.ID,
            "link": By.LINK_TEXT,
            "name": By.NAME,
            "partial-link": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME,
            "xpath": By.XPATH,
        }

        self.__driver = self.__initialize_driver()
        self.__timer = time.time()

    def __initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=options)

    def __get_webpage(self):
        self.__driver.get(self.__url)

    def __click_button(
        self, locator_value, locator_type="css", wait_seconds=10, javascript=False
    ):
        by_locator = self.LOCATOR_MAP.get(locator_type, By.CSS_SELECTOR)

        button = WebDriverWait(self.__driver, wait_seconds).until(
            EC.element_to_be_clickable((by_locator, locator_value))
        )

        if javascript:
            self.__driver.execute_script("arguments[0].click();", button)
            return

        button.click()
        return

    def __consent_gdpr(self):
        self.__click_button(self.__consent_button_css)

    def __select_english(self):
        self.__click_button(self.__english_button_id, locator_type="id")

    def __accept_cookies(self):
        self.__click_button(self.__accept_cookies_css, javascript=True, wait_seconds=20)

    def __dismiss_google_privacy(self):
        self.__click_button(self.__google_privacy_css, wait_seconds=20)

    def __dismiss_backup_dialog(self):
        self.__click_button(self.__backup_dialog_css)

    def __click_cookie(self):
        pass

    def __buy_upgrade(self):
        pass

    def __setup(self):
        self.__get_webpage()
        self.__consent_gdpr()
        self.__select_english()
        self.__accept_cookies()
        self.__dismiss_google_privacy()
        self.__dismiss_backup_dialog()

    def __game_loop(self):
        while True:
            self.__click_cookie()
            self.__buy_upgrade()

    def run(self):
        self.__setup()
        # self.__game_loop()
