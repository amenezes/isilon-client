class BaseAPI:
    API_VERSION = "v1"

    def __init__(self, client):
        self._client = client

    async def include_auth_header(self, headers: dict) -> dict:
        token = await self._client.credentials.x_auth_token()
        headers.update(token)
        return headers

    @property
    def address(self):
        return self._client.address

    @property
    def http(self):
        return self._client.http

    @property
    def account(self):
        return self._client.account
