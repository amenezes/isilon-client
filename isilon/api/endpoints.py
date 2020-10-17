from isilon.api.base import BaseAPI


class Endpoints(BaseAPI):
    async def __call__(self, headers: dict = {}, **kwargs):
        """List endpoints."""
        await self.include_auth_header(headers)
        async with self.http.get(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/endpoints",
            headers=headers,
            **kwargs,
        ) as resp:
            return resp.status
