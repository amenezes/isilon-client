import pytest

from isilon.client import IsilonClient
from isilon.exceptions import TokenRetrieveException


@pytest.mark.asyncio
async def test_token(isilon_client_mock):
    token = await isilon_client_mock.credentials.token()
    assert token == "abc123lkj"


@pytest.mark.asyncio
async def test_token_failed(token_exeption, http):
    client = IsilonClient(http=http)
    with pytest.raises(TokenRetrieveException):
        await client.credentials.token()


@pytest.mark.asyncio
async def test_x_auth_token(isilon_client_mock):
    auth_token = await isilon_client_mock.credentials.x_auth_token()
    assert auth_token == {"X-Auth-Token": "abc123lkj"}


@pytest.mark.asyncio
async def test_x_auth_token_failed(token_exeption, http):
    client = IsilonClient(http=http)
    with pytest.raises(TokenRetrieveException):
        await client.credentials.x_auth_token()
