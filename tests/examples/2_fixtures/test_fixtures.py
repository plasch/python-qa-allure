def test_one(function_fixture, session_fixture):
    print("from test_one")
    assert 1


def test_two():
    print("from test_two")
    assert 0


def test_three(session_fixture):
    print("from test_three")
    assert 1


def test_four(function_fixture):
    print("from test_four")
    raise AssertionError("ERROR!!!!!!!!!!")
