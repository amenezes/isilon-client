import pytest

from isilon.exceptions import TokenRetrieveException


@pytest.mark.asyncio
async def test_token(creds):
    pass


@pytest.mark.asyncio
async def test_token_failed(creds):
    with pytest.raises(TokenRetrieveException):
        await creds.token("http://localhost:8080/token")


@pytest.mark.asyncio
async def test_x_auth_token(creds):
    pass


@pytest.mark.asyncio
async def test_x_auth_token_failed(creds):
    with pytest.raises(TokenRetrieveException):
        await creds.x_auth_token("http://localhost:8080/token")
