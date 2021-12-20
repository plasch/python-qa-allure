import pytest


@pytest.fixture
def function_fixture(request):
    print("Function setup")
    def fin(): print("Function finalizer")
    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print("Session setup")
    def fin(): print("Session finalizer")
    request.addfinalizer(fin)
