import pytest
from _pytest.fixtures import Parser, FixtureRequest

from ui.fixtures import *


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--timeout', default=5)


@pytest.fixture(scope="session")
def configuration(request: FixtureRequest) -> dict:
    timeout = request.config.getoption('--timeout')

    return {
        'timeout': timeout
    }
