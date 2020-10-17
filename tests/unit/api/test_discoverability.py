import pytest

from isilon.client import IsilonClient
from isilon.exceptions import TokenRetrieveException


@pytest.mark.asyncio
async def test_info(isilon_client_mock):
    resp = await isilon_client_mock.discoverability.info()
    assert isinstance(resp, str)


@pytest.mark.asyncio
async def test_info_failed_to_get_token(token_exeption):
    client = IsilonClient()
    with pytest.raises(TokenRetrieveException):
        await client.discoverability.info()
