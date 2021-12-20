import allure

from selenium.common.exceptions import NoSuchElementException


def test_attachments_failed(driver):
    driver.get("https://yandex.ru")

    with allure.step("Прикрепил html"):

        allure.attach(
            body=driver.page_source,
            name='Attach_with_HTML_type',
            attachment_type=allure.attachment_type.HTML)
        with allure.step("Поиск элемента"):
            try:
                driver.find_element_by_css_selector("no-such-selector")
            except NoSuchElementException as e:
                allure.attach(
                    body=driver.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                raise AssertionError(e.msg)


def test_attachments_success(driver):
    driver.get("https://yandex.ru")
    with allure.step("Прикрепил html"):
        allure.attach(
            body='<h1>HTML is here</h1><span>And it is very good</span><br><a href="https://otus.ru">OTUS</a>',
            name='Attach_with_HTML_type',
            attachment_type=allure.attachment_type.HTML)
        with allure.step("Выполняю элемента"):
            try:
                driver.find_element_by_css_selector("input")
            except NoSuchElementException as e:
                allure.attach(body=driver.get_screenshot_as_png(),
                              name="screenshot_image")
                raise AssertionError(e.msg)
