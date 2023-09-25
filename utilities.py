from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOCATOR_MAP = {
    "class": By.CLASS_NAME,
    "css": By.CSS_SELECTOR,
    "id": By.ID,
    "link": By.LINK_TEXT,
    "name": By.NAME,
    "partial-link": By.PARTIAL_LINK_TEXT,
    "tag": By.TAG_NAME,
    "xpath": By.XPATH,
}


def get_text(driver, locator_value, locator_type="css", wait_seconds=10):
    by_locator = LOCATOR_MAP.get(locator_type, By.CSS_SELECTOR)
    try:
        text = (
            WebDriverWait(driver, wait_seconds)
            .until(EC.presence_of_element_located((by_locator, locator_value)))
            .text
        )
        return text
    except:
        pass


def parse_int(score_text):
    if score_text != None:
        return int(score_text.split(" ")[0].replace(",", ""))
    return None


def click_button(
    driver, locator_value, locator_type="css", wait_seconds=10, javascript=False
):
    by_locator = LOCATOR_MAP.get(locator_type, By.CSS_SELECTOR)

    button = WebDriverWait(driver, wait_seconds).until(
        EC.element_to_be_clickable((by_locator, locator_value))
    )

    if javascript:
        driver.execute_script("arguments[0].click();", button)
        return

    button.click()
    return
