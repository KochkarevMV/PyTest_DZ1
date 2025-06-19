import pytest

@pytest.fixture(scope='session')
def enter_exit_points():
    print("\nСтарт теста")
    yield
    print("\nКонец теста")


