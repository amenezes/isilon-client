from isilon.api.base import BaseAPI


class Accounts(BaseAPI):
    async def show(self, account_name: str, headers: dict = {}, **kwargs):
        """Show account details and list containers."""
        await self.include_auth_header(headers)
        async with self.http.get(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{account_name}?format=json",
            headers=headers,
            **kwargs,
        ) as resp:
            response = await resp.json()
            return response

    async def update(self, account_name: str, headers: dict = {}, **kwargs):
        """Create, update, or delete account metadata."""
        await self.include_auth_header(headers)
        async with self.http.post(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{account_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return resp

    async def metadata(self, account_name: str, headers: dict = {}, **kwargs):
        """Show account metadata."""
        await self.include_auth_header(headers)
        async with self.http.head(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{account_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return dict(resp.headers)
