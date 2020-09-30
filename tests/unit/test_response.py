import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "attribute",
    ["status", "http_version", "url", "headers", "method"],
)
async def test_properties(http, attribute):
    response = await http.get("https://httpbin.org/get")
    assert hasattr(response, attribute)


@pytest.mark.asyncio
async def test_repr(http):
    response = await http.get("https://httpbin.org/get")
    assert str(response).startswith("Response")


@pytest.mark.asyncio
async def test_text(http):
    response = await http.get("https://httpbin.org/get")
    text = await response.text()
    assert isinstance(text, str)


@pytest.mark.asyncio
async def test_json(http):
    response = await http.get("https://httpbin.org/json")
    json = await response.json()
    assert isinstance(json, dict)
