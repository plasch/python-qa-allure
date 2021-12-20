import allure


@allure.feature('Authorization')
@allure.story('Valid credentials')
@allure.title('Authorization with admin credentials')
def test_with_epic_1():
    pass


@allure.feature('Authorization')
@allure.story('Valid credentials')
@allure.title('Authorization with user credentials')
def test_authorization_user_credentials():
    assert False
