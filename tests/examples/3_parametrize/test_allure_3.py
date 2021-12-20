import pytest


@pytest.fixture(params=[1, 2, 3])
def my_fixture():
    pass


@pytest.mark.parametrize('param1', [True, False], ids=['Истина', 'Ложь'])
def test_parameterize_with_fixture(param1, my_fixture):
    pass


@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
def test_parametrize_with_two_parameters(param1, param2):
    pass


@pytest.mark.parametrize('param1', [True], ids=['МойАлиас'])
@pytest.mark.parametrize('param2', ['value1', 'value2'])
@pytest.mark.parametrize('param3', [1])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    pass
