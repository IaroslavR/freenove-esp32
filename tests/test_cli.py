"""CLI tool test-suit."""

from freenove_esp32.cli import hello


def test_hello():
    assert hello() == "hello"
