import pytest

from isilon.client import IsilonClient
from isilon.exceptions import TokenRetrieveException


@pytest.mark.asyncio
async def test_call(isilon_client_mock):
    resp = await isilon_client_mock.endpoints()
    assert resp == 200


@pytest.mark.asyncio
async def test_failed_to_get_token(token_exeption):
    client = IsilonClient()
    with pytest.raises(TokenRetrieveException):
        await client.endpoints()
