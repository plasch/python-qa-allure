import logging
import os

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.actions = ActionChains(driver)
        self.__config_logger()

    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        if to_file:
            os.makedirs("logs", exist_ok=True)
            self.logger.addHandler(logging.FileHandler(f"logs/{self.driver.test_name}.log"))
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step("Opening url: {url}")
    def _open(self, url):
        self.logger.info(f"Opening url: {url}")
        self.driver.get(url)

    @allure.step("Click on element {locator}")
    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Input value {value} in {locator} input")
    def input_and_submit(self, locator, value):
        self.logger.info(f"Input {value} in input {locator}")
        find_field = self.wait.until(EC.presence_of_element_located(locator))
        find_field.click()
        find_field.clear()
        find_field.send_keys(value)
        find_field.send_keys(Keys.ENTER)

    @allure.step("Verify element {locator} present on screen")
    def is_present(self, locator):
        self.logger.info(f"Check if element {locator} is present")
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=f"{self.driver.current_url}",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Element {locator} was not found")
