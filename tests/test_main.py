from hello_world import get_greeting


def test_get_greeting_default():
    assert get_greeting() == "Hello, World!"

def test_get_greeting_custom():
    assert get_greeting("Python") == "Hello, Python!"
