import pytest


@pytest.mark.asyncio
async def test_show(isilon_client_mock):
    resp = await isilon_client_mock.accounts.show("test")
    assert isinstance(resp, str)


@pytest.mark.asyncio
async def test_update(isilon_client_mock):
    resp = await isilon_client_mock.accounts.update("test")
    assert resp is not None


@pytest.mark.asyncio
async def test_metadata(isilon_client_mock):
    resp = await isilon_client_mock.accounts.metadata("test")
    assert "X-Object-Meta" in resp
