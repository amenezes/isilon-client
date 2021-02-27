import pytest

from isilon.client import IsilonClient
from isilon.exceptions import TokenRetrieveException


@pytest.mark.asyncio
async def test_call(isilon_client_mock):
    resp = await isilon_client_mock.endpoints()
    assert resp == ""


@pytest.mark.asyncio
async def test_failed_to_get_token(token_exeption, http):
    client = IsilonClient(http=http)
    with pytest.raises(TokenRetrieveException):
        await client.endpoints()
