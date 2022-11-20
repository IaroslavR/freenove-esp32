"""CLI tool test-suit."""

from blueprint_python.cli import hello


def test_hello():
    assert hello("test") == "Hello test111"
