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
        self.__driver = self.__initialize_driver()
        self.__timer = time.time()

    def __initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(options=options)

    def __get_webpage(self):
        self.__driver.get(self.__url)

    def __click_button_with_xpath(self, xpath):
        button = WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        button.click()

    def __click_button_with_id(self, id):
        button = WebDriverWait(self.__driver, 30).until(
            EC.element_to_be_clickable((By.ID, id))
        )
        button.click()

    def __instant_click_button_with_class_name(self, class_name):
        button = self.__driver.find_element(By.CLASS_NAME, class_name)
        button.click()

    def __consent_gdpr(self):
        button = WebDriverWait(self._driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME,))
        )
        self.__instant_click_button_with_class_name(
            "fc-button fc-cta-consent fc-primary-button"
        )

    def __select_english(self):
        self.__click_button_with_xpath(
            "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]"
        )
        # Wait for the page to reload
        WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.ID, "bigCookie"))
        )

    def __click_cookie(self):
        cookie = WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.ID, "bigCookie"))
        )
        self.__driver.execute_script("arguments[0].click();", cookie)

    def __buy_upgrade(self):
        current_time = time.time()
        if (
            current_time - self.__timer >= 5
        ):  # I changed it from 5000 to 5 for 5 seconds
            try:
                print("Got to it!")
                self.instant_click_button_with_class_name("product unlocked enabled")
                print("Found it!")
                self.__timer = current_time
            except:
                print("Waiting...")
                pass

    def __game_loop(self):
        while True:
            self.__click_cookie()
            self.__buy_upgrade()

    def run(self):
        self.__get_webpage()
        # self.__consent_gdpr()
        # self.__select_english()
        # self.__game_loop()
