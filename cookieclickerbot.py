from selenium import webdriver

import actions
import utilities
from config_singleton import ConfigSingleton

config = ConfigSingleton().config


class CookieClickerBot:
    def __init__(self):
        self.__url = config["url"]
        self.__cookie_score_id = config["selectors"]["cookie_score_id"]
        self.__product_ids = config["selectors"]["product_ids"]
        self.__price_ids = config["selectors"]["price_ids"]
        self.__driver = self.__initialize_driver()

    def __initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=options)

    def __get_webpage(self):
        self.__driver.get(self.__url)

    def __get_int(self, locator, locator_type):
        text = utilities.get_text(self.__driver, locator, locator_type=locator_type)
        return utilities.parse_int(text)

    def __get_prices(self):
        prices = []
        for price in self.__price_ids:
            prices.append(self.__get_int(price, "id"))
        print(prices)

    def __setup(self):
        self.__get_webpage()
        actions.consent_gdpr(self.__driver)
        actions.select_english(self.__driver)
        actions.accept_cookies(self.__driver)
        actions.dismiss_google_privacy(self.__driver)
        actions.dismiss_backup_dialog(self.__driver)

    def __game_loop(self):
        while True:
            actions.click_cookie(self.__driver)
            # self.__get_prices()

    def run(self):
        self.__setup()
        self.__game_loop()
