from main import foo, bye


def test_hello():
    assert foo() == "hello"


def test_bye():
    assert bye() == "bye"
