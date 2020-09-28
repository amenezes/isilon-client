import pytest


@pytest.mark.parametrize(
    "attribute",
    [
        "isilon_addr",
        "account",
        "user",
        "password",
        "http_client",
        "credentials",
        "objects",
        "discoverability",
        "containers",
        "endpoints",
        "accounts",
    ],
)
def test_attributes(isilon_client, attribute):
    assert hasattr(isilon_client, attribute)
