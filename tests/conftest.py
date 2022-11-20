"""Package-wide test fixtures and hooks."""
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--runintegration",
        action="store_true",
        help="run integration tests",
    )


def pytest_runtest_setup(item):
    with_integration = item.config.getvalue("runintegration")
    if "integration" in item.keywords and not with_integration:
        pytest.skip("need --runintegration option to run this test")
    elif "integration" not in item.keywords and with_integration:
        pytest.skip("started with --runintegration option")
