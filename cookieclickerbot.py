import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


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
        self.__cookie_id = self.__config["selectors"]["cookie_id"]
        self.__cookie_score_id = self.__config["selectors"]["cookie_score_id"]
        self.__product_ids = self.__config["selectors"]["product_ids"]
        self.__price_ids = self.__config["selectors"]["price_ids"]

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

    def __get_text(self, locator_value, locator_type="css", wait_seconds=10):
        by_locator = self.LOCATOR_MAP.get(locator_type, By.CSS_SELECTOR)
        try:
            text = (
                WebDriverWait(self.__driver, wait_seconds)
                .until(EC.presence_of_element_located((by_locator, locator_value)))
                .text
            )
            return text
        except TimeoutException:
            return None

    def __parse_int(self, score_text):
        if score_text != None:
            return int(score_text.split(" ")[0].replace(",", ""))
        return None

    def __get_int(self, locator, locator_type):
        text = self.__get_text(locator, locator_type=locator_type)
        return self.__parse_int(text)

    def __get_prices(self):
        prices = []
        for price in self.__price_ids:
            prices.append(self.__get_int(price, "id"))
        print(prices)

    # def __buy_upgrade(self):
    #     score = self.__get_int()
    #     if score % 100 == 0 and score > 100:
    #         self.__click_button(self.__grandma_id, locator_type="id")

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
        self.__click_button(self.__cookie_id, locator_type="id")

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
            self.__get_prices()

    def run(self):
        self.__setup()
        self.__game_loop()
