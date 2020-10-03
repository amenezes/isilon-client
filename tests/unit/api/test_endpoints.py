import pytest

import isilon
from isilon.exceptions import TokenRetrieveException


@pytest.mark.asyncio
async def test_endpoints(isilon_client_mock):
    resp = await isilon_client_mock.endpoints()
    assert resp == 200


@pytest.mark.asyncio
async def test_info_failed_to_get_token():
    with pytest.raises(TokenRetrieveException):
        await isilon.endpoints()
