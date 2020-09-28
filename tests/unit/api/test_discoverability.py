import pytest

from isilon.exceptions import TokenRetrieveException


@pytest.mark.asyncio
async def test_info(isilon_client_mock):
    resp = await isilon_client_mock.discoverability.info()
    assert isinstance(resp, str)


@pytest.mark.asyncio
async def test_info_failed_to_get_token(isilon_client):
    with pytest.raises(TokenRetrieveException):
        await isilon_client.discoverability.info()
